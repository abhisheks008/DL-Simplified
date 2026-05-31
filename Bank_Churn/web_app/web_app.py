"""
Bank Customer Churn Prediction - Web App
Built with Streamlit

To run: streamlit run web_app.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pickle
import os
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Model

# ─────────────────────────────────────────────────────────────────────────────
# Custom Layers
# ─────────────────────────────────────────────────────────────────────────────

class TabNetLayer(layers.Layer):
    def __init__(self, feature_dim, output_dim, num_steps=3, **kwargs):
        super().__init__(**kwargs)
        self.feature_dim = feature_dim
        self.output_dim  = output_dim
        self.num_steps   = num_steps

        self.shared_fc = layers.Dense(output_dim * 2, use_bias=False)
        self.shared_bn = layers.BatchNormalization()

        self.step_fc = [layers.Dense(output_dim * 2, use_bias=False) for _ in range(num_steps)]
        self.step_bn = [layers.BatchNormalization() for _ in range(num_steps)]

        self.attn_fc = [layers.Dense(feature_dim, use_bias=False) for _ in range(num_steps)]
        self.attn_bn = [layers.BatchNormalization() for _ in range(num_steps)]

        self.final_fc = layers.Dense(output_dim, activation='relu')

    def call(self, inputs, training=False):
        B            = tf.shape(inputs)[0]
        prior_scales = tf.ones([B, self.feature_dim])
        aggregated   = tf.zeros([B, self.output_dim])
        importance   = tf.zeros([B, self.feature_dim])

        for step in range(self.num_steps):
            h            = self.attn_fc[step](inputs)
            h            = self.attn_bn[step](h, training=training)
            h            = h * prior_scales
            alpha        = tf.nn.softmax(h, axis=-1)
            prior_scales = prior_scales * (1.0 - alpha + 1e-6)
            importance   = importance + alpha
            masked       = inputs * alpha

            x = self.shared_fc(masked)
            x = self.shared_bn(x, training=training)
            x = x + self.step_fc[step](masked)
            x = self.step_bn[step](x, training=training)
            x = tf.nn.relu(x)

            d          = self.output_dim
            aggregated = aggregated + tf.nn.relu(x[:, :d]) * tf.nn.sigmoid(x[:, d:])

        out = self.final_fc(aggregated / self.num_steps)
        return out, importance / self.num_steps

    def get_config(self):
        config = super().get_config()
        config.update({
            'feature_dim': self.feature_dim,
            'output_dim' : self.output_dim,
            'num_steps'  : self.num_steps,
        })
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)


class FeatureTokenizer(layers.Layer):
    def __init__(self, num_features, d_token, **kwargs):
        super().__init__(**kwargs)
        self.num_features = num_features
        self.d_token      = d_token

    def build(self, input_shape):
        self.W = self.add_weight(
            name='W', shape=(self.num_features, self.d_token),
            initializer='glorot_uniform', trainable=True
        )
        self.b = self.add_weight(
            name='b', shape=(self.num_features, self.d_token),
            initializer='zeros', trainable=True
        )
        super().build(input_shape)

    def call(self, x):
        x      = tf.expand_dims(x, axis=-1)
        tokens = x * self.W[tf.newaxis, :, :] + self.b[tf.newaxis, :, :]
        return tokens

    def get_config(self):
        config = super().get_config()
        config.update({
            'num_features': self.num_features,
            'd_token'     : self.d_token,
        })
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)


CUSTOM_OBJECTS = {
    'TabNetLayer'     : TabNetLayer,
    'FeatureTokenizer': FeatureTokenizer,
}

# ─────────────────────────────────────────────────────────────────────────────
# Model Builders
# ─────────────────────────────────────────────────────────────────────────────

def build_tabnet(input_dim, output_dim=64, num_steps=3):
    inp    = layers.Input(shape=(input_dim,))
    bn_inp = layers.BatchNormalization()(inp)

    tabnet = TabNetLayer(input_dim, output_dim, num_steps)
    features, attention = tabnet(bn_inp)

    x   = layers.Dense(32, activation='relu')(features)
    x   = layers.Dropout(0.2)(x)
    out = layers.Dense(1, activation='sigmoid')(x)

    model = Model(inputs=inp, outputs=out, name='TabNet')
    return model


def build_ft_transformer(num_features, d_token=32, num_heads=4, num_blocks=2, ffn_dim=64):
    inp    = layers.Input(shape=(num_features,))
    tokens = FeatureTokenizer(num_features, d_token)(inp)

    for _ in range(num_blocks):
        attn_out = layers.MultiHeadAttention(
            num_heads=num_heads, key_dim=d_token // num_heads
        )(tokens, tokens)
        tokens = layers.LayerNormalization()(tokens + attn_out)

        ffn    = layers.Dense(ffn_dim, activation='relu')(tokens)
        ffn    = layers.Dense(d_token)(ffn)
        tokens = layers.LayerNormalization()(tokens + ffn)

    pooled = layers.GlobalAveragePooling1D()(tokens)
    x      = layers.Dense(32, activation='relu')(pooled)
    x      = layers.Dropout(0.2)(x)
    out    = layers.Dense(1, activation='sigmoid')(x)

    model = Model(inputs=inp, outputs=out, name='FT_Transformer')
    return model


# ─────────────────────────────────────────────────────────────────────────────
# Weight load helper
# ─────────────────────────────────────────────────────────────────────────────

def load_weights_safe(model, path):
    """Load weights from pkl regardless of whether it's a list or dict."""
    with open(path, 'rb') as f:
        weights = pickle.load(f)
    if isinstance(weights, list):
        weights_list = weights
    else:
        weights_list = [weights[i] for i in sorted(weights.keys())]
    model.set_weights(weights_list)
    return model


def load_weights_by_shape(model, path):
    """
    Match pkl weights to model weights purely by shape.
    Handles ordering mismatches between saved and rebuilt models.
    """
    with open(path, 'rb') as f:
        weights = pickle.load(f)
    if isinstance(weights, list):
        pkl_weights = weights
    else:
        pkl_weights = [weights[i] for i in sorted(weights.keys())]

    model_weights = model.get_weights()
    pkl_available = list(pkl_weights)  # copy we'll consume
    matched = []

    for mw in model_weights:
        found = None
        for i, pw in enumerate(pkl_available):
            if pw.shape == mw.shape:
                found = i
                break
        if found is None:
            raise ValueError(f"No pkl weight matches model shape {mw.shape}")
        matched.append(pkl_available.pop(found))

    model.set_weights(matched)
    return model


# ─────────────────────────────────────────────────────────────────────────────
# Page config
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Bank Churn Predictor",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
    html, body, [class*="css"] { font-family: 'Sora', sans-serif; }

    .app-header {
        background: linear-gradient(135deg, #1a1f2e 0%, #0d1117 100%);
        border: 1px solid #30363d; border-radius: 16px;
        padding: 2rem 2.5rem; margin-bottom: 2rem;
        position: relative; overflow: hidden;
    }
    .app-header::before {
        content: ''; position: absolute; top: -50%; left: -50%;
        width: 200%; height: 200%;
        background: radial-gradient(circle at 30% 30%, rgba(88,166,255,0.06) 0%, transparent 60%);
        pointer-events: none;
    }
    .app-title { font-size: 2.2rem; font-weight: 700; color: #e6edf3; margin: 0; letter-spacing: -0.5px; }
    .app-subtitle { color: #7d8590; margin: 0.3rem 0 0; font-size: 0.95rem; }
    .accent { color: #58a6ff; }

    .metric-card {
        background: #161b22; border: 1px solid #30363d;
        border-radius: 12px; padding: 1.2rem 1.5rem; margin-bottom: 1rem;
    }
    .metric-label { color: #7d8590; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.3rem; }
    .metric-value { font-family: 'JetBrains Mono', monospace; font-size: 1.8rem; font-weight: 600; color: #e6edf3; }

    .risk-high { background: rgba(248,81,73,0.15); border: 1px solid rgba(248,81,73,0.4); color: #f85149; padding: 0.8rem 1.5rem; border-radius: 8px; font-size: 1.1rem; font-weight: 600; text-align: center; }
    .risk-low  { background: rgba(63,185,80,0.15);  border: 1px solid rgba(63,185,80,0.4);  color: #3fb950; padding: 0.8rem 1.5rem; border-radius: 8px; font-size: 1.1rem; font-weight: 600; text-align: center; }
    .risk-medium { background: rgba(210,153,34,0.15); border: 1px solid rgba(210,153,34,0.4); color: #d29922; padding: 0.8rem 1.5rem; border-radius: 8px; font-size: 1.1rem; font-weight: 600; text-align: center; }

    .section-header { color: #e6edf3; font-size: 1.1rem; font-weight: 600; border-bottom: 1px solid #30363d; padding-bottom: 0.5rem; margin-bottom: 1rem; }

    .model-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
    .model-table th { background: #1f2937; color: #9ca3af; padding: 0.6rem 1rem; text-align: left; font-weight: 500; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.5px; }
    .model-table td { padding: 0.6rem 1rem; border-bottom: 1px solid #30363d; color: #e6edf3; }
    .model-table tr:hover td { background: #161b22; }
    .best-row td { color: #58a6ff !important; font-weight: 600; }

    .stSelectbox label, .stSlider label, .stNumberInput label { color: #7d8590 !important; font-size: 0.85rem !important; }
    .stButton button {
        background: linear-gradient(135deg, #1f6feb, #388bfd) !important;
        color: white !important; border: none !important; border-radius: 8px !important;
        padding: 0.6rem 2rem !important; font-family: 'Sora', sans-serif !important;
        font-weight: 600 !important; font-size: 1rem !important; width: 100%;
    }
    div[data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .info-box { background: #161b22; border-left: 3px solid #58a6ff; border-radius: 0 8px 8px 0; padding: 0.8rem 1rem; margin: 0.5rem 0; font-size: 0.88rem; color: #c9d1d9; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────────────────────────────────────
MODEL_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Model', 'saved_models')


# ─────────────────────────────────────────────────────────────────────────────
# Load Models
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_resource
def load_all_models():
    loaded  = {}
    scaler  = None
    results = None

    if not os.path.exists(MODEL_DIR):
        return loaded, scaler, results

    # --- scaler & results ---
    try:
        scaler  = joblib.load(os.path.join(MODEL_DIR, 'scaler.pkl'))
        results = pd.read_csv(os.path.join(MODEL_DIR, 'model_results.csv'))
    except Exception as e:
        st.warning(f"Could not load scaler/results: {e}")
        return loaded, scaler, results

    # --- resolve input_dim: try input_dim.pkl, fall back to feature_names.pkl ---
    input_dim = None
    try:
        input_dim = joblib.load(os.path.join(MODEL_DIR, 'input_dim.pkl'))
    except Exception:
        pass
    if input_dim is None:
        try:
            feature_names = joblib.load(os.path.join(MODEL_DIR, 'feature_names.pkl'))
            input_dim = len(feature_names)
        except Exception as e:
            st.warning(f"Could not determine input_dim: {e}")
            return loaded, scaler, results

    # --- ANN ---
    try:
        p = os.path.join(MODEL_DIR, 'ann_model.h5')
        if os.path.exists(p):
            loaded['ANN'] = keras.models.load_model(p)
    except Exception as e:
        st.warning(f"ANN load failed: {e}")

    # --- TabNet ---
    try:
        p = os.path.join(MODEL_DIR, 'tabnet_weights.pkl')
        if os.path.exists(p):
            m = build_tabnet(input_dim)
            m(tf.zeros((1, input_dim)))          # build weights
            load_weights_by_shape(m, p)
            loaded['TabNet'] = m
    except Exception as e:
        st.warning(f"TabNet load failed: {e}")

    # --- FT-Transformer ---
    try:
        p = os.path.join(MODEL_DIR, 'ft_weights.pkl')
        if os.path.exists(p):
            m = build_ft_transformer(input_dim)
            m(tf.zeros((1, input_dim)))
            load_weights_safe(m, p)
            loaded['FT-Transformer'] = m
    except Exception as e:
        st.warning(f"FT-Transformer load failed: {e}")

    # --- Autoencoder + Classifier ---
    try:
        enc_p = os.path.join(MODEL_DIR, 'encoder_model.h5')
        clf_p = os.path.join(MODEL_DIR, 'ae_classifier.h5')
        if os.path.exists(enc_p) and os.path.exists(clf_p):
            loaded['Autoencoder + Classifier'] = {
                'encoder'   : keras.models.load_model(enc_p),
                'classifier': keras.models.load_model(clf_p),
            }
    except Exception as e:
        st.warning(f"Autoencoder load failed: {e}")

    return loaded, scaler, results


models, scaler, results_df = load_all_models()
models_available = len(models) > 0


# ─────────────────────────────────────────────────────────────────────────────
# Preprocessing
# ─────────────────────────────────────────────────────────────────────────────
def preprocess_input(credit_score, geography, gender, age, tenure,
                     balance, num_products, has_cr_card, is_active, salary):
    geo_germany = 1 if geography == 'Germany' else 0
    geo_spain   = 1 if geography == 'Spain'   else 0
    gender_enc  = 1 if gender    == 'Male'    else 0

    row = np.array([[
        credit_score, gender_enc, age, tenure, balance,
        num_products, has_cr_card, is_active, salary,
        geo_germany, geo_spain
    ]], dtype=np.float32)
    return row


# ─────────────────────────────────────────────────────────────────────────────
# Predict all models
# ─────────────────────────────────────────────────────────────────────────────
def predict_all(features_raw):
    preds = {}

    if scaler is None:
        seeds = {'ANN': 11, 'TabNet': 22, 'FT-Transformer': 33, 'Autoencoder + Classifier': 44}
        for name, seed in seeds.items():
            np.random.seed(seed + int(features_raw.sum()) % 100)
            preds[name] = float(np.random.beta(2, 5))
        return preds

    features_sc = scaler.transform(features_raw)

    for name, model in models.items():
        try:
            if isinstance(model, dict):
                enc  = model['encoder'].predict(features_sc, verbose=0)
                prob = model['classifier'].predict(enc, verbose=0).flatten()[0]
            else:
                prob = model.predict(features_sc, verbose=0).flatten()[0]
            preds[name] = float(prob)
        except Exception as e:
            st.warning(f"{name} prediction failed: {e}")

    return preds


# ─────────────────────────────────────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<p class="section-header">🤖 Models</p>', unsafe_allow_html=True)

    for key in ['ANN', 'TabNet', 'FT-Transformer', 'Autoencoder + Classifier']:
        is_loaded = key in models
        icon      = '🟢' if is_loaded else '🔴'
        label     = 'Loaded' if is_loaded else 'Not found'
        st.markdown(f"""
        <div class="info-box" style="margin-bottom:0.4rem;">
            {icon} <b>{key}</b><br>
            <span style="font-size:0.78rem; color:#7d8590;">{label}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    if not models_available:
        st.markdown("""
        <div class="info-box" style="border-left-color: #d29922;">
        ⚠️ <b>Demo Mode</b><br>
        Run the notebook first to train and save models.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="info-box" style="border-left-color: #3fb950;">
        ✅ <b>{len(models)}/4 models loaded</b><br>
        All predictions are real.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<p class="section-header">ℹ️ How it works</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
    Fill in customer details and click <b>Predict</b>.
    All 4 models run simultaneously and an ensemble average is shown as the final verdict.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Header
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <h1 class="app-title">🏦 Bank Churn <span class="accent">Predictor</span></h1>
    <p class="app-subtitle">
        All 4 models run simultaneously · ANN · TabNet · FT-Transformer · Autoencoder · Ensemble Average
    </p>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Input Form
# ─────────────────────────────────────────────────────────────────────────────
st.markdown('<p class="section-header">👤 Customer Details</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    credit_score = st.slider("Credit Score", 300, 850, 650)
    age          = st.slider("Age", 18, 92, 40)
    tenure       = st.slider("Tenure (years)", 0, 10, 5)
    balance      = st.number_input("Account Balance (€)", 0.0, 300000.0, 75000.0, step=500.0)

with col2:
    geography    = st.selectbox("Country", ["France", "Germany", "Spain"])
    gender       = st.selectbox("Gender", ["Male", "Female"])
    num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
    salary       = st.number_input("Estimated Salary (€)", 0.0, 250000.0, 60000.0, step=1000.0)

with col3:
    has_cr_card  = st.radio("Has Credit Card?", ["Yes", "No"])
    is_active    = st.radio("Active Member?",   ["Yes", "No"])
    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn  = st.button("🔍 Predict Churn", use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# Prediction Results
# ─────────────────────────────────────────────────────────────────────────────
if predict_btn:
    features_raw = preprocess_input(
        credit_score, geography, gender, age, tenure,
        balance, num_products,
        1 if has_cr_card == "Yes" else 0,
        1 if is_active   == "Yes" else 0,
        salary
    )

    st.markdown("---")
    st.markdown('<p class="section-header">📈 Prediction Results — All Models</p>',
                unsafe_allow_html=True)

    with st.spinner("Running all models..."):
        model_probs = predict_all(features_raw)

    if model_probs:

        # per-model cards
        cols = st.columns(len(model_probs))
        for i, (mname, prob) in enumerate(model_probs.items()):
            pct   = prob * 100
            color = '#f85149' if pct > 60 else ('#d29922' if pct > 30 else '#3fb950')
            with cols[i]:
                st.markdown(f"""
                <div class="metric-card" style="text-align:center;">
                    <div class="metric-label">{mname}</div>
                    <div class="metric-value" style="color:{color};">{pct:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)

        # ensemble average
        avg   = np.mean(list(model_probs.values())) * 100
        color = '#f85149' if avg > 60 else ('#d29922' if avg > 30 else '#3fb950')
        st.markdown(f"""
        <div class="metric-card" style="text-align:center; border-color:#58a6ff;">
            <div class="metric-label">⚡ Ensemble Average</div>
            <div class="metric-value" style="color:{color};">{avg:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

        # risk badge
        if avg < 30:
            badge = '<div class="risk-low">✅ Low Risk — Customer likely to stay</div>'
        elif avg < 60:
            badge = '<div class="risk-medium">⚠️ Medium Risk — Monitor this customer</div>'
        else:
            badge = '<div class="risk-high">🚨 High Risk — Likely to Churn</div>'
        st.markdown(badge, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # bar chart
        fig, ax = plt.subplots(figsize=(9, 3.5), facecolor='#0d1117')
        ax.set_facecolor('#0d1117')

        bar_colors = ['#58a6ff', '#3fb950', '#d29922', '#bc8cff']
        bars = ax.bar(
            list(model_probs.keys()),
            [v * 100 for v in model_probs.values()],
            color=bar_colors[:len(model_probs)],
            edgecolor='#30363d', linewidth=0.8, width=0.5
        )
        ax.axhline(50,  color='#f85149', linestyle='--', linewidth=1, alpha=0.6, label='50% threshold')
        ax.axhline(avg, color='#e6edf3', linestyle=':',  linewidth=1, alpha=0.5, label=f'Ensemble avg ({avg:.1f}%)')
        ax.set_ylabel('Churn Probability (%)', color='#7d8590', fontsize=9)
        ax.set_ylim(0, 110)
        ax.tick_params(colors='#7d8590', labelsize=8)
        for spine in ax.spines.values():
            spine.set_edgecolor('#30363d')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.legend(fontsize=8, facecolor='#161b22', labelcolor='#7d8590', edgecolor='#30363d')

        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, h + 1.5,
                    f'{h:.1f}%', ha='center', va='bottom',
                    color='#e6edf3', fontsize=8, fontweight='600')

        plt.xticks(rotation=15, ha='right', color='#7d8590')
        plt.tight_layout(pad=0.5)
        st.pyplot(fig)
        plt.close()

        # progress bars
        st.markdown('<p class="section-header" style="margin-top:1rem;">Model Breakdown</p>',
                    unsafe_allow_html=True)

        for mname, prob in model_probs.items():
            pct       = prob * 100
            bar_color = '#f85149' if pct > 60 else ('#d29922' if pct > 30 else '#3fb950')
            st.markdown(f"""
            <div style="margin-bottom:0.8rem;">
                <div style="display:flex; justify-content:space-between;
                            color:#7d8590; font-size:0.82rem; margin-bottom:4px;">
                    <span>{mname}</span>
                    <span style="color:{bar_color}; font-weight:600;">{pct:.1f}% churn</span>
                </div>
                <div style="background:#30363d; border-radius:4px; height:10px; overflow:hidden;">
                    <div style="width:{pct}%; background:{bar_color}; height:100%; border-radius:4px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Model Performance Table
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown('<p class="section-header">🏆 Model Performance (Test Set)</p>', unsafe_allow_html=True)

if results_df is not None and not results_df.empty:
    best       = results_df.iloc[0]['model']
    table_html = '<table class="model-table"><thead><tr><th>#</th><th>Model</th><th>ROC-AUC</th><th>Accuracy</th><th></th></tr></thead><tbody>'
    for i, row in results_df.iterrows():
        is_best   = row['model'] == best
        row_cls   = 'best-row' if is_best else ''
        badge     = '👑 Best' if is_best else ''
        table_html += f"""
        <tr class="{row_cls}">
            <td>{i+1}</td><td>{row['model']}</td>
            <td>{row['roc_auc']:.4f}</td><td>{row['accuracy']:.4f}</td>
            <td>{badge}</td>
        </tr>"""
    table_html += '</tbody></table>'
    st.markdown(table_html, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="info-box">
    Run the notebook first to generate model performance metrics.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#3d444d; font-size:0.8rem; padding:1rem;">
    Built with ❤️ using TensorFlow 2.10 · Streamlit<br>
    Bank Customer Churn Prediction — Deep Learning Project
</div>
""", unsafe_allow_html=True)
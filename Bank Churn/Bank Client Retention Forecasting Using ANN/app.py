import streamlit as st
import numpy as np
import pandas as pd
import joblib
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, Model
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Bank Churn Predictor",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank Customer Churn Predictor")
st.markdown("Predict whether a customer is likely to churn using 4 Deep Learning models.")

# Sidebar inputs
st.sidebar.header("Customer Details")

credit_score     = st.sidebar.slider("Credit Score", 300, 900, 650)
geography        = st.sidebar.selectbox("Geography", ["Tier 1", "Tier 2", "Tier 3"])
gender           = st.sidebar.selectbox("Gender", ["Male", "Female"])
age              = st.sidebar.slider("Age", 18, 92, 38)
tenure           = st.sidebar.slider("Tenure (years)", 0, 10, 5)
balance          = st.sidebar.number_input("Account Balance (₹)", 0.0, 300000.0, 80000.0, step=1000.0)
num_products     = st.sidebar.selectbox("Number of Products", [1, 2, 3, 4])
has_cr_card      = st.sidebar.selectbox("Has Credit Card?", ["Yes", "No"])
is_active_member = st.sidebar.selectbox("Is Active Member?", ["Yes", "No"])
estimated_salary = st.sidebar.number_input("Estimated Salary (₹)", 0.0, 300000.0, 100000.0, step=1000.0)

st.sidebar.header("Model Selection")
model_choice = st.sidebar.selectbox(
    "Choose Model",
    ["ANN (Baseline)", "TabNet", "FT-Transformer", "Autoencoder + Classifier", "Compare All Models"]
)

INPUT_DIM = 15

# builds the feature vector — same order as notebook preprocessing
def build_features(credit_score, geography, gender, age, tenure,
                   balance, num_products, has_cr_card, is_active_member, estimated_salary):

    gender_enc    = 1 if gender == "Male" else 0
    has_cc_enc    = 1 if has_cr_card == "Yes" else 0
    is_active_enc = 1 if is_active_member == "Yes" else 0

    # Tier 1 = France, Tier 2 = Germany, Tier 3 = Spain
    # honestly weird mapping but keeping consistent with notebook
    # TODO: change to actual country names later
    geo_france  = 1 if geography == "Tier 1" else 0
    geo_germany = 1 if geography == "Tier 2" else 0
    geo_spain   = 1 if geography == "Tier 3" else 0

    balance_salary_ratio = balance / (estimated_salary + 1)
    products_per_year    = num_products / (tenure + 1)
    active_balance       = is_active_enc * balance

    # st.write(raw_features)  # debug: uncomment to check feature vector

    return np.array([[
        credit_score, gender_enc, age, tenure, balance,
        num_products, has_cc_enc, is_active_enc, estimated_salary,
        geo_france, geo_germany, geo_spain,
        balance_salary_ratio, products_per_year, active_balance
    ]], dtype=np.float32)


# Model definitions (must match notebook exactly)

def build_ann(input_dim):
    inp = keras.Input(shape=(input_dim,))
    x = layers.Dense(128, activation='relu')(inp)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(64, activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(32, activation='relu')(x)
    out = layers.Dense(1, activation='sigmoid')(x)
    return Model(inp, out)


class TabNetClassifierKeras(keras.Model):
    def __init__(self, n_features, n_d=32, n_a=32, n_steps=5, gamma=1.3, momentum=0.02, **kwargs):
        super().__init__(**kwargs)
        self.n_steps = n_steps
        self.n_d     = n_d
        self.gamma   = gamma

        self.initial_bn  = layers.BatchNormalization(momentum=momentum)
        self.shared_fc   = layers.Dense((n_d + n_a) * 2, use_bias=False)
        self.step_fc_att = [layers.Dense((n_d + n_a) * 2, use_bias=False) for _ in range(n_steps)]
        self.step_bn_att = [layers.BatchNormalization(momentum=momentum) for _ in range(n_steps)]
        self.att_fc      = [layers.Dense(n_features, use_bias=False) for _ in range(n_steps)]
        self.att_bn      = [layers.BatchNormalization(momentum=momentum) for _ in range(n_steps)]
        self.step_fc     = [layers.Dense((n_d + n_a) * 2, use_bias=False) for _ in range(n_steps)]
        self.step_bn     = [layers.BatchNormalization(momentum=momentum) for _ in range(n_steps)]
        self.final_fc    = layers.Dense(1, activation='sigmoid')

    def call(self, x, training=False):
        B = tf.shape(x)[0]
        x = self.initial_bn(x, training=training)
        prior_scales  = tf.ones_like(x)
        complementary = tf.zeros([B, self.n_d])
        h_att         = tf.zeros([B, self.n_d + 32])

        for i in range(self.n_steps):
            a = self.step_fc_att[i](h_att)
            a = self.step_bn_att[i](a, training=training)
            a = self.att_fc[i](a)
            a = self.att_bn[i](a, training=training)
            a = a * prior_scales
            a = tf.nn.softmax(a, axis=-1)
            prior_scales  = prior_scales * (self.gamma - a)
            masked        = x * a
            h  = self.shared_fc(masked) + self.step_fc[i](masked)
            h  = self.step_bn[i](h, training=training)
            n_da = self.n_d + 32
            h  = h[:, :n_da] * tf.nn.sigmoid(h[:, n_da:])
            complementary = complementary + tf.nn.relu(h[:, :self.n_d])
            h_att = h

        return self.final_fc(complementary)


class FeatureTokenizer(layers.Layer):
    def __init__(self, n_features, d_model, **kwargs):
        super().__init__(**kwargs)
        self.W         = self.add_weight(shape=(n_features, d_model), initializer='glorot_uniform', name='W')
        self.b         = self.add_weight(shape=(n_features, d_model), initializer='zeros', name='b')
        self.cls_token = self.add_weight(shape=(1, 1, d_model), initializer='zeros', name='cls')

    def call(self, x):
        tokens = tf.einsum('bf,fd->bfd', x, self.W) + self.b
        cls    = tf.repeat(self.cls_token, tf.shape(x)[0], axis=0)
        return tf.concat([cls, tokens], axis=1)


def build_ft_transformer(n_features, d_model=64, n_heads=8, n_layers=3, dropout=0.1):
    inp = keras.Input(shape=(n_features,))
    x   = FeatureTokenizer(n_features, d_model)(inp)

    for _ in range(n_layers):
        # self-attention block
        res = x
        x   = layers.LayerNormalization()(x)
        x   = layers.MultiHeadAttention(num_heads=n_heads, key_dim=d_model // n_heads, dropout=dropout)(x, x)
        x   = layers.Dropout(dropout)(x)
        x   = x + res
        # feedforward block
        res = x
        x   = layers.LayerNormalization()(x)
        x   = layers.Dense(d_model * 4, activation='gelu')(x)
        x   = layers.Dropout(dropout)(x)
        x   = layers.Dense(d_model)(x)
        x   = layers.Dropout(dropout)(x)
        x   = x + res

    x   = layers.LayerNormalization()(x)
    out = layers.Dense(1, activation='sigmoid')(x[:, 0, :])  # CLS token
    return Model(inp, out)


def build_autoencoder(input_dim, encoding_dim=12):
    inp     = keras.Input(shape=(input_dim,))
    x       = layers.Dense(64, activation='relu')(inp)
    x       = layers.Dense(32, activation='relu')(x)
    encoded = layers.Dense(encoding_dim, activation='relu', name='bottleneck')(x)
    x       = layers.Dense(32, activation='relu')(encoded)
    x       = layers.Dense(64, activation='relu')(x)
    decoded = layers.Dense(input_dim, activation='linear')(x)
    return Model(inp, decoded), Model(inp, encoded)


@st.cache_resource
def load_models():
    ann     = build_ann(INPUT_DIM)
    tabnet  = TabNetClassifierKeras(n_features=INPUT_DIM)
    ft      = build_ft_transformer(INPUT_DIM)
    ae, enc = build_autoencoder(INPUT_DIM)
    # INPUT_DIM=15, +1 recon error, +12 latent = 28 total
    # took me a while to get this right lol
    clf     = build_ann(INPUT_DIM + 1 + 12)

    # dummy forward pass to init weights before loading
    dummy    = np.zeros((1, INPUT_DIM), dtype=np.float32)
    dummy_ae = np.zeros((1, INPUT_DIM + 1 + 12), dtype=np.float32)
    ann(dummy); tabnet(dummy); ft(dummy); ae(dummy); enc(dummy); clf(dummy_ae)

    for model, path in [
        (ann,    "ann_weights.h5"),
        (tabnet, "tabnet_weights.h5"),
        (ft,     "ft_weights.h5"),
        (ae,     "ae_weights.h5"),
        (clf,    "ae_clf_weights.h5"),
    ]:
        try:
            model.load_weights(path)
        except Exception:
            pass  # no saved weights yet — runs in demo mode

    return ann, tabnet, ft, ae, enc, clf


@st.cache_resource
def load_scaler():
    try:
        return joblib.load("scaler.pkl")
    except Exception:
        # scaler.pkl not found, returning unfitted scaler
        # predictions will be off without it, just for demo
        from sklearn.preprocessing import StandardScaler
        return StandardScaler()


ann_model, tabnet_model, ft_model, ae_model, enc_model, clf_model = load_models()
scaler = load_scaler()


def predict_single(model_name, X_raw):
    try:
        X = scaler.transform(X_raw).astype(np.float32)
    except Exception:
        X = X_raw.copy()

    if model_name == "ANN (Baseline)":
        return float(ann_model.predict(X, verbose=0).flatten()[0])

    elif model_name == "TabNet":
        return float(tabnet_model.predict(X, verbose=0).flatten()[0])

    elif model_name == "FT-Transformer":
        return float(ft_model.predict(X, verbose=0).flatten()[0])

    elif model_name == "Autoencoder + Classifier":
        recon = ae_model.predict(X, verbose=0)
        error = np.mean(np.abs(X - recon), axis=1, keepdims=True)
        embed = enc_model.predict(X, verbose=0)
        X_ae  = np.concatenate([X, error, embed], axis=1).astype(np.float32)
        return float(clf_model.predict(X_ae, verbose=0).flatten()[0])


def predict_all(X_raw):
    models = ["ANN (Baseline)", "TabNet", "FT-Transformer", "Autoencoder + Classifier"]
    return {m: predict_single(m, X_raw) for m in models}


raw_features = build_features(
    credit_score, geography, gender, age, tenure,
    balance, num_products, has_cr_card, is_active_member, estimated_salary
)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Customer Summary")
    summary = {
        "Credit Score":   credit_score,
        "Geography":      geography,
        "Gender":         gender,
        "Age":            age,
        "Tenure":         f"{tenure} yrs",
        "Balance":        f"₹{balance:,.0f}",
        "Products":       num_products,
        "Credit Card":    has_cr_card,
        "Active Member":  is_active_member,
        "Salary":         f"₹{estimated_salary:,.0f}",
    }
    st.table(pd.DataFrame(summary.items(), columns=["Feature", "Value"]))

with col2:
    st.subheader("Churn Prediction")

    if st.button("Predict Churn", use_container_width=True):

        if model_choice == "Compare All Models":
            results = predict_all(raw_features)
            avg     = np.mean(list(results.values()))

            st.markdown("### Model Comparison")
            for name, prob in results.items():
                label = "Churn Risk" if prob >= 0.5 else "Low Risk"
                st.metric(label=name, value=f"{prob*100:.1f}%", delta=label)

            st.info(f"Ensemble Average: {avg*100:.1f}% churn probability")

        else:
            prob = predict_single(model_choice, raw_features)

            st.metric(label=f"{model_choice} — Churn Probability", value=f"{prob*100:.1f}%")

            if prob >= 0.7:
                st.error("High Risk — Immediate retention action recommended.")
            elif prob >= 0.5:
                st.warning("Medium Risk — Monitor this customer closely.")
            elif prob >= 0.3:
                st.info("Low-Medium Risk — Worth a proactive check-in.")
            else:
                st.success("Low Risk — Customer appears stable.")

            st.progress(prob)

    st.caption("Note: Models run in demo mode until .h5 weight files are present in the same folder.")

st.markdown("---")
st.subheader("Feature Importance Guide")
# TODO: add SHAP values here for proper feature importance
# for now just using EDA observations
st.markdown("""
Based on EDA findings from the dataset:

| Feature | Impact |
|---|---|
| **Age** | High — Older customers churn more (avg 44.8 vs 37.4) |
| **Balance** | High — Higher balance customers churn more |
| **IsActiveMember** | High — Inactive members churn significantly more |
| **Geography (Tier 3)** | Medium — Tier 3 customers have disproportionately higher churn |
| **NumOfProducts** | Medium — Customers with 1 or 4 products churn more |
| **CreditScore** | Low — Barely differs between churners and non-churners |
| **Tenure** | Low — Weak standalone predictor |
""")
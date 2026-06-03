import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
import joblib

st.set_page_config(page_title="Stress Level Detector", page_icon="🧠")
st.title("🧠 Stress Level Detection from PPG Sensor Data")
st.markdown("Enter HRV features derived from PPG sensor to predict stress level.")

@st.cache_resource
def load_assets():
    model  = load_model("stress_ppg_cnn_model.h5", compile=False)
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_assets()

FEATURE_NAMES = [
    'MEAN_RR','MEDIAN_RR','SDRR','RMSSD','SDSD','SDRR_RMSSD','HR','pNN25','pNN50',
    'KURT','SKEW','MEAN_REL_RR','MEDIAN_REL_RR','SDRR_REL_RR','RMSSD_REL_RR',
    'SDSD_REL_RR','SDRR_RMSSD_REL_RR','KURT_REL_RR','SKEW_REL_RR',
    'VLF','VLF_PCT','LF','LF_PCT','LF_NU','HF','HF_PCT','HF_NU','TP','LF_HF','HF_LF',
    'SD1','SD2','sampen','higuci'
]

# Real rows from the dataset — model predicts each class with near 100% confidence
PRESETS = {
    "no_stress": [
        885.1578, 853.7637, 140.9727, 15.5545, 15.5534, 9.0631,
        69.5, 11.1333, 0.5333, -0.8566, 0.3352, -0.0002,
        -0.0002, 0.0171, 0.008, 0.008, 2.1433, -0.8566,
        0.3352, 2661.8941, 72.2033, 1009.2494, 27.3757, 98.4853,
        15.5226, 0.421, 1.5147, 3686.6662, 65.0181, 0.0154,
        11.0016, 199.0618, 2.1398, 1.1635
    ],
    "interruption": [
        939.4254, 948.3579, 81.3177, 12.9644, 12.9642, 6.2724,
        64.3631, 5.6, 0.0, -0.4082, -0.1553, -0.0001,
        0.0006, 0.014, 0.0048, 0.0048, 2.9309, -0.4082,
        -0.1553, 2314.2655, 76.9757, 690.1133, 22.9541, 99.6954,
        2.1085, 0.0701, 0.3046, 3006.4873, 327.2966, 0.0031,
        9.1701, 114.6345, 2.1745, 1.0847
    ],
    "time_pressure": [
        848.6209, 851.5731, 57.8863, 14.1427, 14.1425, 4.093,
        71.0401, 8.1333, 0.0, -0.3996, -0.1898, -0.0001,
        -0.0, 0.0168, 0.0104, 0.0104, 1.6271, -0.3996,
        -0.1898, 819.511, 53.9582, 653.7106, 43.0416, 93.4837,
        45.5667, 3.0002, 6.5163, 1518.7882, 14.3462, 0.0697,
        10.0036, 81.2501, 2.206, 1.2912
    ],
}


# --- Init session state with training means ---
if 'initialized' not in st.session_state:
    for i, name in enumerate(FEATURE_NAMES):
        st.session_state[f"f_{name}"] = float(scaler.mean_[i])
    st.session_state.initialized = True

# --- Preset buttons: write directly into session state keys ---
st.markdown("**Quick Presets** — load verified values for each stress class:")
cp1, cp2, cp3 = st.columns(3)
with cp1:
    if st.button("😊 No Stress Example"):
        for i, name in enumerate(FEATURE_NAMES):
            st.session_state[f"f_{name}"] = float(PRESETS["no_stress"][i])
        st.rerun()
with cp2:
    if st.button("😐 Interruption Example"):
        for i, name in enumerate(FEATURE_NAMES):
            st.session_state[f"f_{name}"] = float(PRESETS["interruption"][i])
        st.rerun()
with cp3:
    if st.button("😰 Time Pressure Example"):
        for i, name in enumerate(FEATURE_NAMES):
            st.session_state[f"f_{name}"] = float(PRESETS["time_pressure"][i])
        st.rerun()

# --- Feature inputs (key= ties widget to session state) ---
st.subheader("Enter HRV Features")

st.markdown("**Time Domain Features**")
c1, c2, c3 = st.columns(3)
with c1:
    MEAN_RR           = st.number_input("MEAN_RR",           key="f_MEAN_RR")
    SDRR              = st.number_input("SDRR",               key="f_SDRR")
    SDSD              = st.number_input("SDSD",               key="f_SDSD")
    HR                = st.number_input("HR",                 key="f_HR")
    pNN50             = st.number_input("pNN50",              key="f_pNN50")
    SKEW              = st.number_input("SKEW",               key="f_SKEW")
with c2:
    MEDIAN_RR         = st.number_input("MEDIAN_RR",         key="f_MEDIAN_RR")
    RMSSD             = st.number_input("RMSSD",             key="f_RMSSD")
    SDRR_RMSSD        = st.number_input("SDRR_RMSSD",        key="f_SDRR_RMSSD")
    pNN25             = st.number_input("pNN25",             key="f_pNN25")
    KURT              = st.number_input("KURT",              key="f_KURT")
    MEAN_REL_RR       = st.number_input("MEAN_REL_RR",       key="f_MEAN_REL_RR")
with c3:
    MEDIAN_REL_RR     = st.number_input("MEDIAN_REL_RR",     key="f_MEDIAN_REL_RR")
    SDRR_REL_RR       = st.number_input("SDRR_REL_RR",       key="f_SDRR_REL_RR")
    RMSSD_REL_RR      = st.number_input("RMSSD_REL_RR",      key="f_RMSSD_REL_RR")
    SDSD_REL_RR       = st.number_input("SDSD_REL_RR",       key="f_SDSD_REL_RR")
    SDRR_RMSSD_REL_RR = st.number_input("SDRR_RMSSD_REL_RR", key="f_SDRR_RMSSD_REL_RR")
    KURT_REL_RR       = st.number_input("KURT_REL_RR",       key="f_KURT_REL_RR")

SKEW_REL_RR = st.number_input("SKEW_REL_RR", key="f_SKEW_REL_RR")

st.markdown("**Frequency Domain Features**")
c4, c5 = st.columns(2)
with c4:
    VLF    = st.number_input("VLF",    key="f_VLF")
    LF     = st.number_input("LF",     key="f_LF")
    LF_NU  = st.number_input("LF_NU",  key="f_LF_NU")
    HF_PCT = st.number_input("HF_PCT", key="f_HF_PCT")
    TP     = st.number_input("TP",     key="f_TP")
with c5:
    VLF_PCT = st.number_input("VLF_PCT", key="f_VLF_PCT")
    LF_PCT  = st.number_input("LF_PCT",  key="f_LF_PCT")
    HF      = st.number_input("HF",      key="f_HF")
    HF_NU   = st.number_input("HF_NU",   key="f_HF_NU")
    LF_HF   = st.number_input("LF_HF",   key="f_LF_HF")

HF_LF = st.number_input("HF_LF", key="f_HF_LF")

st.markdown("**Non-linear Features**")
c6, c7 = st.columns(2)
with c6:
    SD1    = st.number_input("SD1",    key="f_SD1")
    sampen = st.number_input("sampen", key="f_sampen")
with c7:
    SD2    = st.number_input("SD2",    key="f_SD2")
    higuci = st.number_input("higuci", key="f_higuci")

# --- Predict ---
if st.button("Predict Stress Level", type="primary"):
    features = np.array([[
        MEAN_RR, MEDIAN_RR, SDRR, RMSSD, SDSD, SDRR_RMSSD, HR, pNN25, pNN50,
        KURT, SKEW, MEAN_REL_RR, MEDIAN_REL_RR, SDRR_REL_RR, RMSSD_REL_RR,
        SDSD_REL_RR, SDRR_RMSSD_REL_RR, KURT_REL_RR, SKEW_REL_RR,
        VLF, VLF_PCT, LF, LF_PCT, LF_NU, HF, HF_PCT, HF_NU, TP, LF_HF, HF_LF,
        SD1, SD2, sampen, higuci
    ]])

    scaled = scaler.transform(features)
    seq    = scaled.reshape(1, 34, 1)
    probs  = model.predict(seq, verbose=0)[0]
    pred   = int(np.argmax(probs))

    labels = {0: "😐 Interruption", 1: "😊 No Stress", 2: "😰 Time Pressure"}
    colors = {0: "orange",          1: "green",         2: "red"}

    st.markdown(f"### Prediction: **:{colors[pred]}[{labels[pred]}]**")
    st.markdown("**Confidence:**")
    for i, (label, prob) in enumerate(
        zip(["Interruption", "No Stress", "Time Pressure"], probs)
    ):
        st.progress(float(prob), text=f"{label}: {prob*100:.1f}%")

import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import joblib

st.set_page_config(page_title="Stress Level Detector", page_icon="🧠")

st.title("🧠 Stress Level Detection from PPG Sensor Data")
st.markdown("Enter HRV features derived from PPG sensor to predict stress level.")

# Load model
@st.cache_resource
def load_assets():
    model = load_model("stress_ppg_cnn_model.h5")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_assets()

# Feature input
st.subheader("Enter HRV Features")

# Time domain
st.markdown("**Time Domain Features**")
col1, col2, col3 = st.columns(3)
with col1:
    MEAN_RR      = st.number_input("MEAN_RR",      value=800.0)
    SDRR         = st.number_input("SDRR",          value=50.0)
    SDSD         = st.number_input("SDSD",          value=30.0)
    HR           = st.number_input("HR",            value=75.0)
    pNN50        = st.number_input("pNN50",         value=20.0)
    SKEW         = st.number_input("SKEW",          value=0.1)
with col2:
    MEDIAN_RR    = st.number_input("MEDIAN_RR",    value=795.0)
    RMSSD        = st.number_input("RMSSD",        value=40.0)
    SDRR_RMSSD   = st.number_input("SDRR_RMSSD",   value=1.2)
    pNN25        = st.number_input("pNN25",        value=35.0)
    KURT         = st.number_input("KURT",         value=3.0)
    MEAN_REL_RR  = st.number_input("MEAN_REL_RR",  value=1.0)
with col3:
    MEDIAN_REL_RR   = st.number_input("MEDIAN_REL_RR",   value=1.0)
    SDRR_REL_RR     = st.number_input("SDRR_REL_RR",     value=0.06)
    RMSSD_REL_RR    = st.number_input("RMSSD_REL_RR",    value=0.05)
    SDSD_REL_RR     = st.number_input("SDSD_REL_RR",     value=0.04)
    SDRR_RMSSD_REL_RR = st.number_input("SDRR_RMSSD_REL_RR", value=1.2)
    KURT_REL_RR     = st.number_input("KURT_REL_RR",     value=3.0)

SKEW_REL_RR = st.number_input("SKEW_REL_RR", value=0.1)

# Frequency domain
st.markdown("**Frequency Domain Features**")
col4, col5 = st.columns(2)
with col4:
    VLF    = st.number_input("VLF",    value=500.0)
    LF     = st.number_input("LF",     value=800.0)
    LF_NU  = st.number_input("LF_NU",  value=50.0)
    HF_PCT = st.number_input("HF_PCT", value=20.0)
    TP     = st.number_input("TP",     value=2000.0)
with col5:
    VLF_PCT = st.number_input("VLF_PCT", value=25.0)
    LF_PCT  = st.number_input("LF_PCT",  value=40.0)
    HF      = st.number_input("HF",      value=600.0)
    HF_NU   = st.number_input("HF_NU",   value=50.0)
    LF_HF   = st.number_input("LF_HF",   value=1.3)

HF_LF = st.number_input("HF_LF", value=0.77)

# Non-linear
st.markdown("**Non-linear Features**")
col6, col7 = st.columns(2)
with col6:
    SD1    = st.number_input("SD1",    value=28.0)
    sampen = st.number_input("sampen", value=1.5)
with col7:
    SD2    = st.number_input("SD2",    value=65.0)
    higuci = st.number_input("higuci", value=1.8)

# Predict
if st.button("Predict Stress Level", type="primary"):
    features = np.array([[
        MEAN_RR, MEDIAN_RR, SDRR, RMSSD, SDSD, SDRR_RMSSD, HR, pNN25, pNN50,
        KURT, SKEW, MEAN_REL_RR, MEDIAN_REL_RR, SDRR_REL_RR, RMSSD_REL_RR,
        SDSD_REL_RR, SDRR_RMSSD_REL_RR, KURT_REL_RR, SKEW_REL_RR,
        VLF, VLF_PCT, LF, LF_PCT, LF_NU, HF, HF_PCT, HF_NU, TP, LF_HF, HF_LF,
        SD1, SD2, sampen, higuci
    ]])

    features_scaled = scaler.transform(features)
    features_seq = features_scaled.reshape(1, 34, 1)

    probs = model.predict(features_seq)[0]
    pred = np.argmax(probs)
    labels = {0: "😐 Interruption", 1: "😊 No Stress", 2: "😰 Time Pressure"}
    colors = {0: "orange", 1: "green", 2: "red"}

    st.markdown(f"### Prediction: **:{colors[pred]}[{labels[pred]}]**")
    st.markdown("**Confidence:**")
    for i, (label, prob) in enumerate(zip(["Interruption", "No Stress", "Time Pressure"], probs)):
        st.progress(float(prob), text=f"{label}: {prob*100:.1f}%")

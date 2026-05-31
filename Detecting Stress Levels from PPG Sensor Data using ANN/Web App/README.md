# Web App — Stress Level Detection from PPG Sensor Data

## 🌐 Overview

A **Streamlit** web application that predicts stress levels in real-time based on Heart Rate Variability (HRV) features derived from PPG sensor data. The app uses the trained **1D-CNN** model (best performer with 99.99% accuracy).

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install streamlit tensorflow scikit-learn numpy pandas joblib
   ```

2. **Navigate to the Web App folder:**
   ```bash
   cd "Web App"
   ```

3. **Launch the app:**
   ```bash
   streamlit run web_app.py
   ```

4. Open your browser at `http://localhost:8501`

## 🖥️ App Features

- **34 HRV feature inputs** organized across three domains:
  - Time-domain (19 features): MEAN_RR, SDRR, RMSSD, HR, pNN25/50, KURT, SKEW, etc.
  - Frequency-domain (11 features): VLF, LF, HF, LF_HF, LF_NU, HF_NU, TP, etc.
  - Non-linear (4 features): SD1, SD2, sampen, higuci
- **One-click prediction** with the trained 1D-CNN model
- **Confidence scores** displayed as progress bars for all three stress classes:
  - 😊 No Stress
  - 😐 Interruption
  - 😰 Time Pressure

## 📦 Files Required

| File | Description |
|------|-------------|
| `web_app.py` | Main Streamlit application |
| `stress_ppg_cnn_model.h5` | Trained 1D-CNN model (TF/Keras) |
| `scaler.pkl` | Fitted StandardScaler for feature normalization |

## 📝 Notes

- The app loads the model and scaler with `@st.cache_resource` for efficiency
- Features are scaled and reshaped to `(1, 34, 1)` before inference (matching the 1D-CNN input shape)
- Default input values are set to typical resting-state HRV values for quick testing

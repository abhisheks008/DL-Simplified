import os
import joblib
import numpy as np
import streamlit as st

file_path = './Models/laptop_dataset.pkl'
model_path = './Models/XGBoost_regressor_model.pkl'
encoder_path = './Models/encoder.pkl'

if os.path.exists(file_path):
  with open(file_path, 'rb') as file:
    df = joblib.load(file)
else:
    st.error(f"File not found: {file_path}")
    
if os.path.exists(model_path):
  with open(model_path, 'rb') as file:
    model = joblib.load(file)
else:
  st.error(f"File not found: {model_path}")
  
if os.path.exists(encoder_path):
  with open(encoder_path, 'rb') as file:
    encoder = joblib.load(file)
else:
  st.error(f"File not found: {encoder_path}")

st.title("Laptop Price Predictor")

if 'df' in locals():
  st.header("Specifications")

  with st.form(key='specs_form'):
    st.subheader("Basic Information")
    company = st.selectbox("Select a brand", ["Select"] + list(df['Company'].unique()))
    if company == "Select":
      st.warning("Please select a laptop brand")

    type = st.selectbox("Select Laptop type", ["None"] + list(df['TypeName'].unique()))

    weight = st.number_input('Weight of the Laptop (in kgs)', step=0.1, value=1.4)

    st.subheader("RAM Size")
    ram = st.slider("Select RAM Size (in GB)", min_value=2, max_value=64, step=2, value=8)
    st.write(f"Default RAM Size: {ram} GB")
    
    st.subheader("Display Features")
    col1, col2 = st.columns(2)
    with col1:
      touchscreen = st.checkbox("Touchscreen")
    with col2:
      ips = st.checkbox("IPS")
    
    screen_size = st.number_input('Screen Size (in inches)', min_value=12.0, max_value=20.0, step=0.1, value=15.6)
    if screen_size <= 0:
      st.warning("Please enter a valid screen size")

    resolution = st.selectbox("Resolution", ["Select", '1920x1080', '1366x768', '1600x900', '3480x2160', '3200x1800', '2800x1800', '2560x1440', '2304x1440'])
    if resolution == "Select":
      st.warning("Please select the screen resolution")

    st.subheader("Performance")
    processor = st.selectbox("Select a processor", ["Select"] + list(df['Processor'].unique()))
    if processor == "Select":
      st.warning("Please select a processor")

    hdd = st.selectbox("HDD Size (in GB)", ["Select", 0, 128, 256, 512, 1024, 2048])
    if hdd == "Select":
      st.warning("Please select the HDD size")

    ssd = st.selectbox("SSD Size (in GB)", ["Select", 0, 8, 128, 256, 512, 1024])
    if ssd == "Select":
      st.warning("Please select the SSD size")

    gpu = st.selectbox("Select a GPU", ["No GPU"] + list(df['Gpu'].unique()))
    
    st.subheader("Software")
    os_laptop = st.selectbox("Select an OS", ["Select"] + list(df['OpSys'].unique()))
    if os_laptop == "Select":
      st.warning("Please select an OS")

    if st.form_submit_button(label='Predict Price'):
      if company != "Select" and type != "Select" and ram != "Select" and screen_size > 0 and resolution != "Select" and processor != "Select" and hdd != "Select" and ssd != "Select" and gpu != "Select" and os != "Select":
        # st.success()
        x=resolution.split('x')[0]
        y=resolution.split('x')[1]
        ppi=(int(x)**2+int(y)**2)**0.5/screen_size
        query=np.array([str(company), str(type), int(ram), str(gpu), str(os_laptop), float(weight), int(touchscreen), int(ips), float(ppi), processor, int(hdd), int(ssd)])
        query=encoder.transform([query])
        result=model.predict(query)
        result=np.exp(result)
        st.success(f"The estimated MRP of the laptop is {result[0]:.2f} INR")
        
      else:
        st.warning("Please fill in all required fields")
else:
  st.error("Data not available. Please check the file path and try again.")
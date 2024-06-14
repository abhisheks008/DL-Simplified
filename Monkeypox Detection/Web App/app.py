import streamlit as st
import time
import numpy as np
from utils import MODEL, INFORMATION
from PIL import Image

html_for_home = """
    <style>
        .header {
            background-color: transparent;
            text-align: center;
            text-decoration: underline;
            text-decoration-style: solid;
            text-underline-offset: 5px;
            text-decoration-thickness: 1px;
            text-decoration-color: green;
        }
    </style>
"""

def data_generator(data: str):
    data = data.split(' ')
    for word in data:
        yield word + " "
        time.sleep(0.09)

content = ['Description', 'Causes', 'Symptoms', 'Treatment']

def predict(img, content , name):
    img = np.array(img)
    img = np.expand_dims(img, axis=0)

    prediction = MODEL.predict([img])
    st.write("<div style='text-align: center;'>", unsafe_allow_html=True)
    if prediction[0][0] < 0.5:
        st.markdown(f"### Hey👋 {name} , No Monkey Pox Detected !!")
    else:
        st.markdown(f"### Hey👋 {name} , It's MonkeyPox 🦠 !!")
        for heading in content:
            st.markdown(f"### {heading}")
            st.write(data_generator(INFORMATION[heading]))

st.markdown("<h1 class='header'>🦠 Monkey Pox Detection 🦠</h1>", unsafe_allow_html=True)
st.html(html_for_home)

st.markdown("<h4>Enter your Name</h4>", unsafe_allow_html=True)
name = st.text_input("None", label_visibility="collapsed")

st.markdown("<h4>Select the image</h4>", unsafe_allow_html=True)
img = st.file_uploader("None", type=['png', 'jpeg', 'jpg', 'webp'], help='Select the image', label_visibility="collapsed", accept_multiple_files=False)

if 'run_button' in st.session_state and st.session_state.run_button:
    st.session_state.button_state = True
else:
    st.session_state.button_state = False

try:
    Img = Image.open(img)
    Img = Img.resize((224, 224))
    st.image(caption="Uploaded image", image=Img, width=100, use_column_width=True)
    if st.button(label="Submit", disabled=st.session_state.button_state , key = 'run_button'):
        st.divider()
        predict(Img, content , name)
        st.rerun()
except:
    pass

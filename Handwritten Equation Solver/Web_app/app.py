import streamlit as st      
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import cv2 
from predict import predict
import base64
st.set_page_config(page_title="Equation Solver", page_icon="logo.png",initial_sidebar_state="auto")

LOGO_IMAGE = "logo.png"

st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700;
        font-size:50px ;
        color: black ;
        margin-left:-15px;
        padding: 15px ;
    }
    .logo-img {
        float:right;
        width: 100px;
        height:100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}">
        <p class="logo-text">Equation Solver using CNN</p>
    </div>
    """,
    unsafe_allow_html=True
)
stroke_color = "black"
bg_color = "white"
drawing_mode = "freedraw"
realtime_update = True


with st.sidebar:
    stroke_width=st.slider(label="Adjust Stroke Width",value=5,min_value=3,max_value=10)

    st.markdown("<p style='text-align: center; font-size: 1.2em; color: white;'><a href='https://github.com/Sgvkamalakar/Hand-Written-Equation-Solver'>Source Code</a></p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em; color: white;'><a href='https://github.com/sgvkamalakar'>Explore my Codes</a></p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em; color: white;'><a href='https://www.linkedin.com/in/sgvkamlakar'>Connect with me on LinkedIn</a></p>", unsafe_allow_html=True)
data = st_canvas(
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=realtime_update,
    height=300,
    width=700,
    drawing_mode=drawing_mode,
    key="full_app",
)

if st.button('Predict'):
    path='temp/temp.png'
    cv2.imwrite(path, data.image_data)
    eq,res=predict(path)
    st.write(f"#### Equation: **{eq}**")
    x=str(res)
    res_length=len(x)
    width = 100
    font_size = 35
    if res_length > 3:
        width = 150
        font_size = 25

    padding_top = max(5, (40 - font_size) / 2)
    padding_bottom = max(5, (40 - font_size) / 2)
    style = f"background-color: grey; height: 70px; width: {width}px; border-radius: 5px; padding-top: {padding_top}px; padding-bottom: {padding_bottom}px; margin-left: 150px; text-align: center;"

    label_style = "font-weight: bold; color: white; font-size: {font_size}px;"

    label_style = label_style.format(font_size=font_size)

    st.subheader("Result")
    st.markdown(f"<div style='{style}'><label style='{label_style}'>{res}</label></div>", unsafe_allow_html=True)

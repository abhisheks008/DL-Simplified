import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import os
import tempfile

st.title("Alzheimer's Detection")

st.header("About Alzheimer's Disease")
st.write("""
Alzheimer's disease is a progressive neurologic disorder that causes the brain to shrink (atrophy) and brain cells to die. 
Alzheimer's disease is the most common cause of dementia — a continuous decline in thinking, behavioral and social skills 
that affects a person's ability to function independently. 
The disease is classified into different stages based on the severity of symptoms: Mild Demented, Moderate Demented, 
Non Demented, and Very Mild Demented.
""")

# Handle the path to the sample image using os library
script_dir = os.path.dirname(__file__)
rel_path = "../Images/image.jpg"
abs_file_path = os.path.join(script_dir, rel_path)
st.header("Sample Image")
try:
    image = Image.open(abs_file_path)
    st.image(image, caption='Sample Brain Scan Image')
except Exception as e:
    st.write(f"Error loading image: {e}")
# Handle the path to the uploaded image using os library
st.header("Upload Your MRI Scan")
scan = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if scan is not None:
    try:
        
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(scan.read())
            tmp_path = tmp_file.name

        img = Image.open(tmp_path)
        st.image(img, caption='Uploaded Brain Scan Image')
        
        os.remove(tmp_path)
    except Exception as e:
        st.write(f"Error processing uploaded image: {e}")


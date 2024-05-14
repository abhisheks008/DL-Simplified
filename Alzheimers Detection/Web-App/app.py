import streamlit as st
from PIL import Image
import numpy as np
import os
import tempfile
import tensorflow as tf

# Function to load the model
@st.cache_resource
def load_model():
    script_dir = os.path.dirname(__file__)  
    rel_path = 'model.h5'  
    abs_model_path = os.path.join(script_dir, rel_path)  
    model = tf.keras.models.load_model(abs_model_path)
    return model


model = load_model()

st.title("Alzheimer's Detection")

st.header("About Alzheimer's Disease")
st.write("""
Alzheimer's disease is a progressive neurologic disorder that causes the brain to shrink (atrophy) and brain cells to die. 
Alzheimer's disease is the most common cause of dementia — a continuous decline in thinking, behavioral and social skills 
that affects a person's ability to function independently. 
The disease is classified into different stages based on the severity of symptoms: Mild Demented, Moderate Demented, 
Non Demented, and Very Mild Demented.
""")

st.header("Sample Image")
script_dir = os.path.dirname(__file__)
rel_path = "../Images/image.jpg"
abs_file_path = os.path.join(script_dir, rel_path)
try:
    image = Image.open(abs_file_path)
    st.image(image, caption='Sample Brain Scan Image')
except Exception as e:
    st.write(f"Error loading image: {e}")

st.header("Upload Your MRI Scan")
scan = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

def preprocess_image(image, target_size):
    image = image.convert("RGB")
    image = image.resize(target_size)
    image_array = tf.keras.preprocessing.image.img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

if scan is not None:
    if st.button('Upload'):
        try:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(scan.read())
                tmp_path = tmp_file.name

            img = Image.open(tmp_path)
            st.image(img, caption='Uploaded Brain Scan Image')
            img_array = preprocess_image(img, target_size=(176, 176)) 
            predictions = model.predict(img_array)
            predicted_class = np.argmax(predictions, axis=1)
            class_labels = ['MildDemented', 'ModerateDemented', 'NonDemented', 'VeryMildDemented']
            result = class_labels[predicted_class[0]]
            st.markdown(f'<h3 style="color: red;">Prediction: {result}</h3>', unsafe_allow_html=True)

            os.remove(tmp_path)
        except Exception as e:
            st.write(f"Error processing uploaded image: {e}")

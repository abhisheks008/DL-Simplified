import streamlit as st
from PIL import Image

import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub # type: ignore

# Load the model
TF_MODEL_URL = 'https://tfhub.dev/google/on_device_vision/classifier/landmarks_classifier_asia_V1/1'
IMAGE_SHAPE = (321, 321)

classifier = tf.keras.Sequential([
    tf.keras.layers.InputLayer(shape=IMAGE_SHAPE+(3,)),
    tf.keras.layers.Lambda(lambda x: hub.KerasLayer(TF_MODEL_URL, output_key='predictions:logits')(x))
])

# Load the label map
LABEL_MAP_URL = 'https://www.gstatic.com/aihub/tfhub/labelmaps/landmarks_classifier_asia_V1_label_map.csv'
df = pd.read_csv(LABEL_MAP_URL)
label_map = dict(zip(df.id, df.name))

# Define the prediction function
def classify_image(image):
    img = np.array(image)/255.0
    img = img[np.newaxis, ...]
    prediction = classifier.predict(img)
    return label_map[np.argmax(prediction)]

# Streamlit app
st.title("Landmark Detection Web App")

uploaded_file = st.file_uploader("Choose an image...", type="jpeg")

if uploaded_file is not None:
    st.success("Image uploaded successfully!")
    image = Image.open(uploaded_file).resize(IMAGE_SHAPE)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    if st.button("Classify Image"):
        with st.spinner('Classifying...'):
            label = classify_image(image)
        st.success(f"Prediction: {label}")

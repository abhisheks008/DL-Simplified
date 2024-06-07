# This Streamlit GUI is used for the Deep Learning Model.

import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# # Load the trained model
model2 = tf.keras.models.load_model('path/to/your/trained/model')

# Load the tokenizer
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(['your', 'list', 'of', 'common', 'words'])

# Define the maximum sequence length (adjust based on your model)
max_length = 100

# Streamlit App
def main():
    st.title("SPAM vs HAM Email Classification")

    # User input
    user_input = st.text_area("Enter the email text:")

    if st.button("Predict"):
        # Tokenize and pad the input text
        input_sequence = tokenizer.texts_to_sequences([user_input])
        padded_input = pad_sequences(input_sequence, maxlen=max_length, padding='post', truncating='post')

        # Make the prediction
        prediction = model2.predict(padded_input)

        # Display the result
        if prediction[0][0] > 0.5:
            st.success("Prediction: HAM (Legitimate Email)")
        else:
            st.error("Prediction: SPAM")

if __name__ == '__main__':
    main()

import os
import tempfile

import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import tensorflow as tf

st.set_page_config(page_title="Music Genre Classifier", page_icon="🎵", layout="centered")

GENRES = ["blues", "classical", "country", "disco", "hiphop",
          "jazz", "metal", "pop", "reggae", "rock"]
SAMPLE_RATE = 22050
DURATION = 5
N_MELS = 128
HOP_LENGTH = 512


def extract_mel_spectrogram(file_path):
    y, sr = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)
    if len(y) < SAMPLE_RATE * DURATION:
        y = np.pad(y, (0, SAMPLE_RATE * DURATION - len(y)))
    mel = librosa.feature.melspectrogram(
        y=y, sr=SAMPLE_RATE, n_mels=N_MELS, hop_length=HOP_LENGTH
    )
    mel_db = librosa.power_to_db(mel, ref=np.max)
    return mel_db[..., np.newaxis]


@st.cache_resource
def load_model():
    model_path = os.path.join(os.path.dirname(__file__), "..", "Model", "music_genre_cnn.h5")
    try:
        return tf.keras.models.load_model(model_path)
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        return None


with st.sidebar:
    st.header("About")
    st.write(
        "This app classifies the genre of an uploaded audio clip "
        "using a CNN trained on mel-spectrogram representations of "
        "the GTZAN dataset (10 genres, 1000 tracks)."
    )
    st.subheader("Supported Genres")
    st.write(", ".join(g.capitalize() for g in GENRES))
    st.subheader("How It Works")
    st.write(
        "1. Upload a `.wav` file\n"
        "2. The first 5 seconds are converted to a mel-spectrogram\n"
        "3. A CNN predicts the genre from the spectrogram"
    )

st.title("🎵 Music Genre Classifier")
st.write("Upload a `.wav` audio clip and the model will predict its genre.")

model = load_model()

uploaded_file = st.file_uploader("Choose a WAV file", type=["wav"])

if uploaded_file is not None and model is not None:
    st.audio(uploaded_file, format="audio/wav")

    tmp_fd, tmp_path = tempfile.mkstemp(suffix=".wav")
    try:
        with os.fdopen(tmp_fd, "wb") as tmp:
            tmp.write(uploaded_file.getvalue())

        with st.spinner("Extracting mel-spectrogram..."):
            mel_db = extract_mel_spectrogram(tmp_path)

        st.subheader("Mel-Spectrogram")
        fig_spec, ax_spec = plt.subplots(figsize=(10, 3))
        img = librosa.display.specshow(
            mel_db[:, :, 0], sr=SAMPLE_RATE, hop_length=HOP_LENGTH,
            x_axis="time", y_axis="mel", ax=ax_spec, cmap="magma"
        )
        ax_spec.set_title("Mel-Spectrogram")
        plt.colorbar(img, ax=ax_spec, format="%+2.0f dB")
        plt.tight_layout()
        st.pyplot(fig_spec)
        plt.close(fig_spec)

        with st.spinner("Classifying genre..."):
            input_data = np.expand_dims(mel_db, axis=0)
            predictions = model.predict(input_data, verbose=0)[0]

        predicted_idx = int(np.argmax(predictions))
        predicted_genre = GENRES[predicted_idx].capitalize()
        confidence = float(predictions[predicted_idx]) * 100

        st.success(f"**Predicted Genre: {predicted_genre}** ({confidence:.1f}% confidence)")

        st.subheader("Prediction Probabilities")
        fig_bar, ax_bar = plt.subplots(figsize=(10, 4))
        colors = ["#4CAF50" if i == predicted_idx else "#2196F3" for i in range(len(GENRES))]
        ax_bar.barh([g.capitalize() for g in GENRES], predictions * 100, color=colors)
        ax_bar.set_xlabel("Confidence (%)")
        ax_bar.set_xlim(0, 100)
        plt.tight_layout()
        st.pyplot(fig_bar)
        plt.close(fig_bar)

    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

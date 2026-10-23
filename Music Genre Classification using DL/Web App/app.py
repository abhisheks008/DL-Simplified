"""
Streamlit app for Music Genre Classification.
Upload a .wav file to predict its genre using the trained CNN model.
"""

import streamlit as st
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import soundfile as sf
import json
import os

st.set_page_config(page_title="Music Genre Classifier", layout="wide")
st.title("Music Genre Classifier")
st.write("Upload a `.wav` file to predict its genre using our trained CNN model.")

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "Model", "genre_classifier.keras")
METADATA_PATH = os.path.join(os.path.dirname(__file__), "..", "Model", "model_metadata.json")

MAX_DURATION_SECONDS = 600


class SpecAugment(layers.Layer):
    """Custom Keras layer that applies frequency and time masking for data augmentation."""

    def __init__(self, freq_mask_param=10, time_mask_param=10, n_masks=2, **kwargs):
        super().__init__(**kwargs)
        self.freq_mask_param = freq_mask_param
        self.time_mask_param = time_mask_param
        self.n_masks = n_masks

    def call(self, inputs, training=None):
        """Apply random frequency and time masks to the input spectrogram during training."""
        if not training:
            return inputs
        x = inputs
        freq_dim = tf.shape(x)[1]
        time_dim = tf.shape(x)[2]
        freq_range = tf.range(freq_dim)
        time_range = tf.range(time_dim)
        for _ in range(self.n_masks):
            f = tf.random.uniform([], 1, self.freq_mask_param, dtype=tf.int32)
            f0 = tf.random.uniform([], 0, freq_dim - f, dtype=tf.int32)
            freq_mask = tf.cast(
                tf.logical_or(freq_range < f0, freq_range >= f0 + f), tf.float32
            )
            x = x * freq_mask[tf.newaxis, :, tf.newaxis, tf.newaxis]
            t = tf.random.uniform([], 1, self.time_mask_param, dtype=tf.int32)
            t0 = tf.random.uniform([], 0, time_dim - t, dtype=tf.int32)
            time_mask = tf.cast(
                tf.logical_or(time_range < t0, time_range >= t0 + t), tf.float32
            )
            x = x * time_mask[tf.newaxis, tf.newaxis, :, tf.newaxis]
        return x

    def get_config(self):
        """Return layer configuration for model serialization."""
        config = super().get_config()
        config.update({
            "freq_mask_param": self.freq_mask_param,
            "time_mask_param": self.time_mask_param,
            "n_masks": self.n_masks,
        })
        return config


@st.cache_resource
def load_model():
    """Load the trained Keras model and metadata JSON from disk."""
    model = keras.models.load_model(
        MODEL_PATH, custom_objects={"SpecAugment": SpecAugment}
    )
    with open(METADATA_PATH) as f:
        metadata = json.load(f)
    return model, metadata


try:
    model, metadata = load_model()
except Exception as e:
    st.error(f"Could not load model. Make sure `genre_classifier.keras` and `model_metadata.json` are in the Model/ folder.\n\nError: {e}")
    st.stop()

GENRES = metadata["genres"]
SR = metadata["sr"]
N_MELS = metadata["n_mels"]
HOP_LENGTH = metadata["hop_length"]
N_FFT = metadata["n_fft"]
SEGMENT_DURATION = metadata["segment_duration"]
SAMPLES_PER_SEGMENT = SR * SEGMENT_DURATION

uploaded_file = st.file_uploader("Choose a .wav file", type=["wav"])

if uploaded_file is not None:
    try:
        info = sf.info(uploaded_file)
        file_duration = info.duration
        if file_duration > MAX_DURATION_SECONDS:
            st.error(f"Audio too long ({file_duration:.0f}s). Maximum allowed duration is {MAX_DURATION_SECONDS}s.")
            st.stop()
    except sf.LibsndfileError:
        st.error("Invalid WAV file. Please upload a valid `.wav` audio file.")
        st.stop()

    uploaded_file.seek(0)
    st.audio(uploaded_file, format="audio/wav")

    with st.spinner("Analyzing audio..."):
        uploaded_file.seek(0)
        try:
            y, _ = librosa.load(uploaded_file, sr=SR)
        except Exception:
            st.error("Could not decode audio. The file may be corrupted or in an unsupported format.")
            st.stop()

        duration = len(y) / SR

        st.subheader("Mel-Spectrogram")
        fig_mel, ax_mel = plt.subplots(figsize=(10, 3))
        try:
            mel_full = librosa.feature.melspectrogram(y=y, sr=SR, n_mels=N_MELS, n_fft=N_FFT, hop_length=HOP_LENGTH)
            mel_full_db = librosa.power_to_db(mel_full, ref=np.max)
            librosa.display.specshow(mel_full_db, sr=SR, hop_length=HOP_LENGTH,
                                     x_axis="time", y_axis="mel", ax=ax_mel)
            ax_mel.set_title("Mel-Spectrogram")
            plt.colorbar(ax_mel.collections[0], ax=ax_mel, format="%+2.0f dB")
            plt.tight_layout()
            st.pyplot(fig_mel)
        finally:
            plt.close(fig_mel)

        num_segments = int(duration // SEGMENT_DURATION)
        if num_segments == 0:
            st.warning(f"Audio is too short ({duration:.1f}s). Need at least {SEGMENT_DURATION}s.")
            st.stop()

        segments = []
        for s in range(num_segments):
            start = s * SAMPLES_PER_SEGMENT
            end = start + SAMPLES_PER_SEGMENT
            segment = y[start:end]
            if len(segment) < SAMPLES_PER_SEGMENT:
                continue
            mel = librosa.feature.melspectrogram(
                y=segment, sr=SR, n_mels=N_MELS, n_fft=N_FFT, hop_length=HOP_LENGTH
            )
            mel_db = librosa.power_to_db(mel, ref=np.max)
            mean = mel_db.mean()
            std = mel_db.std()
            if std > 0:
                mel_db = (mel_db - mean) / std
            else:
                mel_db = mel_db - mean
            segments.append(mel_db)

        X = np.array(segments)[..., np.newaxis]
        pred_probs = model.predict(X, verbose=0)

        avg_probs = pred_probs.mean(axis=0)
        predicted_idx = np.argmax(avg_probs)
        predicted_genre = GENRES[predicted_idx]
        confidence = avg_probs[predicted_idx]

        st.subheader("Prediction")
        st.success(f"**Predicted Genre: {predicted_genre.upper()}** (Confidence: {confidence:.1%})")
        st.caption(f"Based on {len(segments)} segments of {SEGMENT_DURATION}s each")

        st.subheader("Confidence Scores")
        sorted_indices = np.argsort(avg_probs)[::-1]
        for i in sorted_indices:
            genre = GENRES[i]
            prob = avg_probs[i]
            st.progress(float(prob), text=f"{genre}: {prob:.1%}")

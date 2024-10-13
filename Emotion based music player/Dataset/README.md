<h2>Emotion Based Music Player</h2>

### Goal 🎯
The objective of the emotion-based music player project is to create an intelligent system that detects and analyzes users' emotions in real-time through techniques like facial recognition, voice analysis, or biosensors. Based on the detected emotional state, the player automatically curates and adjusts music playlists to enhance the user's mood and provide a personalized listening experience. The system aims to reduce the burden of manual song selection, adapt to emotional changes dynamically, and offer privacy-conscious and culturally relevant music suggestions, while giving users the flexibility to override or customize the music based on their preferences.

### Model(s) used for the Web App 🧮

The models and technologies used in the emotion-based music player project include:

1. Pretrained Keras Model (model.h5): A deep learning model, likely a Convolutional Neural Network (CNN), is loaded to predict emotions based on processed facial landmarks and hand movements.

2. Mediapipe Library: Mediapipe is used for extracting facial landmarks and hand landmarks, which serve as input features for emotion recognition. It captures key points from the user's face and hands for emotion detection.

3. Streamlit and WebRTC: Used for the web interface and real-time video streaming, capturing the users face for emotion recognition through a web camera.

4. The project leverages deep learning (Keras) and computer vision (Mediapipe) to detect emotions based on facial and hand landmark data, then uses the model to predict the emotion, which influences the music recommendation. ​


# Signify - American Sign Language Detection

Welcome to Signify, an American Sign Language (ASL) detection application powered by Flask and TensorFlow. This application allows users to upload images containing ASL hand signs and predicts the corresponding sign using a pre-trained deep learning model.

## Demo
To see how Signify works, check out the demo video

https://github.com/Adhivp/DL-Simplified/assets/92261845/aef089f7-19f2-410b-89de-ed5528511f47

## Getting Started

These instructions will guide you through setting up and running the Signify Flask application on your local machine.


### Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/abhisheks008/DL-Simplified
```
2. Move to this folder and install requirements

```bash
cd "American Sign Language Detection"
pip install -r requirements.txt
```
3. Move to web app
```bash
cd "Web app"
```
4. Set the path to your pre-trained model:

    Open the `app.py` file and locate the `model_path` variable. Replace `Desktop/DL-Simplified/American Sign Language Detection/models/hand_sign_recognition_inceptionV3.h5` with the path to your pre-trained model.

5. Run the Flask application:

```bash
python app.py
```
## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.


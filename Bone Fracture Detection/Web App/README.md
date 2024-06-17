# Bone Fracture Detection Web Application 💻

## Overview  🔍

This web application is designed to facilitate bone fracture detection using machine learning models. It provides an easy-to-use interface for users to upload X-ray images along with their name, and receive predictions on whether the image contains a bone fracture or not. Additionally, the application draws bounding boxes around detected fractures and provides information about the type of fracture detected. The application is built using Flask, a lightweight WSGI web application framework.

## Features 

- **Upload X-ray Images**: Users can upload X-ray images of bone scans along with their name directly through the web interface.
- **Fracture Detection**: The uploaded images are processed using pre-trained machine learning models to detect fractures.
- **Bounding Box Visualization**: Detected fractures are highlighted with bounding boxes overlaid on the original X-ray image.
- **Fracture Type Information**: Users receive information about the type of fracture detected (e.g., transverse, oblique, comminuted).
- **User-Friendly Interface**: The web application features a simple and intuitive user interface for seamless interaction.

## Installation

To run the application locally, follow these steps:

1. Clone this repository to your local machine.
   ```
   git clone https://github.com/abhisheks008/DL-Simplified.git
   ```
2. Navigate to the project directory.
   ```
   cd DL-Simplified/Bone\ Fracture\ Detection/Web App
   ```
3. Install the required dependencies.
   ```
   pip install -r requirements.txt
   ```
4. Run the Flask application.
   ```
   python3 app.py
   ```
5. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Open the web application in your browser.
2. Enter your name in the designated field.
3. Click on the "Choose File" button to upload an X-ray image and upload it.
5. Wait for the prediction result to appear on the screen, including the bounding box around detected fractures and information about the fracture type.
6. Return back to upload additional images or repeat the process as needed.

## Sample Usage 
[![Watch the video](https://img.youtube.com/vi/YNMzmSki_Xg/0.jpg)](https://www.youtube.com/watch?v=YNMzmSki_Xg)

## Model Details

The bone fracture detection models used in this application are trained on a dataset of X-ray images labeled with fracture and non-fracture classes. The models are implemented using deep learning techniques and are capable of accurately identifying fractures in bone scans.

## Contributors

`Bingumalla Likith |
GSSoC 24 Contributor|
Issue Number #650`

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/bingumalla-likith-2633392b9)  [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/binguliki)

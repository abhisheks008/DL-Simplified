from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
from keras.models import load_model

app = Flask(__name__)

# Define the folder to store uploaded videos
UPLOAD_FOLDER = '../Images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the Siamese model
# model_path = "/kaggle/working/siamese_model.h5"  # Specify the path where you saved the model
# model_path = r'C:\Users\Pabitra kumar\OneDrive\Desktop\Anti Spoofing\siamese_flask_app\model\siamese_model.py'  # Specify the path where you saved the model
# siamese_model = load_model(model_path)

# Function to preprocess a video frame
def preprocess_frame(frame):
    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0  # Normalize pixel values to the range [0, 1]
    frame = np.expand_dims(frame, axis=0)  # Add batch dimension
    return frame

# Function to predict the class of a pair of video frames
def predict_class(frame1, frame2):
    # Predict the class
    # pred = siamese_model.predict([frame1, frame2])
    # pred_class = np.argmax(pred)
    pred_class=0

    # Get the predicted class label
    if pred_class == 0:
        return "Genuine"
    else:
        return "Spoof"

# Route to upload a video file
@app.route('/upload', methods=['POST'])
def upload_file(): 
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})

        file = request.files['file']
        # If user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            return jsonify({'error': 'No selected file'})

        # Save the uploaded video file
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return jsonify({'message': 'File uploaded successfully', 'file_path': file_path})

# Route to process and classify the uploaded video
@app.route('/process', methods=['POST'])
def process_video():
    if request.method == 'POST':
        # Get the uploaded video file path
        file_path = request.form.get('file_path')
        print(file_path)
        # Load the video using OpenCV
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            return jsonify({'error': 'Error loading video'})

        # Read the first two frames
        ret1, frame1 = cap.read()
        ret2, frame2 = cap.read()

        # Preprocess the frames
        frame1 = preprocess_frame(frame1)
        frame2 = preprocess_frame(frame2)

        # Predict the class of the video frames
        predicted_label = predict_class(frame1, frame2)

        # Release the video capture object
        cap.release()

        return jsonify({'message': 'Video processed successfully', 'predicted_label': predicted_label})

# Main route to render the upload form
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)





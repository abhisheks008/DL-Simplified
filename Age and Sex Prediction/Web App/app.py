from flask import Flask, render_template, request, redirect, url_for, session
import os
import numpy as np
import cv2
import tensorflow as tf
import sys
import logging

sys.stdout.reconfigure(encoding='utf-8')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = os.urandom(24)

UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# loading the model
# model is saved in static folder
# Load the model
try:
    model = tf.keras.models.load_model('static/age_and_gender_prediction_model.h5')
    logging.info("Model loaded successfully.")
except Exception as e:
    logging.error("Error loading model: %s", e)
    model = None

# gender mapping
# if gender prediction = 0, the predition is MALE
# else FEMAL
gender_dict = {0: 'Male', 1: 'Female'}

# Function to extract face from uploaded image
# The dataset on which model was trained contained only face images
# This function finds the face area using
# a haar cascade designed by OpenCV to detect the frontal face
def extract_face():
    try:
        img = cv2.imread('static/uploaded_img.jpg') # reading uploaded image
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converted to grayscale
        
        # OpenCV's CascadeClassifier to load a pre-trained Haar cascade for detecting frontal faces
        haar_cascade = cv2.CascadeClassifier('static/haarcascade_frontalface_default.xml')
        faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=9)
        extracted_faces = []

        if len(faces_rect) == 0:
            cv2.imwrite('static/extracted.jpg', img) # if no coordinates are detected, its only face image
        else:
            extracted_faces = []
            for (x, y, w, h) in faces_rect:
                face = img[y:y+h, x:x+w]
                extracted_faces.append(face)
            concatenated_faces = cv2.hconcat(extracted_faces)
            cv2.imwrite('static/extracted.jpg', concatenated_faces) # face extracted image - saved as extracted.jpg

        if len(faces_rect) != 0:
            for (x, y, w, h) in faces_rect:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
            cv2.imwrite('static/uploaded_img.jpg', img) # original uploaded image where face is marked
    except Exception as e:
        logging.error("Error occured while extracting face",e)

# Function to extract features from the image
# This is the pre-process technique
# which was applied on original dataset before training
def extract_features(images):
    try:
        img = cv2.imread(images, cv2.IMREAD_GRAYSCALE)  # Read image in grayscale
        img = cv2.resize(img, (128, 128))  # Resize image
        img = np.array(img)  # Convert image to numpy array
        features = img.reshape(1, 128, 128, 1)  # Reshape to match input shape
        return features
    except Exception as e:
        logging.error("error occured during extracting feature",e)

# Function to predict gender and age
def predict_result():
    X = extract_features('static/extracted.jpg')
    X = X/255.0
    pred = model.predict(X.reshape(1, 128, 128, 1))
    pred_gender = gender_dict[round(pred[0][0][0])]
    pred_age = round(pred[1][0][0])
    return pred_gender, pred_age

@app.route('/prediction')
def prediction():
    image_filename = 'static/extracted.jpg'
    gender, age = predict_result()
    if image_filename:
        return render_template('prediction_page.html', age=age, gender=gender)
    else:
        return render_template('not_found.html')  # Redirect to the 'not_found' page

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and 'face_image' in request.files:
        face_image = request.files['face_image']
        if face_image.filename != '':
            image_filename = 'uploaded_img.jpg'
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
            face_image.save(image_path)
            session['image_filename'] = image_filename
            extract_face()
            return redirect(url_for('prediction'))  # Redirect to the 'prediction' route
    return render_template('index.html')

@app.route('/not_found')
def not_found():
    return render_template('not_found.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)

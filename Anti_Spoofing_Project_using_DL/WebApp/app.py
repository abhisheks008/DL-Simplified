# from flask import Flask, render_template, request
# from werkzeug.utils import secure_filename
# import os
# import cv2
# import numpy as np
# from keras.models import load_model  

# app = Flask(__name__)

# # Define the folder to store uploaded videos
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_FOLDER = os.path.join(BASE_DIR, 'Uploads')
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Load the Siamese model
# # model_path = os.path.join(BASE_DIR, 'model', 'siamese_model.h5')  # Specify the correct path
# # siamese_model = load_model(model_path)  # Uncomment when model is available

# # Function to preprocess a video frame
# def preprocess_frame(frame): # working fine
#     frame = cv2.resize(frame, (224, 224))
#     frame = frame / 255.0  # Normalize pixel values to the range [0, 1]
#     frame = np.expand_dims(frame, axis=0)  # Add batch dimension
#     return frame

# # Function to predict the class of a pair of video frames
# def predict_class(frame1, frame2):
#     # Predict the class
#     # pred = siamese_model.predict([frame1, frame2]) 
#     # pred_class = np.argmax(pred)  # Uncomment when model is available
#     pred_class = 1 

#     # Get the predicted class label
#     if pred_class == 0:
#         return "Genuine"
#     else:
#         return "Spoof"

# # Route to upload a video file
# @app.route('/upload', methods=['POST'])
# def upload_file():
   
#     if 'file' not in request.files:
#         return render_template('index.html', error='No file part')

#     file = request.files['file']
#     if file.filename == '':
#         return render_template('index.html', error='No selected file')

#     filename = secure_filename(file.filename)
#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#     try:
#         file.save(file_path)
#         return render_template('upload.html', message='File uploaded successfully',file_path='file_path')
#     except Exception as e:
#         return render_template('index.html', error=str(e))

# # Route to process and classify the uploaded video
# @app.route('/process', methods=['GET'])
# def process_video():
#     print("video processing started")
#     file_path = request.form.get('file_path')
#     # file_path = r'C:\Users\Pabitra kumar\OneDrive\Documents\GitHub\DL-Simplified\Anti Spoofing Project using DL\WebApp\Uploads\0001e96803--62457bc94ff454214e8af551__Infinix_note_11.mp4'
#     if not file_path or not os.path.exists(file_path):
#         print(file_path)
#         print("file path error") 
#         return render_template('index.html', error='Invalid file path')

#     cap = cv2.VideoCapture(file_path)
#     if not cap.isOpened():
#        return render_template('index.html', error='Error loading video')

#     ret1, frame1 = cap.read()
#     ret2, frame2 = cap.read()
#     if not ret1 or not ret2:
#         # print("two")
#         cap.release()
#         return render_template('index.html', error='Error reading video frames')

#     frame1 = preprocess_frame(frame1)
#     frame2 = preprocess_frame(frame2)

#     predicted_label = predict_class(frame1, frame2)
#     # predicted_label= "sooof"
#     cap.release()
#     # print("three")
#     return render_template('process.html', message='Video processed successfully', predicted_label=predicted_label)

# # Main route to render the upload form
# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model 

app = Flask(__name__)

# Define the folder to store uploaded videos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'Uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#converting jupyter file into .h5 format compatable with keras
# Load the model
# model = load_model('anti_spoofing_project_using_dl.ipynb')

# # Save the model in HDF5 format
# model.save('anti_spoofing_project_using_dl.h5')

# Load the Siamese model
# model_path = os.path.join(BASE_DIR, 'model', 'anti_spoofing_project_using_dl.h5')  # Specify the correct path
# model_path = r"C:\Users\Pabitra kumar\OneDrive\Documents\GitHub\DL-Simplified\Anti Spoofing Project using DL\Model\siamese_model.h5"
# siamese_model = load_model(model_path)  


# # Function to preprocess a video frame
def preprocess_frame(frame): # working fine
    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0  # Normalize pixel values to the range [0, 1]
    frame = np.expand_dims(frame, axis=0)  # Add batch dimension
    return frame

# Function to predict the class of a pair of video frames
def predict_class(frame1, frame2):
    # Predict the class
    # pred = siamese_model.predict([frame1, frame2]) 
    # pred_class = np.argmax(pred) 
    pred_class = 1 

    # Get the predicted class label
    if pred_class == 0:
        return "Genuine"
    else:
        return "Spoof"

# Route to upload a video file
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', error='No selected file')

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    try:
        file.save(file_path)
        return redirect(url_for('process_video', file_path=file_path))
    except Exception as e:
        return render_template('index.html', error=str(e))

# Route to process and classify the uploaded video
@app.route('/process', methods=['GET'])
def process_video():
    print("video processing started")
    file_path = request.args.get('file_path')
    if not file_path or not os.path.exists(file_path):
        print("file path error:", file_path)
        return render_template('index.html', error='Invalid file path')

    
    cap = cv2.VideoCapture(file_path)
    if not cap.isOpened():
       return render_template('index.html', error='Error loading video')

    ret1, frame1 = cap.read()
    ret2, frame2 = cap.read()
    if not ret1 or not ret2:
        # print("two")
        cap.release()
        return render_template('index.html', error='Error reading video frames')

    frame1 = preprocess_frame(frame1)
    frame2 = preprocess_frame(frame2)

    predicted_label = predict_class(frame1, frame2)
    # predicted_label= "sooof"
    cap.release()
    # print("three")
    return render_template('process.html', message='Video processed successfully', predicted_label=predicted_label)

    # return render_template('process.html', message='Video processed successfully')

# Main route to render the upload form
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

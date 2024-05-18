from flask import Flask, request, render_template, url_for
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

#Enter your proper path to the output of the model
model_path = 'DL-Simplified/American Sign Language Detection/models/hand_sign_recognition_inceptionV3.h5'
print(f"Loading model from: {model_path}")
model = tf.keras.models.load_model(model_path)
print("Model loaded successfully.")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def prepare_image(image):
    print("Original image mode:", image.mode)
    image = image.convert('RGB')
    print("Converted image mode:", image.mode)
    image = image.resize((228, 228))
    print("Image size after resizing:", image.size)
    image = np.array(image) / 255.0
    print("Image array shape after normalization:", image.shape)
    image = np.expand_dims(image, axis=0)
    print("Image array shape after expanding dimensions:", image.shape)
    return image

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    prediction = None
    error = None
    file_url = None

    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('main.html', error='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('main.html', error='No selected file')
        if file and allowed_file(file.filename):
            try:
                image = Image.open(io.BytesIO(file.read()))
                processed_image = prepare_image(image)
                prediction = model.predict(processed_image)
                print("Model prediction:", prediction)
                predicted_class = np.argmax(prediction, axis=1)[0]
                print("Predicted class:", predicted_class)
                
                if predicted_class == 11:
                    prediction= "The model couldn't predict properly. Please upload a different image."
                else:
                    prediction = f"Predicted Class: {predicted_class}"
                
                # Save the file to static/uploads
                filename = file.filename
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.seek(0)  # Go back to the start of the file
                file.save(file_path)
    

                # Delete the file after use
                if os.path.exists(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_path}")
            except Exception as e:
                error = str(e) 

    return render_template('main.html', prediction=prediction, error=error)

if __name__ == '__main__':
    app.run(debug=True)

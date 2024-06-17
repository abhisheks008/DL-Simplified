from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Enter your proper path to the output of the model
model_path = "/Users/adhivp/Desktop/Web app/American_Sign_Language_MobileNetV3Large.h5"
print(f"Loading model from: {model_path}")
model = tf.keras.models.load_model(model_path)
print("Model loaded successfully.")
CONFIDENCE_THRESHOLD = 0.7

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def prepare_image(image):
    print("Original image mode:", image.mode)
    image = image.convert('RGB')
    print("Converted image mode:", image.mode)
    image = image.resize((224,224))
    print("Image size after resizing:", image.size)
    image = np.expand_dims(image, axis=0)
    print("Image array shape after expanding dimensions:", image.shape)
    return image

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    prediction = None
    error = None
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
                
                max_confidence = np.max(prediction)
                print(max_confidence)
                if max_confidence < CONFIDENCE_THRESHOLD:
                    prediction = ""
                    error = "Model is not confident enough to make a prediction."
                else:
                    predicted_class_index = np.argmax(prediction, axis=1)[0]
                    print("Predicted class index:", predicted_class_index)
                    
                    labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Nothing', 'O', 'P', 'Q', 'R', 'S', 'Space', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                    predicted_label = labels[predicted_class_index]
                    prediction = f"Predicted Class: {predicted_label}"
                
                filename = file.filename
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
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
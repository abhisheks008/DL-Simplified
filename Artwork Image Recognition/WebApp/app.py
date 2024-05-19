import tensorflow as tf
from tensorflow.keras.preprocessing import image
import markdown2
import numpy as np
from werkzeug.utils import secure_filename
import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
api_key = "AIzaSyCQ5FJ29LRieGENvedg_UeQpQNXwcWx5Kk"
genai.configure(api_key=api_key)
app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads')
 
app.config['UPLOAD'] = upload_folder

classes = ['Abstract art',
 'Abstract expressionism paintings',
 'Academic art',
 'Art Nouveau paintings',
 'Art deco paintings',
 'Baroque paintings',
 'Constructivism art',
 'Contemporary art',
 'Cubism art',
 'Dadaism artwork',
 'Digital art',
 'Expressionism paintings',
 'Fauvism paintings',
 'Gothic art',
 'Impressionism artwork',
 'Mannerism paintings',
 'Minimalism art',
 'Modernism artwork',
 'Naive art',
 'Neo-expressionism art',
 'Neoclassical art',
 'Pop art',
 'Post-impressionism artwork',
 'Pre-Raphaelite paintings',
 'Realism paintings',
 'Renaissance paintings',
 'Romanticism paintings',
 'Surrealism artwork',
 'Surrealist paintings',
 'Symbolism artwork']
def preprocess_image(filename):
    img_ = image.load_img(filename, target_size=(228, 228))
    img_array = image.img_to_array(img_)
    img_processed = np.expand_dims(img_array, axis=0)
    img_processed /= 255
    return img_processed

def predict_image(filename, model):
    img_processed = preprocess_image(filename)
    prediction = model.predict(img_processed)
    index = np.argmax(prediction)
    return str(classes[index]).title()

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        ans = predict_image(filename=img, model=model)
        print(ans)
        model_Genai = genai.GenerativeModel("gemini-pro")

        try:
            response = model_Genai.generate_content(ans)
            response = markdown2.markdown(response.text)
        except:
            response = "No Information"
        print(response)
        return render_template('index.html', ans=ans, img=img, res = response)
    return render_template('index.html')

if __name__ == '__main__':
    model = tf.keras.models.load_model('model.h5')
    app.run(debug=True)
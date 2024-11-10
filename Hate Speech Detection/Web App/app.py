# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 08:39:20 2023

@author: Jens Bender
"""

from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import tensorflow as tf
import tensorflow_text  # prerequisite for using the BERT preprocessing layer
import numpy as np
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create the Flask web application
app = Flask(__name__)

# Set a secret key (stored in .env) as a security measure (e.g. protecting against CSRF attacks) 
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Load the TensorFlow model
model = tf.keras.models.load_model("saved_models/model3")


# Create hate speech detection form class (that inherits from the Flask WTForm class)
class HateSpeechForm(FlaskForm):
    comment = StringField("Social Media Comment", validators=[DataRequired()])
    submit = SubmitField("Run")


# Home route 
@app.route("/", methods=["GET", "POST"])
def home():
    # Instantiate a hate speech form class object
    form = HateSpeechForm()
    # If the user submitted valid information in the hate speech form
    if form.validate_on_submit():
        # Get the input text from the form
        input_text = form.comment.data
        # Convert input text to a list
        input_data = [input_text]
        # Make prediction using the TensorFlow model
        prediction_prob = model.predict(input_data)[0][0]
        # Convert prediction probability to percent
        prediction_prob = np.round(prediction_prob * 100, 1)
        # Convert prediction probability to prediction in text form
        if prediction_prob >= 50:
            prediction = "Hate Speech"
        else:
            prediction = "No Hate Speech"
            # Invert the prediction probability
            prediction_prob = 100 - prediction_prob
        # Render the prediction and prediction probability in the index.html template
        return render_template("index.html", 
                               form=form, 
                               prediction=prediction, 
                               prediction_prob=prediction_prob)
    return render_template("index.html", form=form)


# API route
@app.route("/api")
def prediction_by_api():
    # Get the input text from the api query parameter
    input_text = request.args.get("comment")
    # Convert input text to a list
    input_data = [input_text]
    # Make prediction using the TensorFlow model
    prediction_prob = model.predict(input_data)[0][0]
    # Convert prediction probability to prediction in text form
    if prediction_prob >= 0.5:
        prediction = "Hate Speech"
    else:
        prediction = "No Hate Speech"
        # Invert the prediction probability
        prediction_prob = 1 - prediction_prob
    # Return json with the prediction and prediction probability
    return jsonify({"prediction": prediction,
                    "probability": float(prediction_prob)})


# Start the Flask web application
if __name__ == "__main__":
    app.run(debug=True)

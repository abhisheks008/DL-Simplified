# Diabetes Predictor App

This repository contains code for a Diabetes Detection App built using Jupyter notebooks, trained models, and a Streamlit web application.

## Overview
Diabetes Detection App is a web application that predicts the likelihood of an individual having diabetes based on various health parameters such as glucose level, blood pressure, BMI, and more. It utilizes machine learning models trained on a dataset of diabetes patients.

## Contents
- `Notebook/`: Jupyter notebooks containing data exploration, preprocessing, model training, and evaluation.
- `Models/`: Trained Deep Learning models saved in HDF5 format.
- `Dataset/`: Contains `.csv` file used for training the deep learning models.
- `app.py`: Source code for the Streamlit web application.

## Usage
1. **Clone the Repository**: Clone this repository to your local machine using the following command:

    ```bash
    git clone https://github.com/
    ```

2. **Exploring Notebooks**: Navigate to the Notebooks/ directory to explore Jupyter notebooks. These notebooks cover data analysis, preprocessing, model training, and evaluation steps.

3. **Trained Models**: The Models/ directory contains trained Deep Learning models saved in HDF5 format. These models can be loaded and used for making predictions.

4. **Streamlit App:** The app.py contains the source code for the Streamlit web application. To run the app locally, follow the instructions below:

    ```bash
    pip install -r requirements.txt
    streamlit run app.py
    ```

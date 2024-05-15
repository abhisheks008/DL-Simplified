# Diabetes Predictor App

This repository contains code for a Diabetes Prediction App built using Deep Learning and a Streamlit web application.

## Overview
Diabetes Detection App is a web application that predicts the likelihood of an individual having diabetes based on various health parameters such as glucose level, blood pressure, BMI, and more. It utilizes Deep Learning models like ANN, LSTM and RNN trained on a dataset of diabetes patients.

## Repo Structure:

```
Diabetes Prediction
|- Dataset
  |- diabetes.csv
  |- README.md
|- Images
  |- img1.png
  |- img2.png
       :
       :
  |- img11.png
  |- README.md
|- Models
  |- Diabetes Predictor.ipynb
  |- ann_model.h5
  |- lstm_model.h5
  |- rnn_model.h5
  |- README.md
|- Web App
  |- app.py
  |- snapshot.png
  |- Demo.mp4
  |- README.md
|- requirements.txt
```

## Contents
- `Dataset/`: Contains `.csv` file used for training the deep learning models.
- `Images/`: Contains snapshots data visualization plots and Streamlit application.
- `Models/`: Trained Deep Learning models saved in HDF5 format.
- `Web App/`: Source code for the Streamlit web application.

## Usage

1. **Exploring Notebooks**: Navigate to the `Models/` directory to explore Jupyter notebooks. These notebooks cover data analysis, preprocessing, model training, and evaluation steps.
   -  Navigate to the `Models/Diabetes Prediction.ipynb`
   -  Run all the cells
2. **Trained Models**: The `Models/` directory contains trained Deep Learning models saved in HDF5 format. These models can be loaded and used for making predictions.
3. **Streamlit App:** The `Web App/app.py` contains the source code for the Streamlit web application. To run the app locally, follow the instructions below:

    ```bash
    pip install -r requirements.txt
    cd Web App
    streamlit run app.py
    ```

## Contributor:
<p align="center">
  <img src="https://github.com/sgvkamalakar.png" height="200" width="200"/>
</p>
<p align="center">
  Kamalakar Satapathi
</p>

 
Connect with me on [![LinkedIn](https://img.shields.io/badge/-Kamalakar_Satapathi-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sgvkamalakar)

Explore my magical codes [![GitHub](https://img.shields.io/badge/-Sgvkamalakar-181717?style=flat-square&logo=github)](https://github.com/sgvkamalakar)

# Bone Marrow Cells Classification using Deep Learning
This repository contains Python code for a deep learning project that focuses on the classification of bone marrow cells using medical imaging data. Below, you will find an overview of the code and its key components.

# Overview
The classification of bone marrow cells is a critical task in medical diagnostics. This project leverages deep learning techniques to classify bone marrow cells based on medical images. The code achieves accurate classification results.

# Dataset Link:
https://www.kaggle.com/datasets/andrewmvd/bone-marrow-cell-classification/

# Key Components
## 1. Data Preparation
The code loads medical imaging data for bone marrow cell classification.
It preprocesses the data, including resizing images and preparing training and testing sets.
## 2. Model Architecture
The code defines a deep learning model using TensorFlow/Keras.
It uses the EfficientNetB5 architecture as a base model, followed by additional layers for classification.
Batch normalization, dropout, and regularization techniques are applied to enhance model performance.
## 3. Training and Callbacks
The model is trained using the training dataset.
A custom callback, MyCallback, is utilized to monitor and adjust the learning rate based on various criteria.
Training progress is logged, including loss, accuracy, learning rate adjustments, and more.
## 4. Visualization and Evaluation
The code includes functions for visualizing training and testing results, such as loss and accuracy over epochs.
Model performance is evaluated on both training and testing datasets.
Usage

# To use this code, follow these steps:

Clone or download the code from the Kaggle notebook.
Install the required dependencies, including libraries like TensorFlow, NumPy, pandas, and more.
Run the code cells in the notebook sequentially. Adjust any parameters or settings as necessary for your specific use case.
Monitor the training progress and evaluate the model's performance using the provided metrics.

# Results
The code achieves accurate classification results for bone marrow cells.I have got accuracy of 95.545% Detailed performance metrics and visualizations can be found in the Kaggle notebook.

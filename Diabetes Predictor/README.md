# Diabetes Predictor

### 🎯 **Goal**

The main goal of this project is to develop a predictive model that can accurately determine the likelihood of diabetes in individuals based on their medical parameters. By leveraging deep learning techniques and a comprehensive dataset, the project aims to provide a reliable tool for early detection and risk assessment of diabetes.

### 🧵 **Dataset**

The dataset can be accessed from the following source:  [Kaggle: Diabetes Data Set](https://www.kaggle.com/datasets/mathchi/diabetes-data-set)


### 🧾 **Description**

This project focuses on the development of a Deep learning model for predicting the likelihood of diabetes in individuals based on various medical parameters. Diabetes is a prevalent health condition affecting millions of people worldwide, and early detection plays a crucial role in managing the disease and preventing complications.

The project utilizes a comprehensive dataset containing medical information such as glucose levels, blood pressure, BMI, insulin levels, and other relevant features. By analyzing this data and applying Deep learning algorithms, the model aims to accurately classify individuals as either diabetic or non-diabetic.



### 📜 **Repo Structure**

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


### 🧮 **What I had done!**
- Added Deep Learning Models and Streamlit Application for Diabetic Prediction

- This project introduces Deep Learning models trained on diabetic data for diabetic prediction. It includes the implementation of artificial neural network (ANN), long short-term memory (LSTM), and recurrent neural network (RNN) models using TensorFlow.

- A Streamlit application has been developed to provide a user-friendly interface for predicting diabetes based on user input. The application allows users to input various parameters, such as glucose level, blood pressure, BMI, etc. and predicts the likelihood of diabetes using the trained models.

### 🚀 **Models Implemented**

- Artificial Neural Network (ANN)
- Long Short Term Memory (LSTM)
- Recurrent Neural Netowrk (RNN)

### 📚 **Libraries Needed**

- TensorFlow
- Pandas
- Plotly Graph Objects
- Seaborn
- Sklearn
- Matplotlib
- Streamlit

### 📊 **Exploratory Data Analysis Results**

![image](https://github.com/Sgvkamalakar/DL-Simplified/assets/103712713/a1a592c0-09b2-4ea4-99d4-be5931c87fbe)

![image](https://github.com/Sgvkamalakar/DL-Simplified/assets/103712713/890b4b3a-ea88-4960-9286-6aa08089942a)

![image](https://github.com/Sgvkamalakar/DL-Simplified/assets/103712713/d5410231-97fa-4aa1-ba15-8c01c3300a1e)

### ⚙️ **Usage**

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

    
### 📈 **Performance of the Models based on the Accuracy Scores**
<div align="center">
<table>
  <tr>
    <th>Model</th>
    <th>Validation Accuracy</th>
  </tr>
  <tr>
    <td>ANN</td>
    <td>77.2%</td>
  </tr>
  <tr>
    <td>LSTM</td>
    <td>75.3%</td>
  </tr>
  <tr>
    <td>RNN</td>
    <td>77.2%</td>
  </tr>
</table>
</div>

![image](https://github.com/Sgvkamalakar/DL-Simplified/assets/103712713/a68fccbe-1035-405e-9dbe-f67c652bff48)



### 📢 **Conclusion**

Based on the validation accuracy scores, the ANN and RNN models achieved the highest accuracy of approximately 77.27%, while the LSTM model achieved slightly lower accuracy at 75.32%. Therefore, the ANN and RNN models can be considered the best-fitted models for this project.


### ✒️ **Signature**

<p align="center">
  <img src="https://github.com/sgvkamalakar.png" height="200" width="200"/>
</p>
<p align="center">
  Kamalakar Satapathi
</p>

 
Connect with me on [![LinkedIn](https://img.shields.io/badge/-Kamalakar_Satapathi-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sgvkamalakar)

Explore my codes [![GitHub](https://img.shields.io/badge/-Sgvkamalakar-181717?style=flat-square&logo=github)](https://github.com/sgvkamalakar)

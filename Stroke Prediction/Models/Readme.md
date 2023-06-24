# Heart Stroke Prediction




## Goal


The main goal of this project is to develop a predictive model that can accurately predict the likelihood of a heart stroke for individuals based on various features such as `AGE`,`HEART DISEASE`,`GLUCOSE LEVEL`,`BMI` etc. The purpose of this project is to assist in early detection and prevention of heart strokes, enabling timely medical interventions.


## Dataset

The dataset for this project can be found at link given below. 

[![Dataset link](https://img.shields.io/badge/Dataset-Link-green.svg)](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset)



## Approach

1. Data loading and exploration: Loaded the dataset, examined its structure, and performed initial exploratory data analysis (EDA) to gain insights into the data distribution, missing values, and relationships between variables.

2. Data preprocessing: Conducted data preprocessing steps such as handling missing values, encoding categorical variables, and scaling numerical features to prepare the data for model training.

3. Feature selection: Applied feature selection techniques to identify the most relevant features that contribute significantly to the prediction of heart strokes. This helps in reducing model complexity and improving performance.

4. Model development:

```bash
  a.Artificial Neural Network (ANN)- Fully connected neural network model: Constructed 
  an ANN model using the Keras library with multiple hidden layers and appropriate 
  activation functions. Trained the model on the preprocessed data and optimized it using 
  backpropagation algorithms.
```
    
```bash
  b. Feedforward Neural Network (FNN): Developed an FNN model using the Keras library 
  with multiple hidden layers and appropriate activation functions. Trained the model using  
  the preprocessed data and fine-tuned hyperparameters to achieve optimal performance.
```
```bash
  c. Recurrent Neural Network (RNN): Utilized an RNN model, specifically the LSTM (Long 
  Short-Term Memory) architecture, to capture temporal dependencies in sequential data.
  Trained the model on the preprocessed sequential data and fine-tuned the 
  hyperparameters for optimal results.
```
5. Model evaluation: Evaluated the performance of each model using appropriate metrics such as accuracy and precision. 
       
## Libraries Needed

- Pandas
- Numpy
- keras
- seaborn
- matplotlib,etc.

## Accuracies

| Model            | Accuracy                                                               |
| ----------------- | ------------------------------------------------------------------ |
| ANN | 0.8346379647749511 |
| RNN | 0.9393346379647749 |
| FNN| 0.9510763209393346 |



## Conclusion
 In conclusion, this project aimed to predict heart strokes using machine learning models. Among the models developed, the Feedforward Neural Network (fNN) achieved the highest accuracy of 95%. This suggests that the temporal dependencies captured by the FNN architecture are valuable in predicting heart strokes. 

## Harsh Raj

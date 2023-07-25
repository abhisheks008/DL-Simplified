
# Avocados Classification




## Goal


The main goal of this project is to develop a Dl model that can accurately predict whether an avocado is conventional or organic based on various features such as `Size of Bags`,`Volume`,`Price` etc. The purpose of this project is to categorize avocados as conventional or organic for better market segmentation and analysis.

## Dataset

The dataset for this project can be found at link given below. 

[![Dataset link](https://img.shields.io/badge/Dataset-Link-red.svg)](https://www.kaggle.com/datasets/neuromusic/avocado-prices)



## Approach

1. Data loading and exploration: Loaded the dataset, examined its structure, and performed initial exploratory data analysis (EDA) to gain insights into the data distribution, missing values, and relationships between variables.

2. Data preprocessing: Conducted data preprocessing steps such as handling missing values, encoding categorical variables, and scaling numerical features to prepare the data for model training.

3. Feature selection: Applied feature selection techniques to identify the most relevant features that contribute significantly to the prediction of heart strokes. This helps in reducing model complexity and improving performance.

4. Model development:

```bash
  a.LSTM (Long Short-Term Memory In avocado classification, LSTM 
  classifies by taking sequential input data and processing it through 
  memory cells, which learn to retain relevant information. It builds the 
  model using multiple LSTM layers to capture complex patterns, and then 
  applies a dense layer for final classification based on the learned 
  temporal dependencies, resulting in accurate avocado classification.
```
    
```bash
  b. Feedforward Neural Network (FNN): Developed an FNN model using the Keras library 
  with multiple hidden layers and appropriate activation functions. Trained the model using  
  the preprocessed data and fine-tuned hyperparameters to achieve optimal performance.
```
```bash
  c. Recurrent Neural Network (RNN): TABNET classifies using a unique 
  attention mechanism that selects and updates relevant features during 
  training. It builds the model by iteratively selecting subsets of 
  features, employing shared decision trees, and gradually learning 
  feature importance, leading to an interpretable and efficient model 
  for accurate avocado classification..
```
5. Model evaluation: Evaluated the performance of each model using appropriate metrics such as accuracy and precision. 
       
## Libraries Needed

- Pandas
- Tensorflow
- Seaborn
- sklearn
- pathlib
- numpy
- keras
- torch
## Accuracies

| Model            | Accuracy                                                               |
| ----------------- | ------------------------------------------------------------------ |
| TabNet |  0.79 |
| LSTM |9389041095890411 |
| FNN| 1.0 |



## Conclusion
 In conclusion, this project aimed to classifies Avocados using DL models. Among the models developed, the Feedforward Neural Network (fNN) achieved the highest accuracy of 100%. This suggests that the temporal dependencies captured by the FNN architecture are valuable in Classifying Avocados. 

## Harsh Raj


# Earthquake type Classification




## Goal


The main goal of this project is to develop a Dl model that can accurately classify the type of earthquake based on various features such as `Latitude`,`Longitude`,`Magnitude`,`Azimuthal gap` etc. The purpose of this project is that wether a given earthquake is detected by automatic detection systems.

## Dataset

The dataset for this project can be found at link given below. 

[![Dataset link](https://img.shields.io/badge/Dataset-Link-yellow.svg)](https://www.kaggle.com/datasets/usgs/earthquake-database)



## Approach

1. Data loading and exploration: Loaded the dataset, examined its structure, and performed initial exploratory data analysis (EDA) to gain insights into the data distribution, missing values, and relationships between variables.

2. Data preprocessing: Conducted data preprocessing steps such as handling missing values, encoding categorical variables, and scaling numerical features to prepare the data for model training.

3. Feature selection: Applied feature selection techniques to identify the most relevant features that contribute significantly to the prediction of heart strokes. This helps in reducing model complexity and improving performance.

4. Model development:

```bash
  a.GRU (Gated Recurrent Unit): It efficiently processes temporal data by selectively updating 
  and resetting hidden states, capturing important patterns in seismic signals. Its ability to handle
 variable-length sequences makes it suitable for identifying earthquake patterns in time-series data.
```
    
```bash
  b. Feedforward Neural Network (FNN): Developed an FNN model using the Keras library 
  with multiple hidden layers and appropriate activation functions. Trained the model using  
  the preprocessed data and fine-tuned hyperparameters to achieve optimal performance.
```
```bash
  c. Bidirectional Recurrent Neural Networks (BRNNs);  It used in earthquake classification by 
  processing seismic time series data in both forward and backward directions. This architecture 
  captures temporal dependencies effectively, enabling the model to consider past and future 
  information simultaneously. BRNNs are adept at recognizing patterns in the seismic signals, allowing  
  them to classify earthquake events accurately based on their unique characteristics.
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

## Accuracies

| Model            | Accuracy                                                               |
| ----------------- | ------------------------------------------------------------------ |
| BRNN |  0.8960000276565552 |
| GRU |0.8920000195503235 |
| FNN| 1.0 |

   ![IMG_20230729_174802](https://github.com/RAJharsh02/Earthquake-type-prediction/assets/118257196/5947898d-04a1-4b1b-8f67-b63254482f68)

## Conclusion
 In conclusion, this project aimed to classifies Earthquake using DL models. Among the models developed, the Feedforward Neural Network (fNN) achieved the highest accuracy of 100%. This suggests that the temporal dependencies captured by the FNN architecture are valuable in Classification. 

## Harsh Raj

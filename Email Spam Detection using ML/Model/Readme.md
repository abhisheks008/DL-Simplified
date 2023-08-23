# Predictions based on the following approaches

## BERT Fine-Tuning

    Using the test dataset as my validation dataset I achieved the accuracy of about 87%.

# Email Spam Detection using ML #340

## Goal

The main goal of this project is to develop a ML model that can accurately classify the emails as spam or ham(not spam).

## Dataset

The dataset for this project can be found at link given below.

https://www.kaggle.com/datasets/mayank07thakur/spam-mail-dataset

## Approach

1. Data loading and exploration: Loaded the dataset, examined its structure, and performed initial exploratory data analysis (EDA) to gain insights into the data distribution, missing values, and relationships between variables.

2. Data preprocessing: Conducted data preprocessing steps such as handling missing values, encoding categorical variables to prepare the data for model training.

3. Feature Extraction: Applied feature selection techniques to identify the most relevant features that can be used as the input for Logistic Regression. This helps in reducing model complexity and improving performance.

4. Model development:

```bash
    a. Bidirectional Recurrent Neural Networks (BRNNs);  It used in earthquake classification by
  processing seismic time series data in both forward and backward directions. This architecture
  captures temporal dependencies effectively, enabling the model to consider past and future
  information simultaneously. BRNNs are adept at recognizing patterns in the seismic signals, allowing
  them to classify earthquake events accurately based on their unique characteristics.
```

```bash
  b. Long Short Term Memory (LSTM): It is a type of recurrent neural network (RNN) architecture designed to handle sequences and time-series data. LSTM networks are particularly well-suited for tasks involving sequential data, such as natural language processing, speech recognition, and video analysis.
```

```bash
    c. Logistic Regression is a statistical method used for binary classification tasks, where the goal is to predict whether an input belongs to one of two classes. Despite its name, logistic regression is a classification algorithm rather than a regression algorithm.
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

| Model | Accuracy           |
| ----- | ------------------ |
| BRNN  | 0.8664000276565552 |
| GRU   | 0.8663676977157593 |
| LG    | 0.9659192825112107 |

![IMG_20230729_174802](https://github.com/RAJharsh02/Earthquake-type-prediction/assets/118257196/5947898d-04a1-4b1b-8f67-b63254482f68)

## Conclusion

In conclusion, this project aimed to classifies emails using DL models. Among the models developed, the Logistic Regression Binary Classification model achieved the highest accuracy of 97%. This suggests that the temporal dependencies captured by the logistic regression architecture are valuable in Classification.

## Mayank Thakur

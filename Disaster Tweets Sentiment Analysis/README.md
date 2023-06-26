# Disaster Tweets Sentiment Analysis

**PROJECT TITLE**

Disaster Tweets Sentiment Analysis

**GOAL**

The main goal of this project is to develop a classification model that can accurately distinguish between disaster tweet from a non-disaster tweet. The purpose of the project is to explore the performance of different deep learning models in this specific classification task.

**DATASET**

The dataset used for this project can be found at [link to dataset](https://www.kaggle.com/competitions/nlp-getting-started/data). The dataset consists of a collection of tweets labeled as either disaster tweet (1) or non-disaster tweet (0).

**DESCRIPTION**

This project aims to build a classification model that can classifies tweets as either disaster or non-disaster tweet. By leveraging deep learning models, the project seeks to achieve accurate and reliable classification results.

**WHAT I HAD DONE**

1. Data collection: Gathered a diverse dataset of tweets.
2. Data preprocessing: Performed necessary preprocessing steps such as lowercasing, removal of special characters and punctuation, tokenization, etc.
3. Model selection: Chose popular deep learning models: BERT, LSTM for the classification task.
4. Model training: Trained each model using the labeled dataset and appropriate training configurations.
5. Model evaluation: Evaluated the trained models on a separate test dataset to measure their performance.
6. Comparative analysis: Compared the accuracy and results of each model to determine the best-performing model.

**MODELS USED**

The following models were used in this project:

1. BERT
2. LSTM

The choice of these models was based on their proven performance in sentiment analysis tasks and their varying architectural complexities. This allowed for a comprehensive analysis of different model types.

**LIBRARIES NEEDED**

The following libraries are required to run this project:

- TensorFlow
- Keras
- numpy
- matplotlib
- pandas
- sklearn

**VISUALIZATION**

<img src = "../Images/Words.png">
<img src = "../Images/Target_Distribution.png">
<img src = "../Images/Disaster_Word_Count.png">
<img src = "../Images/Total_Characters.png">



**ACCURACIES**

The accuracy results obtained for each model on the test dataset are as follows:

- LSTM: 0.73
- BERT: 0.67

**CONCLUSION**

Based on the accuracy results, LSTM achieved the highest accuracy of 79% on the test dataset, making it the best-fitted model for this particular project. BERT also performed well but had slightly lower accuracy. This project demonstrates the effectiveness of deep learning models in sentiment analysis. 

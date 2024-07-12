# **Suicide and Depression Detection**

### 🎯 Goal
The goal of this project is to detect suicide ideation and depression from text data using various machine learning models.

### Purpose
This project aims to build a reliable text classifier that can accurately identify posts indicating suicide ideation or depression, thereby potentially aiding in early intervention and support.

### 🧵 Dataset
The dataset used in this project is: https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch/data

### 🧾 Description
The dataset is a collection of posts from the "SuicideWatch" and "depression" subreddits on the Reddit platform. The posts were collected using the Pushshift API, covering all posts made to "SuicideWatch" from December 16, 2008 (creation) to January 2, 2021, and "depression" posts from January 1, 2009, to January 2, 2021. All posts from "SuicideWatch" are labeled as suicide, while posts from the depression subreddit are labeled as depression. Non-suicide posts were collected from the "teenagers" subreddit.

### 🚀 Models Implemented
The following models were implemented in this project:
- LSTM (Long Short-Term Memory)
- BiLSTM (Bidirectional Long Short-Term Memory)
- GRU (Gated Recurrent Unit)
- BiLSTM-RNN (Bidirectional Long Short-Term Memory Recurrent Neural Network)

### 📚 Libraries Needed
To run this project, you will need the following libraries:
- TensorFlow
- Keras
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

### 📊 Exploratory Data Analysis Results
Exploratory Data Analysis (EDA) was conducted to understand the distribution of the data, the frequency of words, and the sentiment of the posts. Key findings from the EDA include:
1. Word frequency analysis revealed common terms used in suicide and depression posts.
2. Sentiment analysis indicated a predominance of negative sentiment in posts labeled as suicide or depression.

### 📈 Performance of the Models based on the Accuracy Scores
| Model            | Accuracy                                                               |
| ----------------- | ------------------------------------------------------------------ |
| LSTM | 90.3% |
| Bi-LSTM | 90.7% |
| Bi-LSTM-RNN| 92.3% |
| GRU | 94% |

### 📢 Conclusion
The GRU model achieved the highest accuracy in detecting suicide ideation and depression from text data. This model can be further optimized and deployed in real-world applications to provide timely support to individuals in need.

### Accuracy Results
The models demonstrated good accuracy in detecting suicide ideation and depression, with the GRU model being the best performing model.

### Best Fitted Model
The GRU model was the best-fitted model for this dataset, achieving the highest accuracy score.

## ✒️ Contributor
- Name: Khushi Kalra
- Github: https://www.github.com/abckhush

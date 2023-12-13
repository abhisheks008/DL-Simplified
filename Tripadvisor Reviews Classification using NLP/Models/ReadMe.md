**PROJECT TITLE**
TripAdvisor Reviews Classification Using NLP

**GOAL**
To classify TripAdvisor reviews  using NLP
**DATASET**
https://www.kaggle.com/datasets/arnabchaki/tripadvisor-reviews-2023/data

**DESCRIPTION**
The project compares accuracy of Glove embeddings with GRU to that of Logistic Regression with Tfidf Vectorizer.This project involves combining traditional machine learning with deep learning techniques to classify sentiment in TripAdvisor reviews, offering a comprehensive exploration of different methods for text classification.

**WHAT I HAD DONE**
1. TF-IDF Vectorizer and Logistic Regression:
a. Data Preparation:
Dataset: Collect a dataset of TripAdvisor reviews with labeled sentiments .
Preprocessing: Clean and preprocess the text data, including steps like removing stop words, stemming, and handling special characters.
b. Feature Extraction:
TF-IDF Vectorizer: Convert the preprocessed text data into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization. This technique assigns weights to words based on their importance in the corpus.
c. Model Building:
Logistic Regression: Train a logistic regression classifier using the TF-IDF vectors as input features. Logistic Regression is a commonly used algorithm for binary classification tasks.
d. Model Evaluation:
Split Data: Split the dataset into training and testing sets.
Evaluate Performance: Assess the model's performance using metrics like accuracy, precision, recall, and F1-score on the test set.
2. Glove Embeddings and GRU:
a. Data Preparation:
Embeddings: Use pre-trained Glove embeddings to convert words into dense vectors. Glove embeddings capture semantic relationships between words.
Padding: Ensure that all sequences of reviews have the same length by padding or truncating them.
b. Model Architecture:
GRU Neural Network: Build a neural network using GRU layers for sequential data processing. GRUs are a type of recurrent neural network (RNN) that can capture long-term dependencies in sequential data.
c. Model Training:
Transfer Learning: Fine-tune the pre-trained Glove embeddings or use them as fixed weights.
Training: Train the GRU neural network on the labeled TripAdvisor reviews.
d. Model Evaluation:
Validation: Evaluate the performance of the GRU model on a validation set to tune hyperparameters.
Test Set Evaluation: Assess the final model's performance on a separate test set using appropriate evaluation metrics.

**MODELS USED**
Logistic Regression, RNN

**LIBRARIES NEEDED**
Pandas, Numpy, Keras,TensorFlow, ScikitLearn, Seaborn, Matplotlib,NLTK

**VISUALIZATION**
![EDA -1 ](<../Images/Screenshot (257).png>)
![EDA -2](<../Images/Screenshot (259).png>)

**ACCURACIES**
Around 94% for Logistic Regression
Around 85% for GRU with Glove Embeddings

**CONCLUSION**
*TF-IDF Vectorization:*
Use the TF-IDF Vectorizer to convert the preprocessed text data into numerical features.
TF-IDF assigns weights to words based on their importance in a document relative to the entire corpus.
This results in a sparse matrix where each row represents a document, and each column represents a unique word with its corresponding TF-IDF weight.

*GloVe Embeddings*
 GloVe embeddings capture semantic relationships between words based on their co-occurrence statistics in a large corpus. This helps the model to understand the meaning and context of words in a more nuanced way compared to traditional one-hot encoding.
*GRU*
GRU, being a type of recurrent neural network (RNN), is effective in capturing sequential dependencies in data. It can understand the relationships between words in a sequence, which is crucial for understanding the meaning of sentences and paragraphs.

**YOUR NAME**
Aindree Chatterjee


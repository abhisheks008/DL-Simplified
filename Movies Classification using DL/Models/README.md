# Movie Genre Predictor 🍿<br>

## 🎯 Goal<br>

The Movie Genre Predictor is a project aimed at predicting the genres of movies based on textual information, such as movie descriptions or overviews. The goal is to build a model that can automatically assign appropriate genres to movies, facilitating better categorization and recommendation systems.<br>

## 🧵 Dataset<br>

The dataset used for this project is sourced from [Millions of Movies](https://www.kaggle.com/datasets/akshaypawar7/millions-of-movies) on Kaggle. It comprises extensive information about movies, including titles, overviews, genres, and other relevant details.

## 🧾 Description<br>

This project involves natural language processing (NLP) techniques to analyze and predict movie genres. The model is trained on movie overviews, and various machine learning algorithms are employed for accurate genre prediction.<br>

## 🧮 What I Had Done<br>

1. **Data Preprocessing:**<br>
   - Cleaning and tokenization of movie overviews.<br>
   - Handling missing or irrelevant data.<br>

2. **Feature Engineering:**<br>
   - Utilizing TF-IDF or word embeddings for representing movie overviews.<br>

3. **Model Training:**<br>
   - Training Deep learning models on preprocessed text data.<br>

4. **Model Evaluation:**<br>
   - Evaluating models on test data.<br>
   - Comparing the performance of different models.<br>

## 🚀 Models Implemented<br>

- DL model 1 <br> 
   The model is a sequential neural network with an input layer of 256 neurons, followed by dropout for regularization, a hidden layer of 128 neurons, additional dropout, and an output layer for multi-class classification using softmax activation.<br>

- DL model 2<br>
   The model is a sequential neural network with progressively decreasing hidden layer sizes (256, 128, 64, 32), each followed by dropout for regularization, and concludes with an output layer for multi-class classification using softmax activation, where the number of neurons in the output layer is determined by the unique classes in the training labels.<br>

- LSTM Model <br>
   This model is a sequential neural network with an embedding layer for word representation, followed by three LSTM (Long Short-Term Memory) layers, where the first two have return_sequences=True to pass the entire sequence to the next layer, and the third LSTM layer does not return sequences. The final layer is a dense layer with 20 neurons using softmax activation for multi-class classification.<br>

## 📚 Libraries Needed<br>

1. Scikit-learn<br>
2. NLTK (Natural Language Toolkit)<br>
3. Pandas<br>
4. Matplotlib<br>
5. Seaborn<br>

## 📊 Exploratory Data Analysis Results<br>

- Word Clouds showcasing frequent terms in movie overviews.<br>
- Distribution of movie genres in the dataset.<br>

## 📈 Performance of the Models based on Accuracy Scores<br>

1. DL model 1 : 52%<br>
2. DL model 2 : 45%<br>
3. LSTM model : 26%<br>


## 📢 Conclusion<br>

The Movie Genre Predictor project demonstrates the effectiveness of machine learning algorithms in predicting movie genres based on textual information. The Random Forest Classifier achieved a promising accuracy of 55.3%, providing a reliable method for automated movie genre assignment.<br>

## ✒️ Your Signature<br>

Dipayan Majumder<br>
(https://github.com/dipayan22/)<br>

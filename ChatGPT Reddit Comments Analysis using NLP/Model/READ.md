## **ChatGPT Reddit Comments Analysis using NLP**

### 🎯 **Goal**

The aim of this project is to analyze the reddit comments on ChatGPT using NLP and DL methods.

### 🧵 **Dataset**

[Kaggle-link](https://www.kaggle.com/datasets/armitaraz/chatgpt-reddit)

### 🧾 **Description**

This sentiment analysis project aims to analyze and classify user comments into positive, negative, or neutral sentiments. The dataset consists of user comments, and the goal is to build and evaluate different neural network models for sentiment classification.

### 🧮 **What I had done!**
1. Data Cleaning:
   
* Applied various text cleaning techniques to preprocess user comments.
* Removed URLs, special characters, numerical values, and unnecessary symbols.
* Standardized text using stemming and lemmatization.

2. Sentiment Labeling:

* Assigned sentiment labels (Positive, Negative, Neutral) to each user comment based on the sentiment analysis task using VADER sentiment analyser.

3. Baseline Models:
   
* Implemented baseline sentiment analysis models using traditional machine learning approaches.
* Utilized TF-IDF vectorization to represent text data.
* Trained classifiers to establish baseline performance.

4. Neural Network Models:

* Explored and implemented different neural network architectures for sentiment analysis.
* Experimented with Simple RNN, LSTM, GRU, and Bidirectional GRU models.
* Utilized TensorFlow and Keras for model implementation.

5. BERT-based Model:

* Incorporated a pre-trained BERT model for fine-tuning on the sentiment analysis task.
* Tokenized and encoded the text using a BERT tokenizer.
* Explored the capabilities of transfer learning with BERT.

6. Performance Evaluation:

* Evaluated models on key performance metrics, including accuracy, precision, recall, and F1-score.
* Conducted a detailed comparison of model performances to identify strengths and weaknesses.
   
### 🚀 **Models Implemented**

1. Simple RNN Model:
   
   Simple RNNs are fundamental recurrent neural networks capable of learning sequential patterns. Implemented as a baseline model to understand the basic capabilities of neural networks for sentiment analysis.

2. LSTM Model:

   Long Short-Term Memory (LSTM) networks are designed to capture long-term dependencies in sequential data. Implemented to explore the model's ability to capture nuanced sentiment patterns.

3. GRU Model:

   Gated Recurrent Units (GRU) are computationally more efficient variants of LSTM. Implemented to evaluate performance compared to LSTM and assess the impact of model simplicity.

4. Bidirectional GRU Model:

   Bidirectional models process input sequences in both forward and backward directions, enhancing context understanding. Implemented to investigate the benefits of bidirectionality in sentiment analysis.

5. BERT-based Model:

   BERT (Bidirectional Encoder Representations from Transformers) is a powerful transformer-based model pre-trained on vast amounts of data. Fine-tuned for sentiment analysis to explore the capabilities of transfer learning on a complex language understanding task.

### 📚 **Libraries Needed**

1. Pandas
2. NumPy
3. wordclud
4. matplotlib.pyplot
5. seabon
6. vaderSentiment
7. nltk
8. re
9. string
10. keras
11. tensorflow
12. sklean.metrics
13. tqdm
14. os
15. transformers
16. BertWordPieceTokenizer

### 📊 **Exploratory Data Analysis Results**

![word_cloud](https://github.com/lakshmipriya-ragupathi/DL-Simplified/assets/101037197/6c0d54cc-a972-4a6b-9a8e-7b6188b877e7)

![subreddit_distribution](https://github.com/lakshmipriya-ragupathi/DL-Simplified/assets/101037197/17388f28-b17c-4097-9851-ca11cccbbdbc)

![sentiment_distribution_per_subreddit](https://github.com/lakshmipriya-ragupathi/DL-Simplified/assets/101037197/31b1416f-41b2-4e9b-ad07-1cb8e6e132fb)

![sentiment_distribution](https://github.com/lakshmipriya-ragupathi/DL-Simplified/assets/101037197/2c27b876-f937-45bd-95ff-793872338413)

### 📈 **Performance of the Models based on the Accuracy Scores**

1. Sequential Model (Simple RNN):
   * Accuracy: 0.52
   * Precision (Positive): 0.36
   * Recall (Positive): 0.29
   * F1-score (Positive): 0.32

2. Sequential_1 Model (LSTM):
   * Accuracy: 0.58
   * Precision (Positive): 0.49
   * Recall (Positive): 0.23
   * F1-score (Positive): 0.31

3. Sequential_2 Model (GRU):
   * Accuracy: 0.58
   * Precision (Positive): 0.50
   * Recall (Positive): 0.22
   * F1-score (Positive): 0.31

4. Sequential_3 Model (Bidirectional GRU):
   * Accuracy: 0.59
   * Precision (Positive): 0.50
   * Recall (Positive): 0.22
   * F1-score (Positive): 0.31

5. BERT-based Model:
   * Accuracy: 0.24
   * Precision (Positive): 0.24
   * Recall (Positive): 1.00
   * F1-score (Positive): 0.39



### 📢 **Conclusion**

The Bidirectional GRU-based model (Sequential_3) combines the advantages of the bidirectional layer with the GRU architecture.
It achieves competitive performance with fewer trainable parameters, making it more parameter-efficient.
The choice between Sequential_2 and Sequential_3 depends on factors like computational resources, dataset characteristics, and the desired trade-off between model complexity and performance.
Both Sequential_2 and Sequential_3 models exhibit similar performance, outperforming the Simple RNN and LSTM models in terms of accuracy and other metrics.
The BERT-based model shows significantly lower accuracy compared to the other models.
While the precision for the Positive class is better in the BERT model, it comes at the cost of extremely low recall and F1-score for other models.
The BERT-based model appears to heavily favor the Positive class, resulting in a poor overall performance.

### ✒️ **Your Signature**

LAKSHMIPRIYA RAGUPATHI

email : lakshmi190803@gmail.com

linkedin : https://www.linkedin.com/in/lakshmipriya-ragupathi/

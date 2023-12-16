# Twitter Sentiment Analysis NLP

## PROJECT TITLE

Twitter Sentiment Analysis NLP

## GOAL

The main goal of this project is to analyse the tweets of people using LSTM and Keras Sequential model

## DATASET

https://www.kaggle.com/datasets/kazanova/sentiment140. 

## DESCRIPTION

This project aims to perform a sentiment analysis on the tweets posted by various people, and group those into positive and negative tweets.

## WHAT I HAD DONE

1. Used NLTK to preprocess and clean text , using Stemmer, Lemmatizer, removing symbols, etc
2. Created sequential model using Keras, added weight initializers and regulators
3. Used Glove embeddings in other notebook
4. Created LSTM model with Conv1D, Spatial DropOut, Dense and other layers
5. Used confusion matrix
6. Used BERT for classification

## MODELS USED

1. Glove embeddings with LSTM
2. Sequential Model
3. BERT

## LIBRARIES NEEDED
- numpy
- pandas
- sklearn
- tensorflow
- keras
- scipy

## VISUALIZATION

![For Sequential Model](<../Images/Screenshot (277).png>)- keras sequential
![For LSTM](<../Images/Screenshot (279).png>) - lstm 

## EVALUATION METRICS

Confusion matrix was created and recall, f1 score, precision were used as metrics of accuracy

## RESULTS

LSTM has higher accuracy (About 78%) compared to 72% of Keras sequential model. The highest accuracy is offered by BERT at 87%

## CONCLUSION

Long Short-Term Memory (LSTM) networks are beneficial in tweet sentiment analysis compared to Keras Sequential models due to their ability to capture contextual dependencies and handle sequential data effectively. Tweets often contain short and informal language, making it challenging for traditional models to discern sentiment accurately. LSTMs, with their memory cells, can capture nuances in the temporal structure of tweets, considering dependencies between words and phrases. This enables LSTMs to grasp the sentiment context better than simple sequential models. In contrast, Keras Sequential models may struggle to capture the inherent sequential nature and intricate dependencies present in tweet data, leading to suboptimal performance in sentiment analysis tasks.Using encoders from Transformer enables BERT to have a better context understanding than traditional neural networks such as LSTM or RNN since the encoder process all inputs, which is the whole sentence, simultaneously so when building a context for a word, BERT will take into account the inputs before it

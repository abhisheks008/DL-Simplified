# Disaster Twitter Sentiment Analysis NLP

## PROJECT TITLE

Disaster Twitter Sentiment Analysis NLP

## GOAL

The main goal of this project is to analyse the tweets on disasters and classify them as fake and real using Transformers

## DATASET

https://www.kaggle.com/competitions/nlp-getting-started/data

## DESCRIPTION

The main goal of this project is to analyse the tweets on disasters and classify them as fake and real using Transformers. Also, standard ML models like Random forest, SVC, logistic regression are used for this research

## WHAT I HAD DONE

This neural network architecture is tailored for Natural Language Processing (NLP) tasks. The Positional Embedding incorporates the sequential order of words, crucial for understanding context. The Transformer Encoder captures contextual information, enabling the model to comprehend relationships within input sequences. Global Max Pooling 1D extracts salient features, reducing dimensionality for efficient processing. Dropout mitigates overfitting, enhancing the model's generalization ability. The Dense layer produces the final prediction, with the architecture designed for tasks like text classification or sentiment analysis. Overall, this combination empowers the model to effectively process and interpret textual data, making it suitable for a range of NLP applications.

## MODELS USED

1. Random forest regressor
2. SVC
3. Logistic Regression
4. Decision Tree Regression
5. Transformer based Neural Network

## LIBRARIES NEEDED
- numpy
- pandas
- sklearn
- tensorflow
- keras
- scipy

## VISUALIZATION

EDA was used to compare tweets based on number of words, lettercount and the keywords mentioned. Bar Charts were used.
Confusion matrix was used to compare the performance of standard ML models
Graph of training and test accuracy were used for comparing performance of transformer based models
Now, we also use wordclouds to graphically depict the keywords and words with highest frequency in both kinds of tweets.

## EVALUATION METRICS

Confusion matrix was created and recall, f1 score, precision were used as metrics of accuracy

## RESULTS

Transformers provide 95% accuracy which is significantly higher than Logistic Regression and Decision Tree models coming at 81% accuracy

## CONCLUSION
The provided neural network architecture is well-suited for classifying disaster tweets as fake or real in the context of natural language processing (NLP). Here's how each component contributes to this task:

Positional Embedding:

Helps the model understand the order of words in tweets, capturing nuances and context essential for discerning fake or real information during a disaster.
Transformer Encoder:

Enables the model to process the entire sequence of words, capturing intricate relationships and contextual information, which is crucial for distinguishing between authentic and misleading content in disaster-related tweets.
Global Max Pooling 1D:

Extracts the most significant features from the encoded sequence, focusing on key information that might indicate whether a tweet is reporting a real disaster or spreading misinformation.
Dropout:

Mitigates overfitting, enhancing the model's ability to generalize from training data to unseen examples, which is vital for accurately classifying diverse disaster-related tweets.
Dense Layer:

Produces the final prediction, indicating whether a given tweet is likely to be real or fake based on the features extracted by the preceding layers.
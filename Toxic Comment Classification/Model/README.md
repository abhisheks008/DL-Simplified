# Toxic Comment Classification

## PROJECT TITLE

Toxic Comment Classification

## GOAL

To rank comments based on the toxicity they have using NLP techniques.

## DATASET

The dataset used for this project can be found at [link to dataset](https://www.kaggle.com/datasets/julian3833/jigsaw-toxic-comment-classification-challenge?select=train.csv). 

## DESCRIPTION

This project aims to classify the comments as toxic, severe toxic, obscene, threat, insult or identity hate comments.

## WHAT I HAD DONE

1. Data collection: As the link I have mentioned is updated with new data periodically, there was o need to use any tweeter API to fetch the tweets.
2. Data preprocessing: Cleaned and preprocessed the data. In order to pass the data to the model we have to first embed it.
3. Model selection: Chose CNN, LSTM and Bi-directional LSTM.
4. Comparative analysis: Compared the Accuracy and Loss of all techniques.

## MODELS USED

1. Convolutional Neural Network
2. Long short term memory Neural Netowrk
3. Bi-directional Long short term memory Neural Netowrk


## LIBRARIES NEEDED

The following libraries are required to run this project:

- nltk
- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow

## VISUALIZATION
![bar](https://github.com/achrekarom12/DL-Simplified/assets/88442486/7bb768e1-7ab0-428c-a363-bb5479d43b73)



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss

## RESULTS
Accuracy for these models were:

| Model | Accuracy | Loss | 
| ----- | ---------------- | ---------------- | 
| CNN   | 0.676       | 0.054        |
| LSTM   | 0.924       | 0.06        |
| Bi-directional LSTM   | 0.964       | 0.059        |

## CONCLUSION
Based on the results we can draw following conclusions:
1. CNN Model: The CNN model achieved an accuracy of 0.676 with a loss of 0.054. This model utilizes convolutional layers for feature extraction from the text data. However, it seems to be less effective compared to the other models in capturing the complex patterns and dependencies within the text data.
2. LSTM Model: The LSTM model achieved the highest accuracy among the three models, with a score of 0.924 and a loss of 0.06. LSTM models are well-suited for capturing long-term dependencies in sequential data. The LSTM model's ability to remember past information and its sequential processing nature contributed to its superior performance compared to the CNN model.
3. Bi-directional LSTM Model: The bi-directional LSTM model achieved an accuracy of 0.964 with a loss of 0.059. Bi-directional LSTM models incorporate information from both past and future timesteps, allowing them to capture a broader context for prediction. This model outperformed both the CNN and LSTM models, indicating the effectiveness of utilizing bidirectional information flow for toxic comment classification.

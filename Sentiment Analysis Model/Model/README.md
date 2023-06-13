# Sentiment Analysis Model

## PROJECT TITLE

Sentiment Analysis Model

## GOAL

The main goal of this project is to analyse the iMDB review sentiment.

## DATASET

The dataset used for this project can be found at [link to dataset](https://www.kaggle.com/columbine/imdb-dataset-sentiment-analysis-in-csv-format/). 

## DESCRIPTION

This project aims to perform a sentiment analysis on the iMDB reviews. This sentiment analysis is done using Simple Neural Network, CNN and RNN (LSTM).

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Done stopword removal and word embedding.
3. Model selection: Chose Simple Neural Network, CNN and RNN (LSTM) for better sentiment analysis.
4. Comparative analysis: Compared the accuracy score of all the techniques.

## MODELS USED

1. Simple Neural Network
2. Convolutional Neural Network
3. Long short term memory Neural Network (Recurrent Neural Network)


## LIBRARIES NEEDED

The following libraries are required to run this project:

- re
- nltk
- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/5ecbe61f-d183-4463-b766-41fb9c72d1b0)



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss
- Confusion Matrix

## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| SNN    | 0.7178     | 0.9930    |
| CNN    | 0.8472     | 0.8535    |
| LSTM    | 0.8634    | 0.4711    |

#### Confusion Matrix:
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/88dc73b8-20f1-41d6-8827-c5af3abe9c3f)
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/f566e412-36fd-4a7a-bdbc-a3946936d3e9)
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/9040125c-4f5b-4c83-a374-ffa5c0deb09c)


## CONCLUSION
Based on results we can draw following conclusions:
1. SNN (Simple Neural Network) achieved an accuracy of 71.78% and a loss of 0.9930. While the accuracy is decent, the higher loss suggests that the model might not be effectively capturing the underlying patterns in the data.

2. CNN (Convolutional Neural Network) performed better with an accuracy of 84.72% and a loss of 0.8535. The model's ability to capture spatial dependencies through convolutional layers likely contributed to its improved performance compared to the SNN.

3. LSTM (Long Short-Term Memory) achieved the highest accuracy among the three models with 86.34% and a loss of 0.4711. LSTM's ability to retain and process information from longer sequences helped it capture the temporal dependencies in the text data, resulting in improved sentiment analysis performance.

In summary, the LSTM model outperformed the SNN and CNN models in terms of accuracy on the IMDB sentiment analysis task. This suggests that the sequential nature of the text data is crucial for accurately predicting sentiment. 

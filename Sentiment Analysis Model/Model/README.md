# Sentiment Analysis Model

## PROJECT TITLE

Sentiment Analysis Model,Sentiment Analysis with BERT/RoBERTa

## GOAL

The main goal of this project is to analyse the iMDB review sentiment.
The main goal of this project is to perform sentiment analysis, classifying textual data into positive or negative sentiments.

## DATASET

The dataset used for this project can be found at [link to dataset](https://www.kaggle.com/columbine/imdb-dataset-sentiment-analysis-in-csv-format/). 
The dataset consists of three CSV files:

Train.csv: Training data with two columns, text and label
Test.csv: Testing data with two columns, text and label
Valid.csv: Validation data with two columns, text and label
The label column contains binary values (0 or 1), representing the sentiment of each text sample.

## DESCRIPTION

This project aims to perform a sentiment analysis on the iMDB reviews. This sentiment analysis is done using Simple Neural Network, CNN and RNN (LSTM).
This project utilizes pre-trained BERT and RoBERTa models from the Hugging Face transformers library to classify sentiment. The models are fine-tuned on a custom dataset for binary sentiment classification.



## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Done stopword removal and word embedding.
3. Model selection: Chose Simple Neural Network, CNN and RNN (LSTM) for better sentiment analysis.
4. Comparative analysis: Compared the accuracy score of all the techniques.
Data Collection: Prepared Train.csv, Test.csv, and Valid.csv datasets.
Data Preprocessing: Tokenized the text using the BERT tokenizer.
Model Selection: Fine-tuned BERT (bert-base-uncased) and RoBERTa (roberta-base) for binary sentiment classification.
Training: Trained the models using the Trainer API from Hugging Face.
Evaluation: Evaluated model performance using metrics such as accuracy, precision, recall, and F1 score.

## MODELS USED

1. Simple Neural Network
2. Convolutional Neural Network
3. Long short term memory Neural Network (Recurrent Neural Network)
4.BERT (Bidirectional Encoder Representations from Transformers)
5.RoBERTa (A robustly optimized BERT pretraining approach)


## LIBRARIES NEEDED

The following libraries are required to run this project:

- re
- nltk
- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0
-Python 3.8+
-PyTorch
-Transformers
-Pandas
-scikit-learn


## VISUALIZATION
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/5ecbe61f-d183-4463-b766-41fb9c72d1b0)



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss
- Confusion Matrix
The evaluation metrics used to assess the models:

Accuracy
F1 Score
Precision
Recall

## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| SNN    | 0.7178     | 0.9930    |
| CNN    | 0.8472     | 0.8535    |
| LSTM    | 0.8634    | 0.4711    |
Results on the validation and test datasets:

Model	Accuracy	Precision	Recall	F1 Score
BERT	0.885	  0.872	        0.881        0.877
RoBERTa	0.893	    0.882	    0.890	    0.886



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
Based on the results, the following conclusions can be drawn:

BERT achieved a solid performance with 88.5% accuracy. Its balance between precision and recall shows it effectively captures patterns in the sentiment data.

RoBERTa slightly outperformed BERT with an accuracy of 89.3%. This improvement is attributed to RoBERTa’s robust optimization, leading to better generalization.

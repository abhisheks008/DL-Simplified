## PROJECT TITLE

CHATGPT Reddit Comments Analysis using NLP

## GOAL

To analyse the sentiments behind each comment and find out the best fitted model to predict it

## DATASET

The link for the dataset used in this project: https://www.kaggle.com/datasets/armitaraz/chatgpt-reddit

## DESCRIPTION

Find out the best fitted model to predict the sentiment

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above.
2. Data preprocessing: Preprocessed the given data
3. Sentiment Analysis:A sentiment analyzer is used to assign sentiment scores to each data point.Scores are converted to categorical labels:
   Negative: -1
   Neutral: 0
   Positive: 1
   A new column named "category" is added to the dataset containing these labels.
4. Text Normalization:Lemmatization and stemming are applied to reduce words to their base or root form.This reduces variations of words (e.g., "running", "runs", "ran" become "run").
5. Undersampling: If the dataset has class imbalance (unequal distribution of sentiment classes), undersampling is used to balance the classes.
   This can improve model performance.
6. TF-IDF (Term Frequency-Inverse Document Frequency) : is used to represent the text data numerically.It considers the importance of a word based on its frequency in a document and its rarity across the corpus.
7. Model selection: I chose to use LSTM,CNN and CNN+LSTM
8. Comparative analysis: Compared the accuracy score of all the models.

## MODELS USED

1. LSTM
2. CNN
3. CNN+LSTM

## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy
- pandas
- matplotlib
- tensorflow

## VISUALIZATION

<b>Positive sentiment words:</b>
![image](https://github.com/Diyaa0313/DL-Simplified/blob/main/ChatGPT%20Reddit%20Comments%20Analysis%20using%20NLP/Images/wordcloud1.png)
<b>Negative Sentiment words</b>
![image](https://github.com/Diyaa0313/DL-Simplified/blob/main/ChatGPT%20Reddit%20Comments%20Analysis%20using%20NLP/Images/wordcloud2.png)
<b>Neutral Sentiment Words</b>
![image](https://github.com/Diyaa0313/DL-Simplified/blob/main/ChatGPT%20Reddit%20Comments%20Analysis%20using%20NLP/Images/wordcloud2.png)

Epoch vs Loss plots :
<b>LSTM</b>
![image](https://github.com/Diyaa0313/DL-Simplified/blob/main/ChatGPT%20Reddit%20Comments%20Analysis%20using%20NLP/Images/plot_lstm.png)
<b>CNN</b>
![image](https://github.com/Diyaa0313/DL-Simplified/blob/main/ChatGPT%20Reddit%20Comments%20Analysis%20using%20NLP/Images/plot_cnn.png)
<b>CNN+LSTM</b>
![image](https://github.com/Diyaa0313/DL-Simplified/blob/main/ChatGPT%20Reddit%20Comments%20Analysis%20using%20NLP/Images/plot_cnn%2Blstm.png)

## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy
- Loss

## RESULTS

Results on Validation dataset:

| Model    | Accuracy | Loss  |
| -------- | -------- | ----- |
| LSTM     | 0.90     | 0.317 |
| CNN      | 0.88     | 0.364 |
| CNN+LSTM | 0.89     | 0.34  |

## CONCLUSION

Hence, we observe that LSTM is best fitted model for the sentiment analysis of the comments as it gives the highest accuracy with lowest loss.

## SIGNATURE

Diya Sen

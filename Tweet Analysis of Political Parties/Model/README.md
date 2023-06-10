# Tweet Analysis of Indian Political Parties

## PROJECT TITLE

Tweet Analysis of Indian Political Parties

## GOAL

The main goal of this project is to analyse the tweets of national level political parties and draw some useful insights.

## DATASET

The dataset used for this project can be found at [link to dataset](https://www.kaggle.com/datasets/aryansingh0909/indian-political-party-tweets-daily-updated). 

## DESCRIPTION

This project aims to perform a sentiment analysis on the tweets posted by official tweeter handles of respective ploitical parties. It also aims to analyse how these accounts are handled for example, tweet frequency, tweet length etc.

## WHAT I HAD DONE

1. Data collection: As the link I have mentioned is updated with new data periodically, there was o need to use any tweeter API to fetch the tweets.
2. Data preprocessing: There were lakhs of tweets and some of them were in Hindi so first I cleaned the text, removed symbols and unnecessary characters. Then I seperated English tweets and Hindi tweets. Took first 5000 hindi tweets and translated them in english before appending them back to english tweets.
3. Model selection: Chose VADER and RoBERTa for better sentiment analysis..
4. Comparative analysis: Compared the sentiment score of both the techniques.

## MODELS USED

1. VADER (Valence Aware Dictionary and Sentiment Reasoner)
2. RoBERTa (Robustly Optimized BERT Pre-training Approach)

The choice of these model was based on its proven performance for sentiment analysis and its architectural complexities. This allowed for a comprehensive analysis of different model types.

## LIBRARIES NEEDED

The following libraries are required to run this project:

- nltk
- torch==2.0.1
- torchvision==0.15.0
- torchaudio==0.8.1
- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- segmentation-models==1.0.1
- tensorflow
- transformers==4.11.3
- scipy==1.7.3

## VISUALIZATION

![Tweets Comparison](Images/final_comppng.png)

## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Sentiment Score
- Compound Score

## RESULTS

For three major political parties the scores were:
| Party | RoBERTa Positive | RoBERTa Neutral | RoBERTa Negative | Compound Score |
| ----- | ---------------- | ---------------- | ---------------- | -------------- |
| BJP   | 0.49107894       | 0.45851955        | 0.05040156       | 0.097866       |
| INC   | 0.21044777       | 0.50115585        | 0.2883963       | 0.07605211961357569       |
| AAP   | 0.23715205277117726       | 0.5601478454257109        | 0.20270010179630024       | 0.01372866       |

## CONCLUSION

Based on the scores, the analysis reveals that the BJP has a more positive sentiment, with a higher positive score and slightly positive compound score. The INC demonstrates a more neutral sentiment, with a higher neutral score and a slightly positive compound score. The AAP also exhibits a relatively neutral sentiment, with a slightly positive compound score but a balanced distribution between positive and negative scores. Overall, the sentiment analysis suggests a more positive sentiment associated with the BJP compared to the other two parties.
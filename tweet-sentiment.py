# using transformers, 
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer
import numpy as np
from scipy.special import softmax
import csv
import urllib.request


# preprocessing
def tweet_preprocessing():
  tweet_words = []

  for word in tweet.split(' '):
    if word.startswith('@') and len(word) > 1:
      word = "@user"
    
    elif word.startswith("http"):
      word = "http"
    tweet_words.append(word)  


  tweet_proc = " ".join(tweet_words)
  return tweet_proc

# load model / tokenizer
def tokenizer():
  roberta = "cardiffnlp/twitter-roberta-base-sentiment"
  model = AutoModelForSequenceClassification.from_pretrained(roberta)
  tokenizer = AutoModelForSequenceClassification.from_pretrained(roberta)

  labels = ["Negative", "Neutral","Positive"]
  return model, tokenizer, labels

# sentiment analysis
def sentiment_analysis(tweet):
  encoded_tweet = tokenizer(tweet_proc, return_tensors="pt")
  output = model(encoded_tweet["input_ids"],encoded_tweet["attention_mask"])
  output = model(**encoded_tweet)

  scores = output[0][0].detach.numpy()
  scores = softmax(scores, axis=1)
  return scores

# reading from csv
def analyze_tweets_from_csv(filename, model, tokenizer, labels):
  with open("elonmusk.csv", newline="") as csvfile:
    reader  = csv.DictReader(csvfile)
    for row in reader:
      tweet = row["Tweet"]
      tweet_proc = tweet_preprocessing(tweet)
      scores = analyze_sentiment(tweet)
      for i in range(len(scores)):
        label = labels[i]
        score = scores[i]
        print(f"{label}: {score:.4f} - {tweet}")

        if __name__ == __main__:
          model,tokenizer,labels = initialize_model_and_tokenizer()
          analyze_tweets_from_csv("/elonmusk.csv",model,tokenizer, labels)

  
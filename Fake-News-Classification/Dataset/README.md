# Fake News Classification using DL 

## PROJECT TITLE

Fake News Detection using Deep Learning 

## GOAL

To identify whether the given news is fake or not. 

## DATASET

The link for the dataset used in this project:  https://www.kaggle.com/competitions/fake-news/data?select=train.csv 


## DESCRIPTION

This project aims to identify whether the given news is fake or not by extracting meaning and semantics of the given news.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Preprocessed the news by combining title and text to create a new feature and did some augementation like tokeinizing and vectorising before passing them to model training
3. Model selection: Self Designed model having a Embedding Layer followed by Global Pooling Layer and then 2 Dense layers and then output layer

## MODELS SUMMARY

Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 embedding (Embedding)       (None, 12140, 182)        30222010  
                                                                 
 global_average_pooling1d (  (None, 182)               0         
 GlobalAveragePooling1D)                                         
                                                                 
 dense (Dense)               (None, 96)                17568     
                                                                 
 dense_1 (Dense)             (None, 24)                2328      
                                                                 
 dense_2 (Dense)             (None, 1)                 25        
                                                                 
=================================================================
Total params: 30241931 (115.36 MB)
Trainable params: 30241931 (115.36 MB)
Non-trainable params: 0 (0.00 Byte)

## LIBRARIES NEEDED

The following libraries are required to run this project:

- nltk
- pandas
- matplotlib
- tensorflow
- keras
- sklearn

## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss

It is shown using Confusion Matrix in the Images folder

## RESULTS
Results on Val dataset:

Accuracy:96.11%
loss: 0.1350

## CONCLUSION
Based on results we can draw following conclusions:

1.The model showed high validation accuracy of 96.11% and loss of 0.1350.Thus the model worked fairly well identifying 2874 fake articles from a total of 3044

# Musical Instrument Chord Classification

## PROJECT TITLE

Musical Instrument Chord Classification

## GOAL

To identify major or minor chords from the given audio.

## DATASET

The link for the dataset used in this project:  https://www.kaggle.com/datasets/deepcontractor/musical-instrument-chord-classification and https://www.kaggle.com/datasets/mehanat96/major-vs-minor-guitar-chords

## DESCRIPTION

This project aims to identify whether the given sound is major chord or minor chord.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Preprocessed the audios and created their spectograms in order to make predictions.
3. Model selection: Chose traditional CNN along with ANN and MLP.
4. Comparative analysis: Compared the accuracy score of all the models.

## MODELS USED

1. CNN
2. ANN
3. MLP


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION
![onechannel](https://github.com/achrekarom12/DL-Simplified/assets/88442486/1ff7750c-6da4-40f4-ba2a-23b8c5c69d90)



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.663     | 0.572   |
| ANN    | 0.81     | 0.916    |
| MLP    | 0.707     | 0.651    |


## CONCLUSION
Based on results we can draw following conclusions:
1. CNN: The CNN model achieved an accuracy of 0.663 and a loss of 0.572. CNNs are well-suited for handling grid-like data such as images and can automatically learn local patterns and spatial relationships. However, in this case, the CNN model's performance is relatively lower compared to the other models.
2. ANN: The ANN (Artificial Neural Network) model achieved an accuracy of 0.810 and a loss of 0.916. ANNs, also known as fully connected neural networks or MLPs, can handle various types of data. The ANN model shows the highest accuracy among the three models, indicating its effectiveness in capturing the underlying patterns in the data.
3. MLP: The MLP model achieved an accuracy of 0.707 and a loss of 0.651. MLPs, similar to ANNs, are versatile and can handle a wide range of data types. The MLP model's performance is intermediate between the CNN and ANN models in terms of accuracy.

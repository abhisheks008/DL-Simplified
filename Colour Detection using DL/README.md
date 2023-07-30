# Colour Detection using DL

## PROJECT TITLE

Colour Detection using DL

## GOAL

To detect 10 different colours using DL techniques. 

## DATASET

The link for the dataset used in this project:  https://www.kaggle.com/datasets/adikurniawan/color-dataset-for-color-recognition

## DESCRIPTION

This project aims to identify ten different colours from the given images.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Preprocessed the image in order to have all images in equal shape.
3. Model selection: Chose traditional CNN along with Image detection architecture VGG16 and ResNet15V2 for Image detection.
4. Comparative analysis: Compared the accuracy score of all the models.

## MODELS USED

1. CNN
2. VGG16
3. ResNet15V2


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION
![cnn](https://github.com/achrekarom12/DL-Simplified/assets/88442486/8336a43a-b9e0-4a74-a7dc-794c3b20f8ec)
![cnn 2](https://github.com/achrekarom12/DL-Simplified/assets/88442486/e68336fc-a0b3-488d-bce5-37b31fd12540)



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.9     | 0.326   |
| VGG16    | 0.825     | 0.154    |
| ResNet50    | 0.875     | 0.987    |


## CONCLUSION
Based on results we can draw following conclusions:
1. CNN Model: The CNN model achieved the highest accuracy of 90% and a relatively low loss of 0.326 on the validation dataset. This indicates that the CNN model performed well in learning and predicting color classes.
2. VGG16 Model: The VGG16 model showed an accuracy of 82.5% and a loss of 0.154. While it performed reasonably well, it didn't outperform the CNN model in terms of accuracy.
3. ResNet50 Model: The ResNet50 model achieved an accuracy of 87.5% but had a relatively high loss of 0.987. This suggests that the model might be overfitting or facing challenges in generalizing to new data.

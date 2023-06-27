# Leukaemia Classification using DL

## PROJECT TITLE

Leukaemia Classification using DL

## GOAL

To classify normal from abnormal cell images of Leukaemia.

## DATASET

The link for the dataset used in this project: https://www.kaggle.com/datasets/andrewmvd/leukemia-classification

## DESCRIPTION

This project aims to identify whether the given medical image contains Leukaemia cells or not.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Preprocessed the image in order to have all images in equal shape.
3. Model selection: Chose three Image detection architecture VGG16, ResNet50 and Inception for Image detection.
4. Comparative analysis: Compared the accuracy score of all the models.

## MODELS USED

1. InceptionV3
2. VGG16
3. ResNet50


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS

Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| Inception    | 0.684     | 0.706   |
| ResNet50    | 0.653     | 0.64    |
| VGG16    | 0.679     | 0.82    |


## CONCLUSION
Based on results we can draw following conclusions:
1. Inception: The Inception model achieved an accuracy of 68.4% with a loss of 0.706. It demonstrates moderate performance in distinguishing between leukemia and non-leukemia samples.
2. ResNet50: The ResNet50 model performed slightly lower with an accuracy of 65.3% and a loss of 0.64. It shows similar capabilities to Inception in leukemia detection.
3. VGG16: The VGG16 model achieved an accuracy of 67.9% but with a higher loss of 0.82. It falls between Inception and ResNet50 in terms of accuracy and loss.

Based on these results, it appears that none of the models achieved high accuracy or low loss in leukemia detection. The performance of the models was limited by the complexity of the task, the available data and computational power. 
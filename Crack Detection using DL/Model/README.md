# Crack Detection using DL

## PROJECT TITLE

Crack Detection using DL

## GOAL

To detect the cracks in the image using Deep learning.

## DATASET

The link for the dataset used in this project: https://www.kaggle.com/competitions/crack-identification-ce784a-2020-iitk/data

## DESCRIPTION

This project aims to identify whether the image contains the cracks or not.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Preprocessed the image in order to have all images in equal shape.
3. Model selection: Chose traditional CNN along with Image detection architecture VGG16 and ResNet50 for Image detection.
4. Comparative analysis: Compared the accuracy score of all the models.

## MODELS USED

1. CNN
2. VGG16
3. ResNet50


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION
##### Cracked Image:
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/43606dbc-0a41-4325-8609-5e52b0df886e)

## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS
##### !!Note: The test directory in the dataset contains unlabelled images only and we have to predict the classes of those images. I have done for one random image for demonstration!!
Results on Train dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.493     | 0.693   |
| VGG16    | 0.887     | 0.222    |
| ResNet50    | 0.495     | 0.693    |


## CONCLUSION
Based on results we can draw following conclusions:
1. CNN model achieved an accuracy of 0.493 and a loss of 0.693. The accuracy is relatively low, indicating that the model has difficulty correctly classifying crack images. The high loss value also suggests that the model's predictions are not accurate.
2. VGG16 model performed better with an accuracy of 0.887 and a loss of 0.222. It outperformed the CNN model in terms of accuracy, indicating that it is more capable of distinguishing crack images. The lower loss value suggests that the VGG16 model's predictions are more accurate.
3. ResNet50 model had a similar performance to the CNN model, with an accuracy of 0.495 and a loss of 0.693. This suggests that ResNet50 is not effective in crack detection and performs similarly to a basic CNN model.

# Scene Classification using DL

## PROJECT TITLE

Scene Classification using DL

## GOAL

To classify the scene in the image from six different classes. 

## DATASET

The link for the dataset used in this project: https://www.kaggle.com/datasets/nitishabharathi/scene-classification

## DESCRIPTION

This project aims to identify six different scenes from the given image which are buildings, forests, mountains, glacier, streets and sea

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
Image Distribution in dataset:

![dist](https://github.com/achrekarom12/DL-Simplified/assets/88442486/c828fa7d-cce4-420e-aa3b-361ff9bf3ca4)



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.833     | 0.451   |
| VGG16    | 0.889     | 0.097    |
| ResNet50    | 0.912     | 0.290    |


## CONCLUSION
Based on results we can draw following conclusions:
1. CNN achieved an accuracy of 0.833 and a loss of 0.451. This model demonstrates good performance in classifying scenes, but there is still room for improvement.
2. VGG16 had a higher accuracy of 0.889 and a very low loss of 0.097 compared to CNN. This suggests that VGG16 is a more powerful model for scene classification and is able to make more accurate predictions.
3. ResNet50 showed the highest accuracy among the models with a value of 0.912 and a moderate loss of 0.290. This indicates that ResNet50 is effective in distinguishing between different scenes and has a good convergence during training.

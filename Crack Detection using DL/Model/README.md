# Crack Detection using DL

## PROJECT TITLE

Crack Detection using DL

## GOAL

To detect the cracks in the image using Deep learning.

## DATASET

The link for the dataset used in this project: https://www.kaggle.com/competitions/crack-identification-ce784a-2020-iitk/data<br>
Alternate dataset you can use: https://www.kaggle.com/datasets/arunrk7/surface-crack-detection

## DESCRIPTION

This project aims to identify whether the image contains the cracks or not.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Preprocessed the image in order to have all images in equal shape.
3. Model selection: Chose traditional CNN along with Image detection architecture VGG16 and ResNet50 for Image detection.
4. Comparative analysis: Compared the accuracy score of all the models.

## MODELS USED

1. VGG16
2. InceptionV3
3. ResNet50


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION
##### Cracked Image:
![positives](https://github.com/achrekarom12/DL-Simplified/assets/88442486/f68744b6-3abe-4d96-8abc-94952f0fbbd0)

##### Uncracked Image:
![negatives](https://github.com/achrekarom12/DL-Simplified/assets/88442486/4d9c0521-851e-4e93-a72b-4d631776e5b9)


## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS
Results on Validation dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| VGG16    | 0.997     | 0.018   |
| InceptionV3    | 0.989     | 0.103    |
| ResNet50    | 0.902     | 0.261    |


## CONCLUSION
Based on the results:
1. VGG16: The VGG16 model achieved high accuracy with an accuracy of 99.7% and a low loss of 0.018. It demonstrates excellent performance in distinguishing between cracked and uncracked images.
2. InceptionV3: The InceptionV3 model also performed well with an accuracy of 98.9% and a relatively low loss of 0.103. It shows good capabilities in crack detection, although slightly lower than VGG16.
3. ResNet50: The ResNet50 model achieved a decent accuracy of 90.2% but with a higher loss of 0.261. It still exhibits reasonable performance in crack detection, although not as accurate as VGG16 and InceptionV3.

Based on these results, we can conclude that VGG16 is the most effective model for crack detection in terms of accuracy and loss. It provides highly accurate predictions on the validation dataset, closely followed by InceptionV3. ResNet50, although not as accurate, still shows potential for crack detection tasks.

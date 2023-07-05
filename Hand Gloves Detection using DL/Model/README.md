# Hand Gloves Detection using DL

## PROJECT TITLE

Hand Gloves Detection using DL

## GOAL

Create a DL model which will detect the gloves.

## DATASET

The dataset used for this project can be found at [link to dataset](https://www.kaggle.com/datasets/dataclusterlabs/gloves-dataset-covid-safety-wear) and [here.](https://www.kaggle.com/datasets/dataclusterlabs/palm-and-gloves-dataset)

## DESCRIPTION

This project aims to identify the hands without gloves and hands with gloves on.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Created a Image generators which helped to generate more images in order to increase the accuracy.
3. Model selection: Chose traditional CNN along with Image detection architecture VGG16, Inception and Xception for Image detection.
4. Comparative analysis: Compared the accuracy score of all the models.

## MODELS USED

1. CNN
2. VGG16
3. Inception
4. Xception


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION
#### Image with gloves on:
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/88077e83-63de-4798-b365-5969a3b09d05)

#### Image without gloves:
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/cb3e0df7-d93d-4508-87cc-9bf815cabaa7)



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss
- Confusion Matrix

## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.903     | 0.49   |
| VGG16    | 0.935     | 0.245    |
| Inception    | 0.892     | 0.222    |
| Xception    | 0.903    | 0.443    |


## CONCLUSION
Based on results we can draw following conclusions:
1. CNN: The CNN model achieved an accuracy of 90.3% and a loss of 0.49. It performed reasonably well in detecting handgloves in the images.

2. VGG16: The VGG16 model outperformed the other models with an accuracy of 93.5% and a lower loss of 0.245. It showed superior performance in detecting handgloves in the images.

3. Inception: The Inception model achieved an accuracy of 89.2% and a loss of 0.222. Although it performed well, it was slightly behind VGG16 in terms of accuracy and loss.

4. Xception: The Xception model achieved an accuracy of 90.3% and a loss of 0.443. It showed comparable performance to the CNN model in terms of accuracy and loss.

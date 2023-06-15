# Human Action Recognition

## PROJECT TITLE

Human Action Recognition

## GOAL

To create a DL model which will identify the actions made by the humans.

## DATASET

The dataset used for this project can be found at [link to dataset](https://www.kaggle.com/datasets/meetnagadia/human-action-recognition-har-dataset). 

## DESCRIPTION

This project aims to identify the human action done in the image. It is trained on the dataset which have various actions and their corresponding labels.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Created a Image generators which helped o generate more images in order to increase the accuracy.
3. Model selection: Chose image detection architecture VGG19, Inception and Xception for action recognition.
4. Comparative analysis: Compared the accuracy score of all the models.

## MODELS USED

1. VGG19
2. Inception
3. Xception


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/3e98f574-b460-494a-9622-ace2d9d8f905)


## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss
- Confusion Matrix

## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| VGG19    | 0.456     | 1.641    |
| Inception    | 0.648     | 1.097    |
| Xception    | 0.664    | 1.099    |

#### Confusion Matrix:
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/56a5958a-4b07-4c7f-9619-cb9e21666292)


## CONCLUSION
Based on results we can draw following conclusions:
1. VGG19: The VGG19 model achieved an accuracy of 0.456 and a loss of 1.641. These results indicate that the model has a relatively low accuracy and high loss, suggesting that it may not be the most effective architecture for this particular task of human action recognition. Further improvements or alternative models should be explored.
2. Inception: The Inception model performed better than VGG19, with an accuracy of 0.648 and a loss of 1.097. These results show a noticeable improvement in accuracy compared to VGG19. The Inception architecture, known for its ability to capture complex patterns and spatial hierarchies, seems to be more suitable for human action recognition.
3. Xception: The Xception model achieved the highest accuracy among the three models, with a value of 0.664, and a loss of 1.099. This indicates that the Xception architecture performs even better than Inception for human action recognition. The Xception model, which is based on an extended version of the Inception architecture, incorporates depthwise separable convolutions to efficiently capture spatial and channel-wise dependencies.

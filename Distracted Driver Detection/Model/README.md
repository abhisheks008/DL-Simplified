# Distracted Driver Detection using DL

## PROJECT TITLE

Distracted Driver Detection using DL

## GOAL

To identify whether the driver driving the vehicle is distracted or not.  

## DATASET

The link for the dataset used in this project:  https://www.kaggle.com/competitions/state-farm-distracted-driver-detection/data

## DESCRIPTION

This project aims to identify the distracted driver while driving a vehicle. These distractions include texting while driving, operating radio or looking at backseat etc.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Preprocessed the images and associated them with their respective labels.
3. Model selection: Chose traditional CNN along with Image detection architecture VGG16, Xception and Inception for Image detection.
4. Comparative analysis: Compared the accuracy score of all the models.

## MODELS USED

1. CNN
2. VGG16
3. Xception
4. Inception


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION
In train data: <br>
![traindist](https://github.com/achrekarom12/DL-Simplified/assets/88442486/bf32b8d5-cc2a-4034-bb0d-f758a33d73e9)

In test data:<br>
![testdist](https://github.com/achrekarom12/DL-Simplified/assets/88442486/f1fd547c-337f-4f73-a9dc-d910a9b388b3)



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.972     | 0.088   |
| VGG16    | 0.845     | 0.48    |
| Xception    | 0.849     | 0.454    |
| Inception    | 0.715     | 0.896    |


## CONCLUSION
Based on results we can draw following conclusions:
1. CNN achieved the highest accuracy of 0.972 with a relatively low loss of 0.088. This indicates that the CNN model performed well in accurately classifying the distracted driver images.
2. VGG16 and Xception achieved moderate accuracies of 0.845 and 0.849, respectively. However, their losses were relatively higher compared to the CNN model. This suggests that these models might have struggled with certain classes or patterns in the dataset.
3. Inception achieved the lowest accuracy of 0.715 with a higher loss of 0.896. This indicates that the Inception model had difficulty capturing the complex features necessary for accurate classification in the Distracted Driver Detection task.

# Cats vs Dogs Audio Classification using DL

## PROJECT TITLE

Cats vs Dogs Audio Classification using DL

## GOAL

To classify the sounds whether its a cat's sound or a dog's sound. 

## DATASET

The link for the dataset used in this project:  https://www.kaggle.com/datasets/mmoreaux/audio-cats-and-dogs

## DESCRIPTION

This project aims to identify the sounds of cats and dogs from the audio files. It is trained on the dataset containing cats and dogs sound.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Preprocessed the audios and created their spectograms in order to make predictions.
3. Model selection: Chose traditional CNN along with Image detection architecture VGG16, ResNet50 and MobileNetV2 for Image detection.
4. Comparative analysis: Compared the accuracy score of all the models.

## MODELS USED

1. CNN
2. VGG16
3. ResNet50
4. MobileNetV2


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION
#### Spectogram for samples:
![spectograms](https://github.com/achrekarom12/DL-Simplified/assets/88442486/60beef49-8cf1-45f8-ab2f-494fdada0eea)



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.94     | 0.203   |
| VGG16    | 0.866     | 0.424    |
| ResNet50    | 0.94     | 0.278    |
| MobileNetV2    | 0.91     | 5.678    |


## CONCLUSION
Based on results we can draw following conclusions:
1. CNN achieved the highest accuracy of 0.94 with a relatively low loss of 0.203. This indicates that the CNN model performed well in distinguishing between cat and dog audio samples.
2. VGG16 achieved an accuracy of 0.866 with a higher loss of 0.424. Although VGG16 performed reasonably well, it showed slightly lower accuracy compared to the CNN model.
3. ResNet50 also achieved a high accuracy of 0.94, similar to the CNN model, but with a slightly higher loss of 0.278. This suggests that ResNet50 was effective in classifying cat and dog audio samples.
4. MobileNetV2 achieved an accuracy of 0.91 but with a significantly higher loss of 5.678. This indicates that the MobileNetV2 model struggled to learn the patterns and features necessary for accurate classification.

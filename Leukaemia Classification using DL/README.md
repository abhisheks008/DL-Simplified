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

1. VGG16
2. ResNet50
3. Inception
4. Xception
5. CNN


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION
![demo2](https://github.com/achrekarom12/DL-Simplified/assets/88442486/4211b013-4b30-40f5-9b97-408e92cd479b)



## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS

Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| Inception    | 0.775     | 0.498   |
| ResNet50    | 0.802     | 0.514    |
| VGG16    | 0.77     | 0.536    |
| CNN    | 0.784     | 0.506    |
| Xception    | 0.783     | 0.533    |


## CONCLUSION
Based on results we can draw following conclusions:
1. Inception: The Inception model achieved an accuracy of 77.5% with a loss of 0.498. It demonstrates good performance in distinguishing between leukemia and non-leukemia samples.
2. ResNet50: The ResNet50 model performed slightly better with an accuracy of 80.2% and a loss of 0.514. It shows improved capabilities compared to Inception in leukemia detection.
3. VGG16: The VGG16 model achieved an accuracy of 77.0% with a loss of 0.536. It falls slightly behind ResNet50 in terms of accuracy and loss.
4. CNN: The CNN model achieved an accuracy of 78.4% with a loss of 0.506. It demonstrates similar performance to ResNet50 and shows potential in leukemia detection.
5. Xception: The Xception model achieved an accuracy of 78.3% with a loss of 0.533. It shows comparable performance to the other models in this task.
Overall, all the models performed relatively well in leukemia detection, with accuracies ranging from 77% to 80.2%.  

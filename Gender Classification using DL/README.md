# Gender Classification using DL 

## PROJECT TITLE

Gender Classification using DL 

## GOAL

To identify whether the given face is masculine or feminine. 

## DATASET

The link for the dataset used in this project:  https://www.kaggle.com/datasets/cashutosh/gender-classification-dataset 


## DESCRIPTION

This project aims to identify whether the given face is masculine or feminine by extracting facial features.

## WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 
2. Data preprocessing: Preprocessed the images and did some augementation before passing them to model training
3. Model selection: Chose VGG16, ResNet50, Inception and MobileNet
4. Comparative analysis: Compared the accuracy score of all the models.

## MODELS USED

1. VGG16
2. ResNet50
3. Inception
4. MobileNet


## LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## VISUALIZATION
![comparision](https://github.com/achrekarom12/DL-Simplified/assets/88442486/5cb0b74c-4220-4c87-8940-572b200b533b)


## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| VGG16    | 0.914     | 0.212   |
| ResNet50    | 0.689     | 0.669    |
| Inception    | 0.926     | 0.188    |
| MobileNet    | 0.913     | 0.222    |


## CONCLUSION
Based on results we can draw following conclusions:
1. The VGG16 model achieved an accuracy of 91.4% and a loss of 0.212. It demonstrated high accuracy, indicating that it was able to effectively distinguish between male and female faces. The relatively low loss value further supports its strong performance.

2. The ResNet50 model, on the other hand, achieved an accuracy of 68.9% and a loss of 0.669. These results indicate that the model struggled to accurately classify male and female faces, as the accuracy is significantly lower compared to other models. The relatively high loss value suggests that the model had difficulty in learning the underlying patterns and features associated with gender classification.

3. The Inception model performed well with an accuracy of 92.6% and a loss of 0.188. It demonstrated excellent accuracy and relatively low loss, showcasing its ability to effectively identify the gender of faces in the dataset.

4. The MobileNet model achieved an accuracy of 91.3% and a loss of 0.222. It performed similarly to the VGG16 model, indicating that it was capable of accurately classifying male and female faces with high accuracy and relatively low loss.

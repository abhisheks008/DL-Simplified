# Chocolate Classification using DL

## PROJECT TITLE

Chocolate Classification using DL

## GOAL

To classify chocolate in the image either as normal chocolate or white chocolate. 

## DATASET

The link for the dataset used in this project: https://www.kaggle.com/datasets/siddharthmandgi/chocolate-classification

## DESCRIPTION

This project aims to identify the white chocolate and dark chocolate in the image. It is trained on the dataset containing images of white chocolate and dark chocolate.

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
![acc_cnn](https://github.com/achrekarom12/DL-Simplified/assets/88442486/877a80a9-fc57-4b27-9565-51bd5eb1c12a) ![acc_resnet50](https://github.com/achrekarom12/DL-Simplified/assets/88442486/7a747369-2666-4a94-bbe4-9cdd8c9afe21) ![acc_vgg16](https://github.com/achrekarom12/DL-Simplified/assets/88442486/ccef084d-e219-4890-a1af-91b2f832a38e)


## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.861     | 0.218   |
| VGG16    | 0.722     | 1.341    |
| ResNet50    | 0.917     | 0.251    |


## CONCLUSION
Based on results we can draw following conclusions:
1. CNN achieved the highest accuracy (0.861) and a relatively low loss (0.218). This model demonstrates good performance in distinguishing between dark and white chocolate images.
2. VGG16 had a lower accuracy (0.722) compared to CNN, indicating that it might not be the most suitable model for this specific chocolate detection task. However, it is still capable of making predictions.
3. ResNet50 showed the highest accuracy (0.917) among the models, suggesting its effectiveness in differentiating between dark and white chocolate images. Additionally, it had a low loss value (0.251), signifying good convergence during training.

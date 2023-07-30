# Cats vs Dogs Classification using DL

## PROJECT TITLE

Cats vs Dogs Classification using DL

## GOAL

Create a DL model which will identify the Cats and Dogs. 

## DATASET

The link for the dataset used in this project: https://www.kaggle.com/datasets/samuelcortinhas/cats-and-dogs-image-classification and https://www.kaggle.com/datasets/tongpython/cat-and-dog

## DESCRIPTION

This project aims to identify the cats and dogs in the image. It is trained on the dataset containing cats and dogs.

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
#### Best performing model accuracy:
![val_acc3](https://github.com/achrekarom12/DL-Simplified/assets/88442486/b48589ab-83e6-4ce7-86df-eebdbe35921f)

#### Best performing model loss:
![val_loss3](https://github.com/achrekarom12/DL-Simplified/assets/88442486/55072c0f-1fdb-433a-87be-c442c25d84a7)


## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss


## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.728     | 1.159   |
| VGG16    | 0.925     | 0.218    |
| ResNet50    | 0.735     | 1.688    |


## CONCLUSION
Based on results we can draw following conclusions:
1. CNN: The CNN model achieved an accuracy of 0.728 and a loss of 1.159. It performed reasonably well, but there is room for improvement.
2. VGG16: The VGG16 model achieved a higher accuracy of 0.925 and a lower loss of 0.218. It outperformed the basic CNN model, indicating that the deeper architecture of VGG16 with more trainable parameters was able to capture more complex features and generalize better.
3. ResNet50: The ResNet50 model achieved an accuracy of 0.735 and a loss of 1.688. It performed slightly better than the basic CNN model but was outperformed by VGG16. ResNet50's residual connections helped in mitigating the vanishing gradient problem and allowed for the training of deeper networks.

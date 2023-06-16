# Human Detection Project

## PROJECT TITLE

Human Detection Project

## GOAL

To create a DL model which will identify the humans in given image.

## DATASET

The dataset used for this project can be found at [link to dataset](https://www.kaggle.com/datasets/constantinwerner/human-detection-dataset). 

## DESCRIPTION

This project aims to identify the humans in the image. It is trained on the dataset containing CCTV footage images(as indoor as outdoor).

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
#### Image with humans
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/88c70bb4-c99f-400d-ad27-34f72df2f809)

#### Image without humans
![image](https://github.com/achrekarom12/DL-Simplified/assets/88442486/fcb2d038-7aad-4603-a86b-3f1189a490b2)




## EVALUATION METRICS

The evaluation metrics I used to assess the models:

- Accuracy 
- Loss
- Confusion Matrix

## RESULTS
Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.756     | 0.591   |
| VGG16    | 0.859     | 0.304    |
| Inception    | 0.886     | 0.33    |
| Xception    | 0.843    | 0.481    |
| Fine-tuned Inception    | 0.902    | 0.312    |


## CONCLUSION
Based on results we can draw following conclusions:
1. CNN Model: The CNN model achieved an accuracy of 75.6% and a loss of 0.591. While it demonstrates reasonable performance, there is room for improvement compared to the other models.

2. VGG16 Model: The VGG16 model outperformed the CNN model with an accuracy of 85.9% and a lower loss of 0.304. It shows the effectiveness of using a pre-trained model like VGG16 for human detection, achieving a higher accuracy and lower loss than the CNN model.

3. Inception Model: The Inception model achieved an accuracy of 88.6% and a loss of 0.33. It performs well, with a higher accuracy than both the CNN and VGG16 models. This suggests that the Inception architecture is effective in capturing human features and distinguishing them from non-human objects.

4. Xception Model: The Xception model achieved an accuracy of 84.3% and a loss of 0.481. While it performs decently, it is slightly behind the VGG16 and Inception models in terms of accuracy.

5. Fine-tuned Inception: The fine-tuned Inception model showed further improvement with an accuracy of 90.2% and a loss of 0.312. Fine-tuning the Inception model likely helped to adapt it more specifically to the task of human image detection, resulting in increased accuracy.

# Leukaemia Classification using DL

## PROJECT TITLE

Leukaemia Classification using DL

## 🎯 GOAL

To classify normal from abnormal cell images of Leukaemia.

## 🧵 DATASET

The link for the dataset used in this project: https://www.kaggle.com/datasets/andrewmvd/leukemia-classification

## 🧾 DESCRIPTION

This project aims to identify whether the given medical image contains Leukaemia cells or not.

## 🧮 WHAT I HAD DONE

1. Data collection: From the link of the dataset given above. 

2. Data preprocessing: Preprocessed the image in order to have all images in equal shape.

3. Model selection: Chose three Image detection architecture VGG16, ResNet50 and Inception for Image detection. Created models for CNN and CNN with Attention mechanism.

4. Comparative analysis: Compared the accuracy score of all the models.

## 🚀 MODELS USED

1. VGG16
2. ResNet50
3. Inception
4. Xception
5. CNN
6. CNN with Attention

## 📚 LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## 🖼️ VISUALIZATION

![demo 1](https://github.com/abhisheks008/DL-Simplified/blob/main/Leukaemia%20Classification%20using%20DL/Images/demo1.png)

![demo 2](https://github.com/abhisheks008/DL-Simplified/blob/main/Leukaemia%20Classification%20using%20DL/Images/demo2.png)

![demo 3](https://github.com/abhisheks008/DL-Simplified/blob/main/Leukaemia%20Classification%20using%20DL/Images/demo3.png)

![Inception](https://github.com/abhisheks008/DL-Simplified/blob/main/Leukaemia%20Classification%20using%20DL/Images/inception.png)

![RESNET50](https://github.com/abhisheks008/DL-Simplified/blob/main/Leukaemia%20Classification%20using%20DL/Images/resnet50.png)

![VGG16](https://github.com/abhisheks008/DL-Simplified/blob/main/Leukaemia%20Classification%20using%20DL/Images/vgg16.png)

![CNN](https://github.com/abhisheks008/DL-Simplified/blob/main/Leukaemia%20Classification%20using%20DL/Images/cnn.png)

![Xception](https://github.com/abhisheks008/DL-Simplified/blob/main/Leukaemia%20Classification%20using%20DL/Images/exception.png)

![CNN-Attention](https://github.com/Arihant-Bhandari/DL-Simplified/blob/enhance_cancer_classify/Leukaemia%20Classification%20using%20DL/Images/CNN-Attention.png)

## 📋 EVALUATION METRICS

The evaluation metrics used for assessing the models:

- Accuracy 
- Loss

## 📈 RESULTS

Results on Val dataset:

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| Inception    | 0.775     | 0.498   |
| ResNet50    | 0.802     | 0.514    |
| VGG16    | 0.77     | 0.536    |
| CNN    | 0.784     | 0.506    |
| Xception    | 0.783     | 0.533    |
| CNN (Attention)    | 0.858     | 0.39    |

## 📢 CONCLUSION

Based on results we can draw following conclusions:

1. Inception: The Inception model achieved an accuracy of 77.5% with a loss of 0.498. It demonstrates good performance in distinguishing between leukemia and non-leukemia samples.

2. ResNet50: The ResNet50 model performed slightly better with an accuracy of 80.2% and a loss of 0.514. It shows improved capabilities compared to Inception in leukemia detection.

3. VGG16: The VGG16 model achieved an accuracy of 77.0% with a loss of 0.536. It falls slightly behind ResNet50 in terms of accuracy and loss.

4. CNN: The CNN model achieved an accuracy of 78.4% with a loss of 0.506. It demonstrates similar performance to ResNet50 and shows potential in leukemia detection.

5. Xception: The Xception model achieved an accuracy of 78.3% with a loss of 0.533. It shows comparable performance to the other models in this task.

6. CNN with Attention: The CNN with Attention mechanism model achieved an astonishingly high accuracy of 85.8% with a significantly lower loss of 0.39. It demonstrates exceptional abilities to generalize and classify with a simple and lightweight architecture.

Overall, all the models performed relatively well in leukemia detection, with accuracies ranging from 77% to 85.8%, with CNN-Attention being the clear winner.  

## YOUR SIGNATURE

Model and README enhanced by: Arihant Bhandari[https://github.com/Arihant-Bhandari]
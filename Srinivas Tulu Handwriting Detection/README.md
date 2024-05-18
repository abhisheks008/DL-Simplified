# Srinivas Tulu Handwriting Detection

## 🎯 Goal

The primary objective of this project is to perform image classification using pre trained models. These models are trained to categorize images into 50 classes(total number of characters in Tulu Language).

## 🖼️ Dataset

The dataset includes various handwritten forms of Tulu script, covering a wide range of characters used in the Tulu language. Each sample is labeled with the corresponding Tulu character, enabling applications such as machine learning models for character classification and language analysis.

**Dataset Link**: [Srinivas Tulu Handwriting Dataset](https://www.kaggle.com/datasets/midhun009/tulu-handwritten-dataset)

## 🧾 Description

This project utilizes 3 transfer learning models EfficientNet, DenseNet and InceptionNet for image classification. The pre-trained models leverage transfer learning, enhancing the model's ability to generalize across diverse images.

## 🧮 What I Had Done

1. **Data Preprocessing**:
   - Resizing images to match the input size (128x128 pixels for pretrained models).

2. **Model Architectures**:
   - EfficientNet: Leveraging the pretrained EfficientNet model.
   - InceptionNet: Utilizing the pretrained model with version V2.
   - DenseNet: Leveraging the powerful DenseNet model.

3. **Model Training**:
   - Training the models over the image dataset.
   - Evaluating the models on the validation set to monitor performance.

4. **Plotting Accuracy**
   - Plotted accuracy and loss vs epochs for each model for better understanding of model perfomance.

###  Libraries and Frameworks used:
1. Pandas
2. Numpy 
3. Matplotlib
4. Seaborn
5. Tensorflow
6. Keras
7. sklearn
8. glob
9. OpenCV

## Deep Learning Algorithms used:
1. DenseNet
2. InceptionNet
3. EfficientNet

## Accuracy and training time comparison of all the Deep Learning Algorithms
|                    |   Accuracy    |
|--------------------|---------------|
|    EfficientNet    |     76%       |  
|     DenseNet       |     97%       |
|    InceptionNet    |     87%       |

# Representation of different Tulu characters
![EDA](https://github.com/the-silent-geek/DL-Simplified/blob/cda670485339d1659afe3d400e639e51d145db3d/Srinivas%20Tulu%20Handwriting%20Detection/images/EDA.png)

# Accuracy and plots of all models

## InceptionNetV2
![inv2](https://github.com/the-silent-geek/DL-Simplified/blob/cda670485339d1659afe3d400e639e51d145db3d/Srinivas%20Tulu%20Handwriting%20Detection/images/inceptionNet.png)

## DenseNet
![densenet](https://github.com/the-silent-geek/DL-Simplified/blob/cda670485339d1659afe3d400e639e51d145db3d/Srinivas%20Tulu%20Handwriting%20Detection/images/DenseNet.png)

## EfficientNet
![effnet](https://github.com/the-silent-geek/DL-Simplified/blob/cda670485339d1659afe3d400e639e51d145db3d/Srinivas%20Tulu%20Handwriting%20Detection/images/effnet.png)


# Conclusion
DenseNet model performs better comparative to other models used on the above dataset.
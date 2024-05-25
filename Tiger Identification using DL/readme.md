# Tiger Identification Project Using Deep Learning

## 🎯 Goal
The main goal of this project is to develop and evaluate deep learning models for the accurate re-identification (Re-ID) of individual tigers from images. 

## Purpose
The purpose of this project is to facilitate wildlife conservation efforts by enabling researchers to track and monitor individual tigers in their natural habitats. By accurately identifying tigers from images, this system helps in managing and protecting tiger populations, thus contributing to their conservation and study.

## 🧵 Dataset
link : https://www.kaggle.com/datasets/quadeer15sh/amur-tiger-reidentification

## 🧾 Description
This project focuses on the development of a tiger re-identification (Re-ID) system using deep learning techniques. The system leverages advanced convolutional neural network architectures, including DenseNet, VGG16, ResNet50, and EfficientNet, to identify and distinguish individual tigers from a collection of images. The dataset consists of cropped photos annotated with keypoints and unique IDs, facilitating the training and evaluation of the models.

In the Re-ID task, models are trained on a training set and tested on a separate test set. During testing, each image is treated as a query image, and the system generates a ranked list of matching images from the gallery. This project aims to enhance the accuracy of tiger identification, thereby aiding in wildlife conservation efforts by enabling better monitoring and management of tiger populations.

## 🧮 What I had done!
1) Dataset Preparation
The dataset comprises images of tigers, categorized into 107 classes, with each class containing a varying number of images.
To balance the dataset, we adjusted the number of images per class to 100.

2) Data Augmentation
Applied data augmentation techniques to enhance the dataset and improve model robustness. The ImageDataGenerator was configured as follows:
```python
trgen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)
```
4) Visualization
Visualized the augmented images to ensure the transformations were applied correctly and to gain insights into the data distribution.

5) Model Training
Trained the balanced and augmented dataset using four deep learning architectures:
- VGG16
- ResNet50
- DenseNet
- EfficientNet

5) Evaluation
Evaluated the trained models using the test set.
Generated classification reports and plotted accuracy graphs to assess and compare the performance of each model.

## 🚀 Models Implemented
1) DenseNet (Dense Convolutional Network)
*Reason:* DenseNet features dense connections between layers, allowing for better feature propagation and reuse. This architecture mitigates the vanishing gradient problem and requires fewer parameters compared to traditional convolutional networks, which makes it efficient for image recognition tasks.

2) VGG16 (Visual Geometry Group Network)
*Reason:* VGG16 is renowned for its simplicity and effectiveness. With its deep architecture consisting of 16 layers, it has demonstrated high performance in image classification tasks. Its straightforward design makes it a strong baseline model for comparison.

3) ResNet50 (Residual Network)
*Reason:* ResNet50 introduces residual connections, which help in training deeper networks by solving the vanishing gradient problem. This model has proven to be highly effective in various image recognition challenges, making it a reliable choice for the Re-ID task.

4) EfficientNet
*Reason:* EfficientNet optimizes both the depth, width, and resolution of the network, providing a balanced approach to scaling. This model achieves state-of-the-art accuracy with fewer parameters and computations, making it highly suitable for large-scale image classification problems like tiger re-identification.

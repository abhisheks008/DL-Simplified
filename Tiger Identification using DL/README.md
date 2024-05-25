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

## 📚 Libraries Needed
- TensorFlow
- Keras
- NumPy
- Pandas
- OpenCV (cv2)
- Matplotlib
- scikit-learn
- ImageDataGenerator from Keras

## 📊 Exploratory Data Analysis Results
To understand the distribution of images across the 107 classes, we visualized the number of images per class before and after balancing the dataset.

- Before Balancing: The dataset had a varied number of images per class, which could lead to biased training.

- After Balancing: We balanced the dataset by ensuring each class had 100 images, thus providing a uniform distribution.

![Screenshot 2024-05-25 121645](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/8057720f-f986-48f5-b252-9fa10e1c9b64)

## 📈 Performance of the Models based on the Accuracy Scores

### Resnet50 results
![ResNet50_results](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/8ee58d18-4461-4d88-9d13-b4baa72d7b11)


### VGG16 results
![VGG16_results](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/ed38a55f-c892-47db-b451-538a2e8f08f9)


### EfficientNet results
![EfficientNetB3_results](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/4b607a9d-e450-45c1-a249-5ac939eca7ed)


## DenseNet results
![DenseNet_results](https://github.com/jeet-Abhi123/Road-Safety-Data-Analysis-Power-BI-/assets/143840497/9ced2d4d-f538-4d6c-a826-ae5c0bbb2da9)


## 📢 Conclusion
The project successfully developed and evaluated deep learning models for tiger re-identification. By using architectures such as DenseNet, VGG16, ResNet50, and EfficientNet, we aimed to identify and distinguish individual tigers from a set of images. The models were trained and tested, with their performances compared based on accuracy scores.

### Accuracy Results
1) EfficientNetB3
- Epoch 1: Accuracy: 64.90%, Validation Accuracy: 91.01%
- Epoch 10: Accuracy: 99.22%, Validation Accuracy: 95.77%
- Best Validation Accuracy: 97.35%

2) DenseNet
- Epoch 1: Accuracy: 58.21%, Validation Accuracy: 86.24%
- Epoch 10: Accuracy: 99.03%, Validation Accuracy: 96.30%
- Best Validation Accuracy: 96.30%

3) VGG16
- Epoch 1: Accuracy: 3.29%, Validation Accuracy: 6.88%
- Epoch 10: Accuracy: 55.93%, Validation Accuracy: 61.90%
- Best Validation Accuracy: 61.90%

4) ResNet50
- Epoch 1: Accuracy: 59.09%, Validation Accuracy: 79.37%
- Epoch 10: Accuracy: 97.93%, Validation Accuracy: 96.83%
- Best Validation Accuracy: 97.35%

### Best Fitted Model
Based on the validation accuracy results, EfficientNetB3 emerged as the best-fitted model for this tiger re-identification project, achieving the highest validation accuracy of 97.35%.

EfficientNetB3's balanced approach to scaling network dimensions contributed to its superior performance, demonstrating its effectiveness in handling the complexities of the tiger Re-ID task.

## ✒️ Contributor

### Name : Abhijeet Kaithwas
LinkedIn profile : https://www.linkedin.com/in/abhijeet-kaithwas-1866b5256/







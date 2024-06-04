## **Indonesian Spice Classification using DL**

### 🎯 **Goal**

The objective of this project is to classify images of Indonesian Spices into 31 categories.

### 🧵 **Dataset**

The dataset consists of 31 subdirectories under Indonesian Spices Dataset, with all images having .jpg extension. Working images under tensorflow(.jpeg, .jpg, .png, .bmp, .gif) total less than 6000. Images can be turned to eligible format from .webp.

### 🧾 **Description**

The project deals with multi-class classification, classifying images into 31 classes of Indonesian Spices.

### 🧮 **What I had done!**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

- Labels were turned into probability distributions from numerical representation.

- Images were resized to a fixed size of 224x224 pixels.

- Custom and pre-trained models were used for this task.

### 🚀 **Models Implemented**

models used:

- ResNet-50
- Xception
- VGG16
- CNN-Keras
- InceptionV3
- DenseNet-121
- EfficientNetB7

### 📚 **Libraries Needed**

- Keras

- Tensorflow

- Numpy

- Matplotlib

### 📊 **Exploratory Data Analysis Results**


- #### **Exploratory Data Analysis**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/biji%20ketumber.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/duan%20jeruk.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/jinten.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/kayu%20secang.png" height="400px" width="400px" />
</p>

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/Inception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/Inception%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/VGG16%20Loss.png" height="400px" width="400px" />
</p>

- #### **EfficientNetB7**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/EfficientNetB7%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/EfficientNetB7%20Loss.png" height="400px" width="400px" />
</p>

- #### **RESNET50**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/RESNET50%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/RESNET50%20Loss.png" height="400px" width="400px" />
</p>

- #### **DenseNet-121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/DENSENET121%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/DENSENET121%20Loss.png" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/Xception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/indonesian-spices/Indonesian%20Spice%20Classification%20using%20DL/Images/Xception%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation and Testing **Loss** and **Accuracy** as metrics.

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| ResNet-50 | 2.92% | 15.6477 |
| InceptionV3 | 85.64%  | 0.5840 | 
| CNN | 77.88% | 0.9821 |
| VGG16 | 87.25% | 0.5719 |
| EfficientNetB7 | 3.53% | 3.4381 |
| DenseNet-121 | 92.17% | 0.2818 |
| Xception | 88.86% | 0.4359 |

### 📢 **Conclusion**

We conclude the following:



### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
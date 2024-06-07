## **Turkey Almond Species Classification using DL**

### 🎯 **Goal**

The objective of this project is to classify images of almonds from various regions into four distinct varieties of Turkic almond species.

### 🧵 **Dataset**

The dataset consists of 4 subdirectories under the main Dataset directory: AK(401 images), KAPADOKYA(465 images), NURLU(306 images) and SIRA(384 images). The Dataset hence can be summarized as: 1556 images of the four varieties.

### 🧾 **Description**

The project deals with multi-class classification, classifying images into 4 classes of Turkey's indigenous almond species.

### 🧮 **What I had done!**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

- Images were resized to a fixed size of 224x224 pixels.

- Labels were converted from numerical to probability distribution representations.

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

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/ALMOND.png">

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/EDA.png">

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/InceptionV3%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/InceptionV3%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/VGG16%20Loss.png" height="400px" width="400px" />
</p>

- #### **EfficientNetB7**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/EfficientNetB7%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/EfficientNetB7%20Loss.png" height="400px" width="400px" />
</p>

- #### **RESNET50**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/RESNET50%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/RESNET50%20Loss.png" height="400px" width="400px" />
</p>

- #### **DenseNet-121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/DENSENET121%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/DENSENET121%20Loss.png" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/Xception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/almond/Turkey%20Almond%20Species%20Classification%20using%20DL/Images/Xception%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation and Testing **Loss** and **Accuracy** as metrics.

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| ResNet-50 | 29.81% | 11.3137 |
| InceptionV3 | 96.47%  | 0.1521 | 
| CNN | 95.51% | 0.1550 |
| VGG16 | 97.76% | 0.0680 |
| EfficientNetB7 | 29.81% | 1.3967 |
| DenseNet-121 | 98.72% | 0.0624 |
| Xception | 97.44% | 0.0794 |

### 📢 **Conclusion**

We conclude the following:

**DenseNet-121**, **Xception**, **VGG16**, **InceptionV3** and **CNN** work exceptionally well, with **DenseNet-121** being the clear winner.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
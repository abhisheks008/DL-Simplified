## **Cats Breed Classification using DL**

### 🎯 **Goal**

The objective of this project is to classify images of cats into 5 breeds, namely, siamese, ragdoll, bengal, domestic shorthair and maine coon.

### 🧵 **Dataset**

The dataset consists of 5 subdirectories: siamese, ragdoll, bengal, domestic_shorthair and maine_coon under cat_v1 directory, totalling to 951 images.

### 🧾 **Description**

The project deals with multi-class classification, classifying images into 5 classes.

### 🧮 **What I had done!**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

- Labels were loaded and one-hot encoded into probability distributions.

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
- MobileNet
- NASNetMobile

### 📚 **Libraries Needed**

- Keras

- Tensorflow

- Numpy

- Matplotlib

### 📊 **Exploratory Data Analysis Results**


- #### **Exploratory Data Analysis**

<p align="center">
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
</p>

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/EDA.png">

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/InceptionV3%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/InceptionV3%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/VGG16%20Loss.png" height="400px" width="400px" />
</p>

- #### **MobileNet**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/MobileNet%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/MobileNet%20Loss.png" height="400px" width="400px" />
</p>

- #### **RESNET50**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/RESNET50%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/RESNET50%20Loss.png" height="400px" width="400px" />
</p>

- #### **DenseNet-121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/DenseNet121%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/DenseNet121%20Loss.png" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/Xception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/Xception%20Loss.png" height="400px" width="400px" />
</p>

- #### **NASNetMobile**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/NASNetMobile%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cat-classify/Cats%20Breed%20Classification%20using%20DL/Images/NASNetMobile%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation **Loss** and **Accuracy** as metrics.

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| ResNet-50 | 22.66% | 12.4663 |
| InceptionV3 | 83.59%  | 0.4896 | 
| CNN | 35.94% | 2.2302 |
| VGG16 | 78.12% | 0.6243 |
| MobileNet | 88.28% | 0.4559 |
| DenseNet-121 | 85.16% | 0.5082 |
| Xception | 82.81% | 0.4810 |
| NASNetMobile | 87.50% | 0.4133 |

### 📢 **Conclusion**

We conclude the following:

**NASNetMobile**, **Xception**, **MobileNet** and **DenseNet-121** work exceptionally on given task.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
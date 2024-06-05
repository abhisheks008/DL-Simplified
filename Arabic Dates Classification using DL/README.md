## **Speech Sentiment Analysis using DL**

### 🎯 **Goal**

The objective of this project is to classify images of Arabic Dates into 9 species from the Arabic region.

### 🧵 **Dataset**

The dataset consists of 9 subdirectories: each containing approximately 175 images totalling to 1658 images.

### 🧾 **Description**

The project deals with multi-class classification, classifying images of Arabic Dates into 9 species.

### 🧮 **What I had done!**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

- Turn Labels from numerical to probability distribution representation.

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

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/display.png"/>

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/EDA.png"/>

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/pie%20distribution.png"/>

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/InceptionV3%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/InceptionV3%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/VGG16%20Loss.png" height="400px" width="400px" />
</p>

- #### **EfficientNetB7**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/EfficientNetB7%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/EfficientNetB7%20Loss.png" height="400px" width="400px" />
</p>

- #### **RESNET50**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/RESNET50%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/RESNET50%20Loss.png" height="400px" width="400px" />
</p>

- #### **DenseNet-121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/DenseNet121%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/DenseNet121%20Loss.png" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/Xception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/dates-classify/Arabic%20Dates%20Classification%20using%20DL/Images/Xception%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation **Loss** and **Accuracy** as metrics.

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| ResNet-50 | 12.05% | 14.1762 |
| InceptionV3 | 90.36%  | 0.3815 | 
| CNN | 83.13% | 0.7560 |
| VGG16 | 97.29% | 0.1368 |
| EfficientNetB7 | 18.37% | 2.1760 |
| DenseNet-121 | 96.99% | 0.1515 |
| Xception | 94.58% | 0.1908 |

### 📢 **Conclusion**

We conclude the following:

VGG16, DenseNet-121, InceptionV3 and CNN work exceptionally well, with **VGG16** and **DenseNet-121** being the ideal choice.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
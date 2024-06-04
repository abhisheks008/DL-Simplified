## **Rock Formation Classification using DL**

### 🎯 **Goal**

The objective of this project is to classify images of Rock formations into 3 types: Igneous, Sedimentary and Metamorphic.

### 🧵 **Dataset**

The dataset consists of 3 directories: Igneous, Sedimentary and Metamorphic, with approximately 3400 images each, totalling 10400 images in entirety.

we consider 7500 images in total for our model.

### 🧾 **Description**

The project deals with multi-class classification, classifying rocks into 3 categories: Igneous, Sedimentary and Metamorphic.

### 🧮 **What I had done!**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

- Images were resized to a fixed size of 224x224 pixels.

- Limited images from 10000 to 7500.

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

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/EDA.png">

<br>

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/Igneous.png" height="400px" width="250px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/Metamorphic.png" height="400px" width="250px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/Sedimentary.png" height="400px" width="250px" />
</p>

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/InceptionV3%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/InceptionV3%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/VGG16%20Loss.png" height="400px" width="400px" />
</p>

- #### **EfficientNetB7**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/EfficientNetB7%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/EfficientNetB7%20Loss.png" height="400px" width="400px" />
</p>

- #### **RESNET50**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/RESNET50%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/RESNET50%20Loss.png" height="400px" width="400px" />
</p>

- #### **DenseNet-121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/DENSENET121%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/DENSENET121%20Loss.png" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/Xception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/rocks-classify/Rock%20Formation%20Classification%20using%20DL/Images/Xception%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation **Loss** and **Accuracy** as metrics.

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| ResNet-50 | 27.73% | 11.6480 |
| InceptionV3 | 56.09%  | 0.9833 | 
| CNN | 54.76% | 0.9459 |
| VGG16 | 59.73% | 0.9362 |
| EfficientNetB7 | 37.51% | 1.0937 |
| DenseNet-121 | 61.87% | 0.8813 |
| Xception | 58.76% | 0.9247 |

### 📢 **Conclusion**

We conclude the following:

VGG16, Inception, Xception and DenseNet-121 work well, with CNN falling just a bit short. DenseNet-121 proved to be the better choice amongst all.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
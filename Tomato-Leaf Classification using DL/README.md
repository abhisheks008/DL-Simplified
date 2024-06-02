## **Tomato-Leaf Classification using DL**

### 🎯 **Goal**

The objective of this project is to classify images of Tomato leaves into 10 distinct categories based on type and level of illness as well as healthy.

### 🧵 **Dataset**

The dataset consists of two subdirectories: train and val. Both train and val contain 10 subdirectories, each representing a category of leaf images. The train subdirectory contains 1000 images per category, while the val subdirectory contains 100 images per category.

### 🧾 **Description**

The project deals with multi-class classification, classifying images into 10 classes.

### 🧮 **What I had done!**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

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

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/EDA-1.png">
<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/eda.png">

<br>

<p align="center">
  <figure>
    <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/healthy%20leaf.png" height="400px" width="400px" alt="healthy tomato leaf" />
    <figcaption>Healthy Tomato Leaf</figcaption>
  </figure>
  <br>
  <figure>
    <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/diseased%20leaf.png" height="400px" width="400px" alt="diseased tomato leaf" />
    <figcaption>Diseased Tomato Leaf</figcaption>
  </figure>
</p>

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/Inception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/Inception%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/VGG16%20loss.png" height="400px" width="400px" />
</p>

- #### **EfficientNetB7**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/EfficientNet%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/EfficientNet%20Loss.png" height="400px" width="400px" />
</p>

- #### **RESNET50**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/RESNET50%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/RESNET50%20Loss.png" height="400px" width="400px" />
</p>

- #### **DenseNet-121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/DenseNet121%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/DenseNet121%20Loss.png" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/Xception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/Xception%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation and Testing **Loss** and **Accuracy** as metrics.

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| ResNet-50 | 10.00% | 14.5063 |
| InceptionV3 | 84.30%  | 0.5310 | 
| CNN | 98.00% | 0.0657 |
| VGG16 | 92.70% | 0.2489 |
| EfficientNetB7 | 10.00% | 2.3026 |
| DenseNet-121 | 93.60% | 0.1880 |
| Xception | 88.90% | 0.3858 |

### 📢 **Conclusion**

We conclude the following:

Pre-trained models like **DenseNet-121** and **VGG16** worked well. **CNN** was the clear winner owing to its significantly higher accuracy and minimal loss as well as its minimal architecture.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
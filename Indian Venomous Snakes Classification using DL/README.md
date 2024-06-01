## **Indian Venomous Snakes Classification using DL**

### 🎯 **Goal**

The objective of this project is to classify images of snakes as either venomous or non-venomous to identify dangerous snakes in Indian wildlife.

### 🧵 **Dataset**

The dataset consists of two subdirectories: train and test. Furthermore, the train directory has two subdirectories named Venomous and Non-Venomous with 1060 and 715 images, respectively.

### 🧾 **Description**

The project deals with binary classification, classifying images into the two classes: Venomous or Non-Venomous

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

### 📚 **Libraries Needed**

- Keras

- Tensorflow

- Numpy

- Matplotlib

### 📊 **Exploratory Data Analysis Results**


- #### **Venomous**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/ven1.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/ven2.png" height="400px" width="400px" />
</p>

- #### **Non Venomous**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/NV1.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/NV2.png" height="400px" width="400px" />
</p>

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/InceptionV3%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/InceptionV3%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/VGG16%20Loss.png" height="400px" width="400px" />
</p>

- #### **EfficientNetB7**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/EfficientNetB7%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/EfficientNetB7%20Loss.png" height="400px" width="400px" />
</p>

- #### **RESNET50**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/RESNET50%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/snake_classify/Indian%20Venomous%20Snakes%20Classification%20using%20DL/Images/RESNET50%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation and Testing **Loss** and **Accuracy** as metrics.

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| ResNet-50 | 65.17% | 0.6405 |
| InceptionV3 | 86.89%  | 0.3523 | 
| CNN | 74.44% | 0.5768 |
| VGG16 | 75.28% | 0.5027 |
| EfficientNetB7 | 60.67% | 0.6833 |

### 📢 **Conclusion**

We conclude the following:

InceptionV3 and VGG16 work well on the dataset, while the custom CNN, being much lighter, falls just a bit short.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
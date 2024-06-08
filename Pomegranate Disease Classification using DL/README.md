## **Pomegranate Disease Classification using DL**

### 🎯 **Goal**

The objective of this project is to classify images of pomegranates into  classes, namely: Alternaria, Anthracnose, Bacterial_Blight, Cercospora, and Healthy.

### 🧵 **Dataset**

The dataset contains 5 subdirectories, each corresponding to 4 different diseases and normal images of pomegranates, totaling to approximately 5100 images.

### 🧾 **Description**

The project deals with multi-class classification, classifying images of pomegranates to 5 classes: Alternaria, Anthracnose, Bacterial Blight, Cercospora, and Healthy.

### 🧮 **What I had done!**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

- Labels were converted to probability distributions by one-hot encoding them.

- Images were resized to a fixed size of 224x224 pixels.

- Custom and pre-trained models were used for this task.

### 🚀 **Models Implemented**

models used:

- ResNet-50
- Xception
- VGG16
- CNN
- InceptionV3
- DenseNet-121
- MobileNet

### 📚 **Libraries Needed**

- Keras

- Tensorflow

- Numpy

- Matplotlib

### 📊 **Exploratory Data Analysis Results**


- #### **Exploratory Data Analysis**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/Alternaria.jpg" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/Anthracnose.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/Bacterial%20Blight.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/Cercospora.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/Healthy.png" height="400px" width="400px" />
</p>

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/EDA.png"/>

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/InceptionV3%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/InceptionV3%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/VGG16%20Loss.png" height="400px" width="400px" />
</p>

- #### **MobileNet**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/MobileNet%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/MobileNet%20Loss.png" height="400px" width="400px" />
</p>

- #### **RESNET50**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/RESNET50%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/RESNET50%20Loss.png" height="400px" width="400px" />
</p>

- #### **DenseNet-121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/DENSENET121%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/DENSENET121%20Loss.png" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/Xception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/pomegranate-disease/Pomegranate%20Disease%20Classification%20using%20DL/Images/Xception%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation **Loss** and **Accuracy** as metrics.

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| ResNet-50 | 20.52% | 12.8102 |
| InceptionV3 | 96.86%  | 0.1006 | 
| CNN | 94.90% | 0.3179 |
| VGG16 | 96.21% | 0.1311 |
| MobileNet | 98.69% | 0.0488 |
| DenseNet-121 | 98.43% | 0.0451 |
| Xception | 97.78% | 0.0834 |

### 📢 **Conclusion**

We conclude the following:

All models except RESNET-50 work exceptionally well, and **DenseNet-121**, **Xception**, **VGG16**, **InceptionV3** and **mobileNet** are ideal choices. Customizing CNN for the task can also be considered a better alternative, due to flexibility in convolutional layers allowing capture of more complex features in a simple yet robust architecture.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
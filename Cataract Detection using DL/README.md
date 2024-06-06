## **Cataract Detection using DL**

### 🎯 **Goal**

The objective of this project is to classify images of eyes into immature and mature cataract in eyes.

### 🧵 **Dataset**

The dataset consists of 2 directories under train folder: immature and mature based on maturity of cataract, each directory containing 200 files totalling to 410.

### 🧾 **Description**

The project deals with binary classification, classifying images into mature and immature.

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
- MobileNet

### 📚 **Libraries Needed**

- Keras

- Tensorflow

- Numpy

- Matplotlib

### 📊 **Exploratory Data Analysis Results**


- #### **Exploratory Data Analysis**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/Negative%20EDA.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/Neutral%20EDA.png" height="400px" width="400px" />
</p>

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/Positive%20EDA.png"/>

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/tomato-leaf/Tomato-Leaf%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/InceptionV3%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/InceptionV3%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/VGG16%20Loss.png" height="400px" width="400px" />
</p>

- #### **MobileNet**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/EfficientNetB7%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/EfficientNetB7%20Loss.png" height="400px" width="400px" />
</p>

- #### **RESNET50**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/RESNET50%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/RESNET50%20Loss.png" height="400px" width="400px" />
</p>

- #### **DenseNet-121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/DENSENET121%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/DENSENET121%20Loss.png" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/Xception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/Xception%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation **Loss** and **Accuracy** as metrics.

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| ResNet-50 | 48.78% | 8.1656 |
| InceptionV3 | 98.37%  | 0.0386 | 
| CNN | 94.31% | 0.4778 |
| VGG16 | 100.00% | 0.0249 |
| MobileNet | 100.00% | 0.0030 |
| DenseNet-121 | 100.00% | 0.0100 |
| Xception | 100.00% | 0.0036 |

### 📢 **Conclusion**

We conclude the following:

MobileNet, VGG16, CNN, Xception and DenseNet-121 work exceptionally well, with **MobileNet**, **Xception**, **VGG16** and **DenseNet-121** being the ideal choice for this task.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
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

<br>

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/Negative%20EDA.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/Neutral%20EDA.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/speech-sentiment/Speech%20Sentiment%20Analysis%20using%20DL/Images/Positive%20EDA.png" height="400px" width="400px" />
</p>

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

- #### **EfficientNetB7**

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
| ResNet-50 | 48.00% | 1.0630 |
| InceptionV3 | 84.00%  | 0.4533 | 
| CNN | 94.00% | 0.2254 |
| VGG16 | 90.00% | 0.3243 |
| EfficientNetB7 | 42.00% | 1.0812 |
| DenseNet-121 | 82.00% | 0.7257 |
| Xception | 86.00% | 0.5171 |

### 📢 **Conclusion**

We conclude the following:



### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
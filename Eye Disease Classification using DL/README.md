## **Indian Venomous Snakes Classification using DL**

### 🎯 **Goal**

The objective of this project is to classify images of eyes into 4 categories: Normal, Cataract, Glaucoma, and Diabetic Retenopathy.

### 🧵 **Dataset**

The dataset consists of 4 subdirectories under the dataset, each having approximately 1000 images totalling to 4217.

### 🧾 **Description**

The project deals with binary classification, classifying images into 4 categories: Normal, Cataract, Glaucoma, and Diabetic Retenopathy.

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
| ResNet-50 | 23.06% | 12.4005 |
| InceptionV3 | 87.68%  | 0.3861 | 
| CNN | 87.68% | 0.4260 |
| VGG16 | 91.79% | 0.2457 |
| MobileNet | 90.52% | 0.2863 |
| DenseNet-121 | 92.42% | 0.2208 |
| Xception | 89.42% | 0.3184 |

### 📢 **Conclusion**

We conclude the following:

InceptionV3, CNN, DenseNet-121, MobileNet and VGG16 as well as Xception performed exceptionally well, with **VGG16**, **MobileNet** and **Densenet-121** being the ideal choice.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
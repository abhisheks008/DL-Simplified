## **Cotton Disease Classification using DL**

### 🎯 **Goal**

The objective of this project is to classify images of Cotton Leaves into 6 categories: Aphids, Army Worms, Bacterial Blight, Powdery Mildew, Target Spot and Healthy.

### 🧵 **Dataset**

The dataset consists of 6 subdirectories dealing with 5 diseases (Aphids, Army Worms, Bacterial Blight, Powdery Mildew, Target Spot) and Healthy set: each set has approximately 520 images totalling to 3118 images.

### 🧾 **Description**

The project deals with multiclass classification, classifying images into 6 categories: Aphids, Army Worms, Bacterial Blight, Powdery Mildew, Target Spot and Healthy.

### 🧮 **What I had done!**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

- Turned Labels into probability distributions.

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


- #### **EDA**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/Aphids.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/Army%20Worms.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/Bacterial%20Blight.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/Powdery%20Mildew.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/Target%20Spot.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/Healthy.png" height="400px" width="400px" />
</p>

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/EDA.png"/>

- #### **DenseNet-121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/DenseNet-121%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/DenseNet-121%20Loss.png" height="400px" width="400px" />
</p>

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/InceptionV3%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/InceptionV3%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/VGG16%20Loss.png" height="400px" width="400px" />
</p>

- #### **MobileNet**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/MobileNet%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/MobileNet%20Loss.png" height="400px" width="400px" />
</p>

- #### **RESNET50**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/RESNET50%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/RESNET50%20Loss.png" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/Xception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/cotton-disease/Cotton%20Disease%20Classification%20using%20DL/Images/Xception%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation **Loss** and **Accuracy** as metrics.

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| ResNet-50 | 17.95% | 13.2251 |
| InceptionV3 | 97.22%  | 0.1047 | 
| CNN | 92.52% | 0.3026 |
| VGG16 | 98.50% | 0.0673 |
| MobileNet | 99.36% | 0.0264 |
| DenseNet-121 | 99.57% | 0.0295 |
| Xception | 97.22% | 0.0989 |

### 📢 **Conclusion**

We conclude the following:

All models except Resnet-50 work excpetionally well on this task, and the ideal choices are **DenseNet-121**, **MobileNet**, **Xception** and **VGG16**. We can also observe that a custom CNN can be a good match for the task as well, being highly accurate with a simpler and smaller architecture.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
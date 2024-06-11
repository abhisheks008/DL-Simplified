## **Facial Keypoint Detection using DL**

### 🎯 **Goal**

The objective of this project is to predict 15 essential facial key-points like center of eyes, edge-points of eyebrows and so on by using images.

### 🧵 **Dataset**

The dataset consists of 2 subdirectories test_images and train_images, with a csv file containing 30 columns of 15 essential facial keypoint features; train_images totalling to approximately 7050 images and test_images totalling to approximately 1750 images.

### 🧾 **Description**

The project deals with regression, using 30 features(x and y co-ordinates, of 15 essential keypoints), dealing with images.

### 🧮 **What I had done!**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

- Labels were used to lock onto features for each image.

- Features have been normalized using a MinMaxScaler.

- Images were resized to a fixed size of 96X96 pixels.

- Custom and pre-trained models were used for this task.

### 🚀 **Models Implemented**

models used:

- NASNetMobile
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
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/Bacteria.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/Fungi.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/Pests.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/Virus.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/Healthy.png" height="400px" width="400px" />
</p>

- #### **DenseNet-121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/DENSENET121%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/DENSENET121%20Loss.png" height="400px" width="400px" />
</p>

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/InceptionV3%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/InceptionV3%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/VGG16%20Loss.png" height="400px" width="400px" />
</p>

- #### **MobileNet**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/MobileNet%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/MobileNet%20Loss.png" height="400px" width="400px" />
</p>

- #### **NASNetMobile**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/NASNetMobile%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/NASNetMobile%20Loss.png" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/Xception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/plant-pathogen/Plant%20Pathogen%20Detection%20using%20DL/Images/Xception%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation and Test **Mean Squared Error (MSE)** and **Mean Absolute Error (MAE)** as metrics.

| Models | Validation MSE | Validation MAE | Test MSE | Test MAE |
|--------|---------------------|--------------------------|---------------------|--------------------------|
| ResNet-50 | 0.0022 | 0.0221 | 0.0020 | 0.0218 |
| InceptionV3 | 0.0023  | 0.0277 | 0.0021 | 0.0273 | 
| CNN | 0.0015 | 0.0213 | 0.0013 | 0.0214 |
| VGG16 | 0.0022 | 0.0262 | 0.0019 | 0.0253 |
| MobileNet | 0.0023 | 0.0278 | 0.0022 | 0.0280 |
| DenseNet-121 | 0.0019 | 0.0245 | 0.0017 | 0.0240 |
| Xception | 0.0019 | 0.0240 | 0.0018 | 0.0239 |

### 📢 **Conclusion**

We conclude the following:

All models work well on the task, with **CNN**, **DenseNet-121**, **Xception**, **VGG-16** and **Resnet-50** are ideal for this.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
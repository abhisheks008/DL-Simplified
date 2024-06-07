## **Fracture Detection using DL**

### 🎯 **Goal**

The objective of this project is to classify images of x-ray scans of bones, into 2 classes: fracture and not-fractured.

### 🧵 **Dataset**

The dataset consists of 3 subdirectories under the bone_fracture_binary_classification directory, train, test and val, all three with 2 subdirectories: fracture and not-fractured; train with approximately 9200 images, val with approximately 850 and test with approximately 600 images respectively.

**Appropriate image count**

Train images images: 9165

Validation images: 764

Test images: 443

### 🧾 **Description**

The project deals with binary classification, classifying images into 2 categories: fracture and not-fractured bone x-ray scans.

### 🧮 **What I had done!**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

- Images were scanned for appropriateness.

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
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/Fracture.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/Not%20fractured.png" height="400px" width="400px" />
</p>

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/EDA.png"/>

- #### **DenseNet-121**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/DenseNet121%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/DenseNet121%20Loss.png" height="400px" width="400px" />
</p>

- #### **CNN**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/CNN%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/CNN%20Loss.png" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/InceptionV3%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/InceptionV3%20Loss.png" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/VGG16%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/VGG16%20Loss.png" height="400px" width="400px" />
</p>

- #### **MobileNet**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/MobileNet%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/MobileNet%20Loss.png" height="400px" width="400px" />
</p>

- #### **RESNET50**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/RESNET50%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/RESNET50%20Loss.png" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/Xception%20Accuracy.png" height="400px" width="400px" />
  <img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/fracture/Fracture%20Detection%20using%20DL/Images/Xception%20Loss.png" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used  **Loss** and **Accuracy** as metrics.

| Models | Validation Accuracy | Validation Loss | Test Accuracy | Test Loss |
|--------|---------------------|--------------------------| ---------------------|--------------------------|
| ResNet-50 | 38.74% | 9.8734 | 44.92% | 8.8777 |
| InceptionV3 | 61.26%  | 6.1766 | 55.08% | 7.1615 |
| CNN | 99.87% | 0.0100 | 100.00% | 0.0037 |
| VGG16 | 94.63% | 0.1482 | 96.16% | 0.1142 |
| MobileNet | 99.21% | 0.0346 | 100.00% | 0.0156 |
| DenseNet-121 | 94.50% | 0.1413 | 95.03% | 0.1494 |
| Xception | 98.82% | 0.0541 | 100.00% | 0.0170 |

### 📢 **Conclusion**

We conclude the following:

**CNN**, **Xception**, **DenseNet-121**, **VGG16** and **MobileNet** are all up to the task and are ideal for this.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
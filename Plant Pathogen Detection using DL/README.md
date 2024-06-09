## **Plant Pathogen Detection using DL**

### 🎯 **Goal**

The objective of this project is to classify images of Plants into 5 categories: Healthy, Virus, Bacteria, Fungi and Pests.

### 🧵 **Dataset**

The dataset consists of 5 subdirectories dealing with Healthy, Virus, Bacteria, Fungi and Pests: each carrying approximately 8000 images totalling to approximately 40000 images.

We downsampled to approximately 1000 images per class totalling to 5000 images.

### 🧾 **Description**

The project deals with multiclass classification, classifying images of Plants into 5 categories: Healthy, Virus, Bacteria, Fungi and Pests.

### 🧮 **What I had done!**

To achieve our goals, the following steps were implemented:

- Images were loaded using keras.utils and normalized to the range 0 to 1.

- Turned Labels into probability distributions.

- Images were resized to a fixed size of 224x224 pixels.

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
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
</p>

<img src=""/>

- #### **DenseNet-121**

<p align="center">
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
</p>

- #### **CNN**

<p align="center">
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
</p>

- #### **InceptionV3**

<p align="center">
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
</p>

- #### **VGG16**

<p align="center">
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
</p>

- #### **MobileNet**

<p align="center">
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
</p>

- #### **NASNetMobile**

<p align="center">
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
</p>

- #### **Xception**

<p align="center">
  <img src="" height="400px" width="400px" />
  <img src="" height="400px" width="400px" />
</p>

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics: 

We used Validation **Loss** and **Accuracy** as metrics.

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| NASNetMobile | 94.67% | 0.1586 |
| InceptionV3 | 93.47%  | 0.2511 | 
| CNN | 91.20% | 0.2696 |
| VGG16 | 97.20% | 0.1099 |
| MobileNet | 97.33% | 0.0917 |
| DenseNet-121 | 97.73% | 0.0754 |
| Xception | 95.20% | 0.1823 |

### 📢 **Conclusion**

We conclude the following:

All models worked exceptionally well on the task, and the ideal models for this are: **Xception**, **VGG16**, **MobileNet** and **DenseNet-121**.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
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
- Inception

### 📚 **Libraries Needed**

- Keras

- Tensorflow

- Numpy

- Matplotlib

### 📊 **Exploratory Data Analysis Results**


- #### Venomous

<img src = "">

- #### Non Venomous

<img src = "">

- #### CNN

<img src = "">

<img src = "">

- #### Xception

<img src = "">

<img src = "">

- #### VGG16

<img src = "">

<img src = "">

### 📈 **Performance of the Models based on the Accuracy Scores**

#### Metrics:

| Models | Accuracy | Loss |
|--------|---------------------|--------------------------|
| ResNet-50 | 60.96% | 0.6848 |
| inception | 76.71%  | 0.4543 | 
| CNN | % | 0. |
| CNN with Attention | % | 0. |
| Xception | 75.34%  | 0.5466 | 
| VGG16 | 78.77% | 0.5400 |

### 📢 **Conclusion**

We conclude the following:

VGG16 and inception work well on the dataset.

### ✒️ **Your Signature**

Original Contributor: Arihant Bhandari [https://github.com/Arihant-Bhandari]
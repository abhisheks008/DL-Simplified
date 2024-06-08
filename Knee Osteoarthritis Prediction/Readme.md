## **Knee Osteoarthritis Prediction**

### 🎯 **Goal**

The objective of this project is to classify xrays of Knee Xrays into 5 distinct categories based on severity of the disease.

### 🧵 **Dataset**

The dataset consists of four subdirectories: train, test, auto test and val (test and auto_test are the same). All four contain 5 subdirectories, each representing a severity of osteoarthritis. The test and auto_test subdirectory contains 1346 images in total, while the train subdirectory contains 5778 images in total and the val subdirectory contains 826 images in total.

### 🧾 **Description**

The project deals with multi-class classification, classifying images into 5 grades of severity.

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
- EfficientNetB7

### 📚 **Libraries Needed**

- Keras

- Tensorflow

- Numpy

- Matplotlib

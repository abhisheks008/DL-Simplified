# Shoe, Sandal, and Boot Image Classification Project<br>

## 🎯 Goal<br>
The main goal of this project is to develop an image classification system capable of distinguishing between shoes, sandals, and boots. The purpose is to create models that can accurately categorize footwear images into predefined classes, aiding in retail and fashion industry applications.<br>

## 🧵 Dataset<br>
The dataset used for this project consists of a collection of footwear images sourced from [Dataset Link](https://www.kaggle.com/datasets/hasibalmuzdadid/shoe-vs-sandal-vs-boot-dataset-15k-images). The dataset is curated to include various styles of shoes, sandals, and boots with labeled classes.<br>

## 🧾 Description<br>
This project focuses on using machine learning techniques to build robust image classification models for footwear. The developed models aim to identify different types of footwear based on visual features extracted from images.<br>

## 🧮 What I had done!<br>
1. **Data Preprocessing:**
   - Resized images to a standard input size for model compatibility.
   - Normalized pixel values to the range [0, 1].

2. **Model Architectures:**
   - Custom Convolutional Neural Network (CNN): Designed for specific features of footwear images.
   - Transfer Learning: Utilized the pre-trained VGG16 architecture for enhanced performance.

3. **Data Augmentation:**
   - Applied image data augmentation techniques using TensorFlow's ImageDataGenerator to improve model generalization.

4. **Model Training:**
   - Trained the custom CNN and VGG16 models on the preprocessed and augmented dataset.
   - Evaluated models on a validation set to monitor performance.

5. **Save Models:**
   - Saved the trained models for future use and predictions.

## 🚀 Models Implemented<br>
   - Custom Convolutional Neural Network (CNN)
   - VGG16-based Convolutional Neural Network

**Why these models:**
   - Custom CNN: Designed for dataset-specific features.
   - VGG16: Known for simplicity and effectiveness in image classification tasks.

## 📚 Libraries Needed
1. TensorFlow
2. Matplotlib
3. Numpy
4. Scikit-learn (for additional evaluation metrics if required)

## 📊 Exploratory Data Analysis Results


**Distribution of Classes**
To gain an understanding of the dataset, we analyzed the distribution of images across different classes.

| Class   | Number of Images |
|---------|-------------------|
| Shoe    |  5000             |
| Sandal  |  5000             |
| Boot    |  5000             |

| Model   | Accuracy |
|---------|-------------------|
| Custom CNN  |  78%            |
| VGG 16  |  98%             |

*INSIGHT* : VGG16 has the better accuracy . <br>

## 📈 Performance of the Models based on Accuracy Scores<br>
   - Custom CNN Model Accuracy: XX%
   - VGG16 Model Accuracy: XX%

## 📢 Conclusion<br>
The footwear image classification project demonstrates effective learning and categorization across different types of footwear. The models show promising accuracy, with the [best_model_name] achieving the highest accuracy of XX%. These results indicate the potential of the models for real-world applications in footwear recognition.<br>

## ✒️ Your Signature<br>
Dipayan Majumder<br>
[dipayan22](https://github.com/dipayan22/)<br>


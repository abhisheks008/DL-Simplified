# CHILDREN VS ADULT CLASSIFICATION

## 🎯 Goal

The main goal of this project is to develop a classification model capable of accurately distinguishing between images of children and adults. The purpose is to explore the performance of different deep learning models specifically tailored for this classification task.

## 🧵 Dataset

The dataset used for this project can be found [here](https://www.kaggle.com/datasets/die9origephit/children-vs-adults-images). It consists of a collection of labeled images containing children and adults.

## 🧾 Description

This project aims to build a classification model that can analyze facial features and classify images as either children or adults. By leveraging deep learning models, the project seeks to achieve accurate and reliable classification results.

## 🧮 What I had done!

1.	Data collection - Gathered a diverse dataset of images containing children and adults.
   
2.	Data preprocessing - Performed essential preprocessing steps, including resizing, normalization, and augmentation, to prepare the data for training.
   
3.	Model selection - Chose popular deep learning models, including VGG19, ResNet50, InceptionV3, and MobileNetV2, for the classification task.
   
4.	Model training - Trained each model using the labelled dataset and appropriate training configurations.
   
5.	Model evaluation - Evaluated the trained models on a separate test dataset to measure their performance in terms of accuracy and other relevant metrics.
    
6.	Comparative analysis - Compared the accuracy and results of each model to determine the best-performing model for the task of classifying images into children and adults categories.

## 🚀 Models Implemented

The following models were used in this project:

1.	VGG19 - VGG19 is a deep convolutional neural network known for its simplicity and effectiveness in image classification tasks. It consists of 19 layers and has achieved remarkable accuracy in various competitions and benchmarks.
   
2.	ResNet50 - ResNet50 is part of the ResNet (Residual Network) architecture, featuring residual connections that enable the training of very deep networks. ResNet50 specifically has 50 layers and has demonstrated superior performance in image classification tasks, especially on datasets with a large number of classes.
   
3.	InceptionV3 - InceptionV3, developed by Google, is famous for its inception module, which allows for efficient use of computational resources by parallelizing operations. It has been widely adopted due to its excellent trade-off between computational efficiency and accuracy,
   
4.	MobileNetV2 - MobileNetV2 is designed specifically for mobile and embedded vision applications, where computational resources are limited. It utilizes depth-wise separable convolutions to reduce the number of parameters and computations while maintaining high accuracy.

The choice of these models was based on their proven performance in image classification tasks and their varying architectural complexities, enabling a comprehensive analysis.

## 📚 Libraries Needed

The following libraries are required to run this project:
 -  TensorFlow - An essential deep learning framework offering a flexible ecosystem for building and training neural networks.
   
 - 	Keras - A high-level neural networks API, seamlessly integrated with TensorFlow, simplifying the process of building and training deep learning models.
   
 -  Numpy - The fundamental package for scientific computing in Python, providing support for large multi-dimensional arrays and matrices.
   
 - 	Matplotlib - A versatile plotting library for Python, enabling visualization of data and model performance with ease.
   
 -	Pandas - A powerful data manipulation and analysis library, facilitating data preprocessing and exploration.

## 📊 Exploratory Data Analysis Results

![comparison2](https://github.com/vanshikab52/DL-Simplified/assets/148718670/fa02141c-e5c6-41d9-a518-27c091af435d)

## 📈 Performance of the Models based on the Accuracy Scores

- VGG19 - 0.73
- ResNet50 - 0.67
- InceptionV3 - 0.74
- MobileNetV2 - 0.79

## 📢 Conclusion

Based on the accuracy results, MobileNetV2 achieved the highest accuracy of 79% on the test dataset, making it the best-fitted model for this particular project. The other models also performed well but had slightly lower accuracies. 
This project demonstrates the effectiveness of deep learning models in classifying images of children and adults based on facial features, with potential applications in age estimation or child/adult recognition systems.

## ✒️ Your Signature

  ##### 📌 README.md modified by *Vanshika Bisht* @ GGSoC2024
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)]( www.linkedin.com/in/vanshika-bisht-a875aa2b7) [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/vanshika52)

# Project Title

Predict the Time of the Day using DL

## Goal

The goal of this project is to develop a machine learning model that can classify images into different time of day categories, such as morning, afternoon, evening, and night.

## Dataset

The dataset used in this project can be found at(https://www.kaggle.com/datasets/aymenkhouja/timeofdaydataset). It consists of a collection of labeled images, each representing a specific time of day.

## Description

This project aims to classify images based on the time of day depicted in them. The images are preprocessed, and three different machine learning algorithms (SVM, KNN, and Random Forest) are trained and evaluated to determine the best-performing model. The accuracy of each model is calculated using cross-validation and the model with the highest accuracy is selected for further analysis. The selected model is used to predict the time of day for a subset of test images and visualize the predictions. Additionally, a confusion matrix is generated to assess the model's performance.

## What I Had Done

1. Loaded and preprocessed the image dataset.
2. Split the dataset into training and testing sets.
3. Encoded the target labels using LabelEncoder.
4. Trained and evaluated three machine learning algorithms: SVM, KNN, and Random Forest.
5. Selected the best-performing model based on accuracy scores.
6. Trained the best model on the training set.
7. Plotted learning curves to visualize the model's performance.
8. Predicted the time of day for a subset of test images and visualized the predictions.
9. Computed and displayed the confusion matrix for the best model.

## Models Used

The following machine learning algorithms were used in this project:

- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Random Forest

I chose these algorithms as they are commonly used for classification tasks and have shown good performance in similar image classification problems.

## Libraries Needed

The following libraries were used in this project:

- os
- numpy
- PIL (Python Imaging Library)
- matplotlib
- sklearn (scikit-learn)

## Visualization

![Screen Shot 2023-06-09 at 08 55 28](https://github.com/SaketGudimella/DL-Simplified/assets/106355242/0057d751-0ce6-4ecf-a8ed-8b16ba12a328)



![Screen Shot 2023-06-09 at 08 55 11](https://github.com/SaketGudimella/DL-Simplified/assets/106355242/0e83f8f6-fc71-4b8a-90f2-20c83b9a18a6)





## Accuracies

The accuracies achieved by the three machine learning algorithms are as follows:

- SVM Accuracy: 0.8450638409898644
- KNN Accuracy: 0.7972949848624458
- Random Forest Accuracy: 0.8024417533236804

Based on these accuracies, the SVM algorithm performed the best and was selected as the final model for classification.

## Conclusion

In this project, we successfully developed a machine learning model to classify images based on the time of day depicted in them. The Random Forest algorithm showed the highest accuracy among the tested models. The model's performance was visualized using learning curves, and a subset of test images was used to demonstrate the model's predictions. The generated confusion matrix provided further insights into the model's performance.

By accurately classifying images into time of day categories, this model can be useful in various applications such as image organization, scene recognition, and smart photo editing.

## Author

Saket Gudimella 
GitHub: https://github.com/SaketGudimella)
LinkedIn: www.linkedin.com/in/saket-gudimella-299611240


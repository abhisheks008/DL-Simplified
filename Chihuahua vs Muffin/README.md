# Chihuahua vs Muffin image Detection using DL

## PROJECT TITLE

Chihuahua vs Muffin

## 🎯 Goal

The aim is to create a deep-learning model that will classfiy images into Chihuahua or Muffin. 

## 🧵 Dataset

The link for the dataset used in this project: https://www.kaggle.com/datasets/samuelcortinhas/muffin-vs-chihuahua-image-classification

## 🧾 Description
The main goal of the project is to develop a deep-learning model that can accurately classify images into Chihuahua or Muffin.

## 🧮 What I had done!

1. Data collection: The data is loaded from the links provided above and its structure is 
   explore 
2. Data preprocessing: The data is then preprocessed, where steps such as setting batch 
   size, and image size, converting the image type to a specific type, and scaling are 
   done 
   to prepare the data for model training
3. Model training: I have taken VGG16 , ResNet and a CNN model from scratch.  
4. Comparative analysis: The developed model performances are analysed based on their 
   accuracy.

## 🚀 MODELS USED

 1. VGG16: VGG16 is chosen for image detection due to its pre-trained architecture on ImageNet, deep layers for learning intricate patterns, availability in frameworks like TensorFlow, and suitability for transfer learning, enabling effective model training even with limited data.
 
2. ResNet50: ResNet50 was chosen for image detection.
3. CNN: The CNN was trained from scratch to binary classify the images into the the respective classes. 



## 📚 LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy
- pandas
- matplotlib
- tensorflow


## 📊 Exploratory Data Analysis Results
This is present in the Images directory.


## 📈 Performance of the Models based on the Accuracy Scores
This is present in the Images directory.

## 📢 Conclusion
Based on the results we can draw the following conclusions:
1. CNN: The CNN model achieved a higher accuracy of 0.9170 and a lower loss of 0.2251.
2. VGG16: The VGG16 model achieved an accuracy of 0.97 and a loss of 0.0727.
3. ResNet50: The ResNet50 model achieved an accuracy of 0.7917 and a loss of 0.4435.

##### Code contributed by: Dipankar Dutta
##### Email: dipankardutta399@gmail.com

# Handwriting Recognition Project

### Goal
The goal is to create a deep learning project which will recognize the handwritings and detect them with an accuracy of more than 85%

### Dataset
The dataset is collected from the following link, https://www.kaggle.com/datasets/landlord/handwriting-recognition

### Description
This dataset consists of more than four hundred thousand handwritten names collected through charity projects. The task is to recognize the handwritten characters and convert it to digital text.


### What I have done
1. Imported the required libraries
2. Imported the dataset
3. Cleaned the data from null values
4. Removed the data which was unreadable
5. Converted lowercase labels to uppercase to maintain uniformity
6. Labels are converted to numbers representing each character
7. Went through the steps to train a Convolutional Recurrent Neural Network (CRNN) model using Connectionist Temporal Classification Loss (CTC Loss) for handwriting recognition.
8. Used stacked 3 convolution layers with 32,64,128 filters respectively with a kernal size of 3x3 
9. To introduce non-linearity in the convolution layers, the activation function ReLU is used.
10. Max-pooling is applied after some convolutional layers
11. Function used to minimize the loss is the CTC loss function because it optimizes both the length of the predicted data and the classes of the same.
12. The model predicts words of 64 characters and each character contains the probability of the 30 alphabets which were defined earlier.



### Libraries used
1. `os`
2. `random`
3. `opencv`
4. `numpy`
5. `pandas`
6. `matplotlib`
7. `keras`
8. `tensorflow`


# Models Used #
1. Convolutional Neural Network (CNN)
2. Convolutional Neural Network (CNN) with MaxPooling layer

### Visualization ###

### Dataset ###
![image](https://github.com/SHAY2407/DL-Simplified/blob/main/Handwriting%20Recognition%20Project/Images/datasetImg.jpg)

### Distribution of names ###
![image](https://github.com/SHAY2407/DL-Simplified/blob/main/Handwriting%20Recognition%20Project/Images/DistbNames.jpg)

### heatmap ###
![image](https://github.com/SHAY2407/DL-Simplified/blob/main/Handwriting%20Recognition%20Project/Images/heatmap.jpg)

### Histogram ###
![image](https://github.com/SHAY2407/DL-Simplified/blob/main/Handwriting%20Recognition%20Project/Images/Histogram.jpg)

### Accuracy ###

|                                             | Accuracy in % (on testing data) |
|:-------------------------------------------:|:-------------:|
| Correct characters predicted                |82.16          |
| Correct words predicted                     |69.10          |

### Conclusion ###
Successfully able to develop a Deep Learning Model that can detect handwriting with upto 85% accuracy

**Yashwardhan Khanna**

Connect with me on Linkedin: https://www.linkedin.com/in/yashwardhan-khanna-7596871a5/
Check out my Github profile: https://github.com/SHAY2407

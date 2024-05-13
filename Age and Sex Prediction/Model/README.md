## **AGE AND SEX PREDICTION**

Deep Learning has many applications in the field of computer vision and one such application is that of facial detection & recognition. To this subfield, we have also added the application of age and sex detection.

### 🎯 **Goal**

The objective of this project is to create a DL model which can detect gender and age using any input facial images. A Convolutional Neural Network is used to classify the images. There are 2 output types: gender (M/F) and age.

### 🧵 **Dataset**

I have used Kaggle's [EMİRHAN BULUT](https://www.kaggle.com/datasets/emirhanai/age-and-sex-prediction-by-artificial-intelligence) dataset, which in turn is based on the [UTKFace](https://www.kaggle.com/datasets/jangedoo/utkface-new) dataset.

### 🧾 **Description**

The dataset consists of over 20,000 facial images with annotations for age, gender, and ethnicity. The dataset is a large-scale face-image dataset with images of people aged 0 to 116 years. Images cover large variation in pose, facial expression, illumination, occlusion, resolution, etc. The dataset can be used to implement a variety of other tasks, such as face detection, age estimation, age progression/regression, landmark localization, etc.

Dataset Image Sample<br>
![image](https://raw.githubusercontent.com/ASHISHKUMAR2411/DL-Simplified/main/Age%20and%20Sex%20Prediction/Images/OneoftheDatasetImage.png)

### 🧮 **What I have done!**

We have trained a pre-trained CNN model using the above dataset and adjusted the algorithm as per the requirements. The model uses Convolutional Layers from Convolutional Neural Networks and compares the accuracy for age and gender. It also figures out the loss during model training. We have trained the model with a large variation of images covering different poses, facial expressions, illumination, occlusion, resolution, etc in order to enhance the accuracy of the model.

### 🚀 **Models Implemented**

![image](https://raw.githubusercontent.com/ASHISHKUMAR2411/DL-Simplified/main/Age%20and%20Sex%20Prediction/Images/ModelUsed.png)


### 📊 **Exploratory Data Analysis Results**

- Frequency Distribution of age in images used in the dataset<br>
![image](https://raw.githubusercontent.com/ASHISHKUMAR2411/DL-Simplified/main/Age%20and%20Sex%20Prediction/Images/AgeDistribution.png)

- Grid View of a few images used in the dataset<br>
![image](https://raw.githubusercontent.com/ASHISHKUMAR2411/DL-Simplified/main/Age%20and%20Sex%20Prediction/Images/DatasetPlot.png)

- Gender Distribution<br>
![image](https://raw.githubusercontent.com/ASHISHKUMAR2411/DL-Simplified/main/Age%20and%20Sex%20Prediction/Images/GenderDistribution.png)

- Accuracy and Loss Graph for Gender

Accuracy<br>
![image](https://raw.githubusercontent.com/ASHISHKUMAR2411/DL-Simplified/main/Age%20and%20Sex%20Prediction/Images/AccuracyforGender.png)

Loss<br>
![image](https://raw.githubusercontent.com/ASHISHKUMAR2411/DL-Simplified/main/Age%20and%20Sex%20Prediction/Images/genderloss.png)

- Accuracy and Loss Graph for Age
![image](https://raw.githubusercontent.com/ASHISHKUMAR2411/DL-Simplified/main/Age%20and%20Sex%20Prediction/Images/Age.png)

### 📈 **Performance of the Models based on the Accuracy Scores**

Testing on a random image from indices 1 - 23708, you can also test by changing index of the image used for test, variable name and image_index.

- Test Image

Original Gender: Male<br>
Original Age: 10<br>
Predicted Gender: Male<br>
Predicted Age: 11<br>

![image](https://raw.githubusercontent.com/ASHISHKUMAR2411/DL-Simplified/main/Age%20and%20Sex%20Prediction/Images/test1.png)

- Test Image 

Original Gender: Male<br>
Original Age: 25<br>
Predicted Gender: Male<br>
Predicted Age: 24<br>

![image](https://raw.githubusercontent.com/ASHISHKUMAR2411/DL-Simplified/main/Age%20and%20Sex%20Prediction/Images/test2.png)

- Test Image 

Original Gender: Female<br>
Original Age: 29<br>
Predicted Gender: Female<br>
Predicted Age: 29<br>

![image](https://raw.githubusercontent.com/ASHISHKUMAR2411/DL-Simplified/main/Age%20and%20Sex%20Prediction/Images/test3.png)

### 📢 **Conclusion**
We can vary the number of epochs to get more accuracy on models. So far, we have achieved an accuracy of more than 95%.

### ✒️ **Your Signature**
Name: Ashish Kumar<br>
License: MIT
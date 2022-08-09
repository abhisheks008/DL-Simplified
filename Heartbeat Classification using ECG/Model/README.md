# Heartbeat Classification using ECG

### Goal
The goal of this project is to create a deep learning model which will predict the heartbeat of the patients from the ECG images.

### Dataset
The dataset is collected from the following link, https://www.kaggle.com/datasets/shayanfazeli/heartbeat

### What I have done
Firstly I have visulized the data using different data visualization techniques and after that the model creation is started.

### Libraries used
1. `Numpy`
2. `Pandas`
3. `sklearn`
4. `Keras`
5. `Tensorflow`
6. `matplotlib`


# Data Visualization And Conclusion #

### Content of the Training Data set ###

![image](https://user-images.githubusercontent.com/83596240/183436392-f412bd71-0330-4bc5-bcde-41f78583a959.png)

### Different classes/categories along with their frequency ###

![image](https://user-images.githubusercontent.com/83596240/183436723-a8930a81-472e-4cf6-81ee-136cc47db7c8.png)

### Depicting each class in percentage wise using a pie plot ###

![image](https://user-images.githubusercontent.com/83596240/183436966-228c24f1-6e79-4a64-ba47-8aadba9c8c24.png)

We can see that Normal beats as the highest percentage and Fusion beats as the lowest

### Normalizing and Resizing the Training Data set ###

![image](https://user-images.githubusercontent.com/83596240/183437696-c1d54039-6043-4e74-a344-92d872eedadc.png)

The resultant Training Data set that we get is

![image](https://user-images.githubusercontent.com/83596240/183437918-93bcb404-d275-4cff-8deb-12cd9eacb38c.png)

### Updated classes/categories along with their frequency ###

![image](https://user-images.githubusercontent.com/83596240/183438062-ac62948e-fd33-4662-b8f3-4860bdfa9576.png)

As we can see the training dataset is equally balanced with each category having frequency of 16000

### Depicting each class in percentage wise using a pie plot ###

![image](https://user-images.githubusercontent.com/83596240/183438173-e9899fa1-f644-4f1d-852a-2190d20e50d8.png)

### Sample data from each categories ###

![image](https://user-images.githubusercontent.com/83596240/183438386-e32a0d44-788f-4ce1-819d-5666c39df86f.png)

### Checking the Testing Accuracy and Loss ###

![image](https://user-images.githubusercontent.com/83596240/183439120-d751e678-a494-4ac5-ad38-89bd42c65665.png)

The accuracy of the trained model stands at 96.67% and loss is 13.4%

Graphing the training accuracy and loss against the testing acurracy and loss

![image](https://user-images.githubusercontent.com/83596240/183438969-d446f376-582a-4283-a67d-2e7f71ececc6.png)

As the epochs increases the loss decreses and the accuracy increases

### Confusion matrics of the trained model ###

![image](https://user-images.githubusercontent.com/83596240/183439764-f22613f0-68d8-4153-a5ed-85a3db911727.png)

### Training the model with noise to avoid overfitting ###

![image](https://user-images.githubusercontent.com/83596240/183439990-49f9aa6b-b425-432d-b371-9e192fd4a7fa.png)

### Checking the Testing Accuracy and Loss of the new model ###

![image](https://user-images.githubusercontent.com/83596240/183440057-23200f9e-c8c8-49a2-b397-1409695a2d74.png)

The accuracy as reduced to 76.3% and the loss as increased to 132% when we add noise to the dataset

Confusion matrics of the newly trained model

![image](https://user-images.githubusercontent.com/83596240/183440297-ebee69b5-82bd-4ff8-80fe-302b955d9f1a.png)

### This the Confusion metrics that we get after applying transfer learning and performing fine tune to the noisy model ###

![image](https://user-images.githubusercontent.com/83596240/183440719-34265311-faea-46c7-9759-dc38fdf1f345.png)


# Introduction

Disease detection Model is a model which will classify the fusarium wilt images among various different classes based on the severity of disease.

# Dataset

The dataset used in this project is take from the Kaggle website.
<br>
<b>Dataset Link:- https://www.kaggle.com/datasets/tolgahayit/fusarium-wilt-disease-in-chickpea-dataset/data </b>
<br>

<br>
The Data Set consists of raw and augmented images with categories of healthy and fusarium wilt diseased leaf images. It is foreseen that the data set will guide related studies in the area.
<br>

<br>
Severity level images from the dataset:
<br>1: Highly Resistant (HR): The plant has been wilted by 0%-10%,
<br>3: Resistant (R): The plant has been wilted by 11%-20%,
<br>5: Moderately Resistant/ Tolerant (MR): The plant has been wilted by 21%-30%,
<br>7: Susceptible (S): The plant has been wilted by 31%-50%,
<br>9: Highly Susceptible (HS): The plant has been wilted by more than 51%
<br>


# Aim

The main aim is to build a Deep Learning model using various approaches that will be able to classify a image into its appropriate class with the highest accuracy.

# Approach

We will try to build the models using  different approaches and compare their accuracy. In this notebook we will be building models using VGG16, DenseNet and MobileNet. 

# VGG16
![VGG16](https://github.com/the-silent-geek/DL-Simplified/blob/7652413344186a95ec90a15f639f3efc10da6493/Fusarium%20Wilt%20Disease%20Detection/images/VGG16.jpg)

# MobileNet
![MobileNet](https://github.com/the-silent-geek/DL-Simplified/blob/01c08181398f712cb364bbe9f71749a23ef668fb/Fusarium%20Wilt%20Disease%20Detection/images/MobileNet.jpg)

# DenseNet
![DenseNet](https://github.com/the-silent-geek/DL-Simplified/blob/97e0d242b9c5dbc11bae466b6f4dc8ba9f1b01e5/Fusarium%20Wilt%20Disease%20Detection/images/DenseNet210.jpg)
# Pie-chart of severity level of diseases
1[Pie-chart](https://github.com/the-silent-geek/DL-Simplified/blob/e9e7a9b61272b8df9c02bfe3a9a6b6d58f282e4c/Fusarium%20Wilt%20Disease%20Detection/images/EDA.png)

# Bar plot for number of cases for specific levels
![Bar-plot](https://github.com/the-silent-geek/DL-Simplified/blob/33ca1d25fe31624b315128b73490b35d0a9aa943/Fusarium%20Wilt%20Disease%20Detection/images/bar%20plot.png)
# Conclusion

We have solved the problem using four different approaches. The differences in the accuracies may be because of the model's architecture, optimizers used, loss functions used.
<br>
The VGG16 model seemed to have the best accuracy in our case.

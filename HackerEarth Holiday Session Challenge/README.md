# HackerEarth Holiday Session Challenge

This is a tutorial demonstrating how to train a CNN model using pretrained model on HackerEarth Holiday Session Challenge dataset.

Process
-----------------

* [Setup](#setup)
* [Preparing training data](#preparing)
* [Training on a local PC](#training-locally)
* [Testing the model](#testing)

 # Introduction

This HackerEarth Holiday Session Challenge Detection model is based on CNN model.

# Dataset

The dataset for this project is taken from the Kaggle website. Here is the link for the dataset,(https://www.kaggle.com/datasets/oossiiris/hackerearth-deep-learning-challenge-holidayseason).

Here in the dataset you will find six categories of images i.e 
-Miscellaneous
-Christmas_Tree
-Jacket
-Candle
-Airplane
-Snowman

# Goal

The goal of this project is to discern whether a post is holiday-related in an effort to better monetize the platform.

# Approach

In the notebook we have implemented InceptionResNetV2 transfer learning method using pretrained weight.

# Approach Using Pretrained model - InceptionResNetV2 

![image.png](https://production-media.paperswithcode.com/methods/Screen_Shot_2020-06-12_at_1.24.15_PM_qDb6V3G.png)

### This model gives an validation accuracy of 89%.

# Training and Testing

Training the model requires GPU for faster training but it can be trained on CPU as well.If GPU is not there then use google colab for training the model.Refer the notebook.ipynb file for detailed procedure of training and testing. 

This is the accuracy and loss plot we got after training-

![image.png](https://github.com/kshitij192/DL-Simplified/blob/main/HackerEarth%20Holiday%20Session%20Challenge/Images/4.png?raw=true)

![image.png](https://github.com/kshitij192/DL-Simplified/blob/main/HackerEarth%20Holiday%20Session%20Challenge/Images/3.png?raw=true)

# Conclusion
### We have implemented this approach and the model perform very well. As here we trained for 10 epoch only, you can train it for more epoch and get more good model.You can also use other pretrained model like MobNetv2,VGG-16 etc.

Author Github Link - **https://github.com/kshitij192**
### Thank You

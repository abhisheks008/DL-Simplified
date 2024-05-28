# Pseudo Papilledema Detection 

This is a tutorial demonstrating how to train a CNN model from scratch as well as using pretrained model on Pseudo Papilledema Detection dataset.

Process
-----------------

* [Setup](#setup)
* [Preparing training data](#preparing)
* [Training on a local PC](#training-locally)
* [Testing the model](#testing)

 # Introduction

This Pseudo Papilledema Detection model is based on CNN model.

# Dataset

The dataset for this project is taken from the Kaggle website. Here is the link for the dataset,(https://www.kaggle.com/datasets/shashwatwork/identification-of-pseudopapilledema).

Here in the dataset you will find three categories of images i.e Normal,Papilledema and Pseudo Papilledema.

# Goal

The goal of this project is to identify the Pseudo Papilledema in the image.

# Approach

In the notebook we have implemented three different approach i.e CNN from scratch, VGG16 and MobNetV2 model and compare their accuracy with the help of dataset each approach will be divided into different section.

# Approach Using CNN from scratch

### This model gives an accuracy of 91.24%.

# Approach Using Pretrained model - VGG16

![image.png](https://miro.medium.com/max/705/1*3-TqqkRQ4rWLOMX-gvkYwA.png)

### This model gives an accuracy of 93.06%.

# Approach Using Pretrained model - MobNetV2

![image.png](https://miro.medium.com/max/1050/1*bqE59FvgpvoAQUMQ0WEoUA.png)

### This model gives an accuracy of 92.70%.

# Training and Testing

Training the model requires GPU for faster training but it can be trained on CPU as well.If GPU is not there then use google colab for training the model.Refer the notebook.ipynb file for detailed procedure of training and testing. 

# Conclusion
### We have implemented three different approach and all of the three model perform very well. As here we trained for 20 epoch only, you can train it for more epoch and get more good model.

Author Github Link - **https://github.com/kshitij192**
### Thank You

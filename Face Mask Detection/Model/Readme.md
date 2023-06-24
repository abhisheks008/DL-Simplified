# Face mask detection using ConvNet, InceptionV3, MobileNet, DenseNet and VGG19

COVID-19 has been an inspiration for many software and data engineers during the last months.
This project demonstrates how a Depp learming models can detect if a person in a picture is wearing a face mask or not.
As you can easily understand the applications of this method may be very helpful for the prevention and the control of COVID-19 as it could be used in public places like airports, shopping malls etc.

## Defining the problem
Detecting if an image contains a person wearing a mask or not is a simple **classification problem**.
We have to classify the images between **2 discrete classes**: The ones that contain a face mask and the ones that do not.

## The dataset
https://www.kaggle.com/datasets/shiekhburhan/face-mask-dataset

![image](https://github.com/ranodeepbanerjee/DL-Simplified/assets/63450189/c0322919-0452-412a-9216-fbc75de3c17a)



## Models used

* Covnet - ConvNet, short for Convolutional Neural Network, is a type of deep learning model commonly used in image classification and object recognition tasks. It consists of multiple layers of convolutional and pooling operations that extract features from the input image.

* InceptionV3 - InceptionV3 is an advanced version of the Inception architecture, which is designed to improve the accuracy and efficiency of image classification models. It uses a combination of convolutions with different kernel sizes and pooling operations to capture multi-scale features.

* MobileNet - MobileNet is a lightweight neural network designed for mobile and embedded devices with limited computational resources. It uses depthwise separable convolutions to significantly reduce the number of parameters and computation required while maintaining high accuracy.

* DenseNet - DenseNet is a densely connected neural network that allows each layer to have direct access to the feature maps of all preceding layers. This results in better feature reuse and gradient flow, leading to improved accuracy and reduced overfitting.

* VGG19 - VGG19 is a deep neural network with 19 layers specifically designed for image recognition tasks. It uses small convolutional filters with a fixed size of 3x3 across all layers and max-pooling operations to extract and learn hierarchical features from images.

## Distribution of classes

![image](https://github.com/ranodeepbanerjee/DL-Simplified/assets/63450189/4392ebd7-5aa2-4fd3-88e3-d90c17dfee14)


## Evaluation

![image](https://github.com/ranodeepbanerjee/DL-Simplified/assets/63450189/eef19273-71e7-4284-8156-3db09f7051c1)

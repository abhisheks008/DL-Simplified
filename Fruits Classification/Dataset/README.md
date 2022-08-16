# Fruits Classification

(dataset image)

# Introduction

Fruits Classification Model is a model which will classify the fruits among various different classes on which it was trained.

# Dataset

The dataset used in this project is take from the Kaggle website.
<br>
<b>Dataset Link:- https://www.kaggle.com/datasets/moltean/fruits </b>
<br>
In this dataset there will be 2 different folders for training and testing. It contains 131 different classes of fruits and vegetables. Out of the total 90483 images, 67692 are in the training folder and 22688 are in the testing folder.
<br>
<b>Some of the classes are:</b> Apples (different varieties), Apricot, Avocado, Banana (Yellow, Red, Lady Finger),Cherry (different varieties, Rainier), Grape (Blue, Pink, White (different varieties)), Onion (Red, White), Orange, Papaya, Tomato (different varieties, Maroon, Cherry Red, Yellow, not ripened, Heart), Watermelon.

# Aim

The main aim is to build a Deep Learning model using various approaches that will be able to classify a fruit's/vegetable's image into its appropriate class with the highest accuracy.

# Approach

We will try to build the models using  different approaches and compare their accuracy. In this notebook we will be building models using CNN, VGG16, Inception ResNet and MobileNet. 

## Exploratory Data Analysis
(image - 3)

## 1. CNN Model 
    
A Convolutional Neural Network is a type of neural network that is used in Computer Vision and Natural Language Processing tasks quite often due to the fact that it can learn to extract relevant features from the input data. 
<br>
A typical CNN layer can be understood with the help of following diagram:
(image 2)

## 2. VGG16 Model

VGG-16 is a convolutional neural network that is 16 layers deep. It is considered to be one of the excellent vision model architecture till date. Most unique thing about VGG16 is that instead of having a large number of hyper-parameter they focused on having convolution layers of 3x3 filter with a stride 1 and always used same padding and maxpool layer of 2x2 filter of stride 2.

## 3. InceptionResnet 
Inception-ResNet-v2 is a convolutional neural network that is trained on more than a million images from the ImageNet database. The network is 164 layers deep and can classify images into 1000 object categories, such as keyboard, mouse, pencil, and many animals.

## 4. MobileNet
MobileNet-v2 is a convolutional neural network that is 53 layers deep. MobileNet uses depthwise separable convolutions. It significantly reduces the number of parameters when compared to the network with regular convolutions with the same depth in the nets. This results in lightweight deep neural networks.

## Observation

We have observed that:<br>
<i>Test Accuracy for CNN model = <b>0.9599</b> <br>
Test Accuracy for VGG16 model = <b>0.8925</b> <br>
Test Accuracy for Inception-ResNet model = <b>0.8008</b> <br>
Test Accuracy for MobileNet model = <b>0.9109</b> <br>

# Conclusion

We have solved the problem using four different approaches. The differences in the accuracies may be because of the model's architecture, optimizers used, loss functions used and so on. You can try changing these and observe how the model performs on your system.
<br>
The CNN model seemed to have the best accuracy in our case.
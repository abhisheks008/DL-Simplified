# CCTV-HUMAN-DETECTION

 ![image.png](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrLn9Zzwpzvpp2FLu0n8bdwOIR26fARzsV4A&usqp=CAU)

YOLOv4 HumaN DETECTION
==========================

This is a tutorial demonstrating how to train a YOLOv4 people detector using [Darknet](https://github.com/AlexeyAB/darknet) and the Kaggle Human dataset.

Process
-----------------

* [Setup](#setup)
* [Preparing training data](#preparing)
* [Training on a local PC](#training-locally)
* [Testing the custom-trained yolov4 model](#testing)

 # Introduction

This Human detection model is made on deep learning model based on Yolo(You Only Look Once).

# Dataset

The dataset for this project is taken from the Kaggle website. Here is the link for the dataset,https://www.kaggle.com/datasets/jonathannield/cctv-human-pose-estimation-dataset.

Here in the dataset you will find the various human images captured through CCTV cameras installed on various places.
But the dataset is not suitable for training for Yolo model.So,first we annotate the data according to format provided by Yolo.
We used LabelIMG to annotate image.

You can refer to https://machinelearningknowledge.ai/train-custom-yolov4-model-for-object-detection-in-google-colab/ for custom data preparation.


# Goal

The goal of this project is to identify human being from CCTV camera.

# Approach

In the notebook we have implemented various Yolov4 and latest released Yolov7 and compare their accuracy with the help of dataset each approach will be divided into different section.

# Approach Using Yolov4

![image.png](https://miro.medium.com/max/785/1*f2diI7O28j2A875FwQPMJA.jpeg)

### This model fails to perform with distant and finer object.

# Approach Using Yolov7

![image.png](https://github.com/WongKinYiu/yolov7/raw/main/figure/performance.png)

### This model performs much better than Yolov4 on distant objects

# Training and Testing

Training the model requires GPU.If GPU is not there then use google colab for training the model.Refer the yolo_model.ipynb file for detailed procedure of training and testing. 

# Conclusion
### We have implemented two different approach Yolov4 and Yolov7 and, Yolov7 gives the best accuracy.

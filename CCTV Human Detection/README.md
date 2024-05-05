# CCTV Human Detection

##  🎯 Goal

The goal of this project is to identify human beings from CCTV camera footage.

 ![image.png](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrLn9Zzwpzvpp2FLu0n8bdwOIR26fARzsV4A&usqp=CAU)
 
## 🧵 Dataset

The dataset for this project is taken from the Kaggle website. [Link](https://www.kaggle.com/datasets/jonathannield/cctv-human-pose-estimation-dataset) to the dataset. Here, you'll find various human images captured through CCTV cameras installed in different locations. However, the dataset is not suitable for training a YOLO model. Therefore, we annotated the data according to the format provided by YOLO using LabelIMG.

## 🧾 Description

This is a tutorial demonstrating how to train a YOLOv4 people detector using Darknet and the Kaggle Human dataset.

## 🧮 What I had done!

#### Setup
- Preparing training data
- Training on a local PC
- Testing the custom-trained YOLOv4 model

## 🚀 Models Implemented

##### YOLOv4
This model fails to perform with distant and finer objects.

##### YOLOv7
This model performs much better than YOLOv4 on distant objects.

## 📚 Libraries Needed

- Darknet
- LabelIMG
- TensorFlow
- NumPy




 # Introduction

This Human detection model is made on deep learning model based on Yolo(You Only Look Once).

# Dataset

The dataset for this project is taken from the Kaggle website. Here is the link for the dataset,https://www.kaggle.com/datasets/jonathannield/cctv-human-pose-estimation-dataset.

Here in the dataset you will find the various human images captured through CCTV cameras installed on various places.
But the dataset is not suitable for training for Yolo model.So,first we annotate the data according to format provided by Yolo.
We used LabelIMG to annotate image.

You can refer to https://machinelearningknowledge.ai/train-custom-yolov4-model-for-object-detection-in-google-colab/ for custom data preparation.



# Approach Using Yolov4

![image.png](https://miro.medium.com/max/785/1*f2diI7O28j2A875FwQPMJA.jpeg)

### This model fails to perform with distant and finer object.

# Approach Using Yolov7

![image.png](https://github.com/WongKinYiu/yolov7/raw/main/figure/performance.png)

### This model performs much better than Yolov4 on distant objects


## 📢 Conclusion

We have implemented two different approaches, YOLOv4 and YOLOv7. YOLOv7 gives the best accuracy for this project.

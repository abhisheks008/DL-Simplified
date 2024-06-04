## **Object Detection from a Video**

### 🎯 **Goal**

The aim is to perform object detection in given video using pre-trained object detection model.

### 🧵 **Dataset**

The dataset is taken from [Kaggle](https://www.kaggle.com/datasets/shawon10/road-traffic-video-monitoring) and for testing and visualization purpose, images and videos are taken from [Pixabay](https://pixabay.com/).

### 🧾 **Description**

For object detection, three different Convolutional Neural Network architecture based models are implemented to detect objects from video. Initially, they are implemented on images, then on videos to check their detection and with what confidence score it detects and how long it takes to detect objects.

### 🧮 **What I had done!**

Since, the aim is to detect objects in videos, which is the sequence of frames, therefore detection using pretrained models are implemented on images and then on videos. The flow is as follows:

#### Frame Quality Analysis (Brightness and Contrast Over Time)
This is performed for detecting inconsistencies. Video might have variations in lighting due to changes in the environment, camera settings, or time of day. Analyzing brightness and contrast helps detect these inconsistencies.

#### Object detection using pretrained models

Here are the list of pretrained models that are used:

- MobileNet SSD
- Faster R-CNN
- YOLOv8

#### Object detection

Object detection is first performed on test images and then for videos, each frame is extracted and object detection is performed.

### 🚀 **Models Implemented**

Overall three models are implemented which are based on architecture of convolutional nueral network.

#### MobileNet SSD (Single Shot MultiBox Detector) - Convolutional Neural Networks (CNNs) based

Algorithms used in the MobileNet SSD model include:
- Convolutional Neural Networks (CNNs): These are used for feature extraction. MobileNet employs depthwise separable convolutions to reduce the number of parameters and computations.
- Single Shot Multibox Detector (SSD): This algorithm is used for object detection. It predicts bounding boxes and class probabilities directly from feature maps at multiple scales.

#### Faster R-CNN: Convolutional Neural Network based

- The model used is a Faster R-CNN (Region-based Convolutional Neural Network) architecture which uses a ResNet-50 backbone pretrained on the COCO dataset.

#### YOLO: Convolutional Neural Network based

- Here we are using the YOLOv8 model, which is an object detection model known for its speed and accuracy.
- YOLO models are based on convolutional neural networks (CNNs) and employ a single neural network to predict bounding boxes and class probabilities directly from full images in a single evaluation.

| Original Traffic Video | MobileNet SSD Object Detection |
| ---- | ---- |
| <img src="https://github.com/theiturhs/DL-Simplified/assets/96874023/761a40d4-e279-4bb1-841c-699fd3523f01" width="450"/> | <img src="https://github.com/theiturhs/DL-Simplified/assets/96874023/bd1b6839-7a5c-4ad2-ac30-4805bd6bf3d0" width="450" /> |
| Faster R-CNN Object Detection | YOLOv8 Object Detection |
| <img src="https://github.com/theiturhs/DL-Simplified/assets/96874023/ec9f8bb1-148b-4041-b231-11730b0183c4" width="450" /> | <img src="https://github.com/theiturhs/DL-Simplified/assets/96874023/2cc67bd2-bd94-4b8d-95b3-23798c947036" width="450" />

### 📚 **Libraries Needed**

- imutils
- numpy
- pandas
- torch
- torchvision
- Cython
- ultralytics

### 📊 **Exploratory Data Analysis Results**

#### Frame Quality Analysis (Brightness and Contrast Over Time)
This is performed for detecting inconsistencies. Video might have variations in lighting due to changes in the environment, camera settings, or time of day. Analyzing brightness and contrast helps detect these inconsistencies.

| ![image](https://github.com/theiturhs/DL-Simplified/assets/96874023/bfba124a-a9b1-4830-a114-11fcad4aae72) | ![image](https://github.com/theiturhs/DL-Simplified/assets/96874023/0f3c81ba-ca66-41f8-8784-cc86d3e64e69) |
| ---- | ---- |
| Brightness and Contrast are almost uniform for Video 1 | Brightness and Contrast are almost uniform for Video 2 |

Here is the object detection implementation on images

| Original Image 1 | MobileNet SSD Object Detection |
| ---- | ---- |
| ![image](https://github.com/theiturhs/DL-Simplified/assets/96874023/5e57ac4d-6b72-4031-acda-cbf82ffea71d) | ![MobileNet SSD Image 1](https://github.com/theiturhs/DL-Simplified/assets/96874023/755617b8-cc06-4401-889b-f459b02ed03b) |
| Faster R-CNN Object Detection | YOLOv8 Object Detection |
| ![Faster RCNN Image 1](https://github.com/theiturhs/DL-Simplified/assets/96874023/cfe96c21-fbc9-4714-8786-fa0a92deec1c) | ![YOLOv8 Image 1](https://github.com/theiturhs/DL-Simplified/assets/96874023/69e480c3-584c-433e-ace5-eed25d1a6a36) |


| Original Image 2 | MobileNet SSD Object Detection |
| ---- | ---- |
| ![highway-3392100_640](https://github.com/theiturhs/DL-Simplified/assets/96874023/767d441c-6330-4e8b-b658-7c21b9c6decf) | ![MobileNet SSD Image 2](https://github.com/theiturhs/DL-Simplified/assets/96874023/5fed5956-fb24-484a-9006-383ecd6f86bb) |
| Faster R-CNN Object Detection | YOLOv8 Object Detection |
| ![Faster RCNN Image 2](https://github.com/theiturhs/DL-Simplified/assets/96874023/ecbb1cb9-becd-4349-ab92-5e8f0d5bcdc5) | ![YOLOv8 Image 2](https://github.com/theiturhs/DL-Simplified/assets/96874023/4540bd42-dcef-4328-add4-4f260a88dca1) |


### 📈 **Performance of the Models based on the Accuracy Scores**

On the basis of detection done by these models, we can summarize them as:

1. In MobileNet SSD, the number of objects detected are less than other two models with average accuracies and takes less time to detect the objects.
2. In Faster RCNN, the accuracy with which it detects objects is greater than other two models, but it takes longer time to produce results.
3. In YOLOv8, it has better accuracy score as well as it takes less time than Faster RCNN to produce results.

Here are more video implementation of YOLOv8

| Video for Object Detection | Video: Object Detection |
| ---- | ---- |
| <img src="https://github.com/theiturhs/DL-Simplified/assets/96874023/5151d65a-b54e-40f5-ab63-8491ef6b8577" width="500"/> | <img src="https://github.com/theiturhs/DL-Simplified/assets/96874023/b9ce65dc-1255-47e9-8029-ee6e65084f52" width="500" /> |
| <img src="https://github.com/theiturhs/DL-Simplified/assets/96874023/f0ad6e08-236d-4d85-9d6d-e44fcf4ed888" width="500"/> | <img src="https://github.com/theiturhs/DL-Simplified/assets/96874023/ba0c77f1-a522-40b7-86b3-119b3f992e6d" width="500" /> |

### 📢 **Conclusion**

Performing detections on two videos by three models, it is concluded that

- Out of MobileNet SSD, Faster R-CNN and YOLOv8, two models detects objects with better confidence scores. These are Faster R-CNN model and YOLOv8 model.
- Along with this, Faster R-CNN took a very longer time than rest two models to detect objects, so overall YOLOv8 performs better.

### ✒️ **Your Signature**
**Shruti Shrivastava**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shrutikshrivastava/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:shrutishrivastava22ss@gmail.com)
[![Carrd](https://img.shields.io/badge/carrd-000000?style=for-the-badge&logo=carrd&logoColor=white)](https://theiturhs.carrd.co/)
[![Kaggle](https://img.shields.io/badge/kaggle-0077B5?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/theiturhs)
[![GitHub](https://img.shields.io/badge/github-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/theiturhs)

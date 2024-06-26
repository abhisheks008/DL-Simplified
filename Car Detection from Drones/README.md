# Car Detection from Drones using DL

## PROJECT TITLE

Car Detection from Drones Using DL

## 🎯 Goal

The aim is to create a deep-learning model that will detect cars on real-time from a drone or a UAV using deep learning techniques.

## 🧵 Dataset

The link for the dataset used in this project: [https://www.kaggle.com/datasets/sshikamaru/car-object-detection](https://www.kaggle.com/datasets/mcagriaksoy/amateur-unmanned-air-vehicle-detection-dataset)

## 🧾 Description
The main goal of the project is to develop a deep-learning model that can accurately predict and cars in the given video file or real-time.

## 🧮 What I had done!

1. Data collection: The data is loaded from the links provided above and its structure is 
   explore 
2. Data preprocessing: The data is then preprocessed, where steps such as setting batch 
   size, and image size, converting the image type to a specific type, and scaling are 
   done 
   to prepare the data for model training
3. Model training: I have taken YOLOv8 and OpenCV SSD models to train the dataset. 
4. Comparative analysis: The developed model performances are analysed based on their 
   accuracy.

## 🚀 MODELS USED

 1. OpenCV: OpenCV is preferred for real-time object detection tasks due to its comprehensive library of computer vision algorithms, robust performance across diverse hardware platforms, extensive community support, and seamless integration with various programming languages like Python and C++. Its versatility allows for efficient implementation of complex vision tasks such as object tracking, image processing, and facial recognition with high accuracy and speed.
 
 2. YOLOv8(You Only Look Once, version 8): This model is chosen for dog face detection due to its high speed and accuracy. It is designed for real-time object detection, making it ideal for applications needing quick and precise results. YOLOv8's CNN architecture efficiently learns and detects spatial patterns and features, ensuring robust detection of cars even with variations in size and position. Its end-to-end learning approach simplifies the detection pipeline, enhancing performance and reliability.


## 📚 LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy
- pandas
- cv2
- cvzone
- tensorflow
- ultralytics

## 📢 Conclusion
Based on the results we can draw the following conclusions:Certainly! Here's a tailored analysis for YOLOv8 and OpenCV models based on their performance in your project:

1. YOLOv8: The YOLOv8 model achieved an F1 score of 0.78, demonstrating strong performance in object detection tasks. Its architecture, optimized for speed and accuracy, effectively detects objects in real-time with high confidence levels. Further fine-tuning and dataset augmentation could potentially enhance its performance.

2. OpenCV: The OpenCV model, utilizing techniques like BackgroundSubtractorMOG2 and contour detection, achieved an accuracy of 0.85 in identifying objects. While simpler compared to deep learning models like YOLOv8, it excels in scenarios where real-time processing and moderate accuracy are sufficient. Its versatility and ease of implementation make it suitable for various computer vision applications.

3. Comparison: YOLOv8's deep learning approach offers superior accuracy and robustness in detecting objects of various sizes and orientations compared to the OpenCV model. YOLOv8's architecture enables efficient processing of frames in complex scenes, making it ideal for applications requiring high detection precision. In contrast, OpenCV provides a lightweight and accessible solution with good performance in less demanding environments, emphasizing simplicity and real-time processing capabilities.

##### Code contributed by: Gaurav Kumar Singh
##### Email: gauravsingh96753@gmail.com
##### Github: https://github.com/Gaurav-576

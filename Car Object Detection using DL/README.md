# Car Object Detection using DL

## PROJECT TITLE

Car Object Detection Using DL

## 🎯 Goal

The aim is to create a deep-learning model that will detect the cars in the image. 

## 🧵 Dataset

The link for the dataset used in this project: https://www.kaggle.com/datasets/sshikamaru/car-object-detection

## 🧾 Description
The main goal of the project is to develop a deep-learning model that can accurately predict and cars in the given image based on various features.

## 🧮 What I had done!

1. Data collection: The data is loaded from the links provided above and its structure is 
   explore 
2. Data preprocessing: The data is then preprocessed, where steps such as setting batch 
   size, and image size, converting the image type to a specific type, and scaling are 
   done 
   to prepare the data for model training
3. Model training: I have taken YOLOv8, VGG16 and Mobilenet SSD models to train the dataset. 
4. Comparative analysis: The developed model performances are analysed based on their 
   accuracy.

## 🚀 MODELS USED

 1. VGG16: VGG16 is chosen for dog face detection due to its pre-trained architecture on ImageNet, deep layers for learning intricate patterns, availability in frameworks like TensorFlow, and suitability for transfer learning, enabling effective model training even with limited data.
 
 2. YOLOv8(You Only Look Once, version 8): This model is chosen for dog face detection due to its high speed and accuracy. It is designed for real-time object detection, making it ideal for applications needing quick and precise results. YOLOv8's CNN architecture efficiently learns and detects spatial patterns and features, ensuring robust detection of cars even with variations in size and position. Its end-to-end learning approach simplifies the detection pipeline, enhancing performance and reliability.

 3. MobileNet SSD: This model is selected for dog face detection due to its lightweight architecture, designed for efficient inference on mobile and embedded devices. It balances between speed and accuracy, making it suitable for real-time applications. Additionally, MobileNet SSD offers object detection capabilities, allowing the model to detect and localize multiple objects, including cars, in an image efficiently.


## 📚 LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.26.2
- pandas==2.1.4
- matplotlib==3.8.2
- tensorflow==2.16.1
- ultralytics==8.2.14


## 📊 Exploratory Data Analysis Results
#### Accuracy and Loss of VGG16 Model:
![vgg_acc](https://github.com/Rithish5513U/DL-Simplified/blob/main/Car%20Object%20Detection%20using%20DL/Images/vgg_acc.png)

#### Accuracy and Loss of Mobilenet SSD model:
![mobilenet_acc](https://github.com/Rithish5513U/DL-Simplified/blob/main/Car%20Object%20Detection%20using%20DL/Images/mobilenet_acc.png)

#### Confidence of YOLOv8 Model:
![yolo_f1_curve](https://github.com/Rithish5513U/DL-Simplified/blob/main/Car%20Object%20Detection%20using%20DL/Images/yolo_f1_curve.png)


## 📈 Performance of the Models based on the Accuracy Scores
The evaluation metrics I used to assess the models:

- Accuracy score
- Loss Function


| Model      | Accuracy | Loss    |
|------------|----------|---------|
| VGG16    | 0.923     | 0.237   |
| YOLOv8    | 0.700     | -    |
| Mobilenet SSD    | 0.969     | 0.193    |

## 📢 Conclusion
Based on the results we can draw the following conclusions:
1. VGG16: The VGG16 model achieved a higher accuracy of 0.923 and a lower loss of 0.237. It outperformed the YOLOv8 model, indicating that the architecture of VGG16 with its specialized design for object detection could capture more complex features and generalize better.
2. YOLOv8: The YOLOv8 model achieved a F1 Confidence of 0.700. It performed reasonably well, but there is room for improvement.
3. Mobilenet SSD: The MobileNet SSD model achieved an accuracy of 0.969 and a loss of 0.193. It performed better than both the VGG16 and YOLOv8 models. MobileNet SSD's lightweight architecture and efficient design helped in achieving a high accuracy while maintaining computational efficiency.

##### Code contributed by: Rithish S
##### Email: rithish.satish@gmail.com

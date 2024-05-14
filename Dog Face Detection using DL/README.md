# Dog Face Detection using DL

## PROJECT TITLE

Dog Face Detection using DL

## 🎯 Goal

The aim is to create a deep-learning model that will detect the dog faces in the image. 

## 🧵 Dataset

The link for the dataset used in this project: https://www.kaggle.com/datasets/wutheringwang/dog-face-detectionyolo-format/code

## 🧾 Description
The main goal of the project is to develop a deep-learning model that can accurately predict and detect dog face in the given image based on various features.

## 🧮 What I had done!

1. Data collection: The data is loaded from the links provided above and its structure is 
   explore 
2. Data preprocessing: The data is then preprocessed, where steps such as setting batch 
   size, and image size, converting the image type to a specific type, and scaling are 
   done 
   to prepare the data for model training
3. Model training: I have taken YOLOv8 model to train the dataset. I chose this model 
   because of the detection task. It performs well at object detection and created 
   particularly for tis purpose.  
5. Performance analysis: The developed model performance is analysed based on their 
   accuracy.

## 🚀 MODELS USED

 1. YOLOv8(You Only Look Once, version 8): This model is chosen for dog face detection due to its high speed and accuracy. It is designed for real-time object detection, making it ideal for applications needing quick and precise results. YOLOv8's CNN architecture efficiently learns and detects spatial patterns and features, ensuring robust detection of dog faces even with variations in size and position. Its end-to-end learning approach simplifies the detection pipeline, enhancing performance and reliability.


## 📚 LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.26.2
- pandas==2.1.4
- matplotlib==3.8.2
- tensorflow==2.16.1
- ultralytics==8.2.14

## 📊 Exploratory Data Analysis Results
#### Confidence Curve:
![F1_curve](https://github.com/Rithish5513U/Dog_Face_Detection_using_DL/blob/main/Dog%20Face%20Detection%20using%20DL/Images/F1_curve.png)

#### Precision-Recall Curve:
![PR_curve](https://github.com/Rithish5513U/Dog_Face_Detection_using_DL/blob/main/Dog%20Face%20Detection%20using%20DL/Images/PR_curve.png)

#### Precision-Confidence Curve:
![P_curve](https://github.com/Rithish5513U/Dog_Face_Detection_using_DL/blob/main/Dog%20Face%20Detection%20using%20DL/Images/P_curve.png)

#### Recall-Confidence Curve:
![R_curve](https://github.com/Rithish5513U/Dog_Face_Detection_using_DL/blob/main/Dog%20Face%20Detection%20using%20DL/Images/R_curve.png)


## 📈 Performance of the Models based on the Accuracy Scores
The evaluation metrics I used to assess the models:

- Confidence Curve
- Precision-Recall Curve
- Precision-Confidence Curve
- Recall-Confidence Curve


## 📢 Conclusion
Based on the results we can draw the following conclusions:
1. YOLOv8: The YOLOv8 model performed exceptionally well in dog face detection:
- Confidence Curve: High confidence levels in predictions.
- Precision-Recall Curve: Excellent balance of precision and recall.
- Precision-Confidence Curve: High precision across varying confidence thresholds.
- Recall-Confidence Curve: Strong recall across different confidence levels.

##### Code contributed by: Rithish S
##### Email: rithish.satish@gmail.com

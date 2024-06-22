# Global Land Cover Mapping using Image Processing

## Project Title

Global Land Cover Mapping using Image Processing

## 🎯 Goal

The aim is to create a deep-learning model that will detect and classify the different types of land cover. 

## 🧵 Dataset

The link for the dataset used in this project: https://www.kaggle.com/datasets/aletbm/global-land-cover-mapping-openearthmap

## 🧾 Description
The main goal of the project is to develop a deep-learning model that can accurately predict the type of land cover in a given image based on various land features.

## 🧮 What I had done!

1. Data collection: The data is loaded from the links provided. 
    It was my first time dealing with .tif images, so I spent a fair bit of time exploring the dataset.
   
2. Data preprocessing: The data is then preprocessed, where steps such as setting batch
   size, and image size, converting the image type to a specific type, and scaling are 
   done.
   As I was dealing with .tif images where each image has 3 layers and the labels for each class had to be        extracted separately.
   I used the DBScan clustering technique to draw bounding boxes around the clusters of a specific class.
   
3. Model training: I have taken YOLOv5, VGG16, and RetinaNet models to train the dataset.
   
4. Comparative analysis: The developed model performances are analyzed based on their 
   accuracy.

## 🚀 MODELS USED

 1.  YOLOv5(You Only Look Once, version 5): This model is chosen for land cover classification due to its high accuracy and efficiency. Designed for real-time classification, it is ideal for applications requiring quick and precise results. YOLOv5's CNN architecture effectively learns and identifies spatial patterns, ensuring robust classification of various land cover types. Its end-to-end learning approach simplifies the classification pipeline, enhancing performance and reliability.

 2. RetinaNet: RetinaNet is chosen for land cover classification due to its high accuracy and robustness. It is designed for real-time classification, making it ideal for applications requiring precise results. RetinaNet's Focal Loss function effectively handles class imbalance, ensuring accurate classification of diverse land cover types. Its deep learning architecture captures intricate spatial patterns, enhancing performance and reliability.
 
 3. VGG16: VGG16 is chosen for landcover detection due to its pre-trained architecture on ImageNet, deep layers for learning intricate patterns, availability in frameworks like TensorFlow, and suitability for transfer learning, enabling effective model training even with limited data.

## 📚 LIBRARIES NEEDED

The following libraries are required to run this project:
- absl-py==2.1.0
- astunparse==1.6.3
- charset-normalizer==3.3.2
- cligj==0.7.2
- Cython==3.0.10
- flatbuffers==24.3.25
- gast==0.5.4
- google-pasta==0.2.0
- grpcio==1.64.1
- h5py==3.11.0
- idna==3.7
- keras==3.3.3
- keras-resnet==0.2.0
- libclang==18.1.1
- Markdown==3.6
- markdown-it-py==3.0.0
- MarkupSafe==2.1.5
- mdurl==0.1.2
- mkl-service==2.4.0
- ml-dtypes==0.3.2
- namex==0.0.8
- opencv-python==4.10.0.84
- opt-einsum==3.3.0
- optree==0.11.0
- ply==3.11
- progressbar2==4.4.2
- protobuf==4.25.3
- Pygments==2.18.0
- PyQt5==5.15.10
- pyscilab==1.0.7.dev1
- python-utils==3.8.2
- requests==2.32.3
- rich==13.7.1
- scilab2py==0.6.2
- tensorboard==2.13.0
- tensorboard-data-server==0.7.2
- tensorflow==2.13.1
- tensorflow-estimator==2.13.0
- tensorflow-io-gcs-filesystem==0.34.0
- tensorrt==10.1.0
- tensorrt-cu12==10.1.0
- tensorrt-cu12-bindings==10.1.0
- tensorrt-cu12-libs==10.1.0
- termcolor==2.4.0
- typing_extensions==4.12.2
- urllib3==2.2.2
- Werkzeug==3.0.3
- wrapt==1.16.0

## 📊 Exploratory Data Analysis Results

#### YOLOv5 Model:

![yolo_f1_curve](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/yolo_F1_curve.png)

![yolo_confusion_matrix](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/yolo_confusion_matrix.png)

![yolo_labels](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/yolo_labels.jpg)

![yolo_results](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/yolo_results.png)

#### RetinaNet Model:

![retinanet_epoch_loss](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/retinanet_epoch_loss.png)

![retinanet_epoch_mAP](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/retinanet_epoch_mAP.png)

![retinanet_regression_loss](https://github.com/ArismitaM/DL-Simplified/blob/main/Global%20Land%20Cover%20Mapping%20using%20Image%20Processing/Images/retinanet_regression_loss.png)

## 📈 Performance of the Models based on the Accuracy Scores
The evaluation metrics I used to assess the models were epoch loss

| Model      | Epoch Loss |
|------------|----------|
| YOLOv5    | 0.020     |
| RetinaNet    | 7.188 |
| VGG16   |    -     |

## 📢 Conclusion
Based on the results we can draw the following conclusions:
1. YOLOv5: The YOLOv5 model had an epoch loss of 0.020. This loss was lower compared to RetinaNet, hence it outperformed the RetinaNet model.

2.RetinaNet: I was successfully able to train YOLO using my GPU. However, that was not the case with RetinaNet. My GPU ran out of memory so I had to train this model using CPU. This had an epoch loss of 7.188. This was higher than the YOLOv5 model.  

3. VGG16: I initially attempted to use VGG as one of my models. However, later in the process, I realized that VGG was ideal for object detection and not classification. Therefore, this model would work properly only if there was 1 class. But, in my case, I had 9 classes, so I could not continue using this model.
   
##### Code contributed by: Arismita Mukherjee
##### Email: arismita08.m@gmail.com

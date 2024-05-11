# CCTV-HUMAN-DETECTION

 ![image.png](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrLn9Zzwpzvpp2FLu0n8bdwOIR26fARzsV4A&usqp=CAU)

# GOAL
Detecting humans from CCTV Images

# DESCRIPTION
This is a tutorial demonstrating how to train a YOLOv4 people detector using [Darknet](https://github.com/AlexeyAB/darknet) and the Kaggle Human dataset,, which contains annotated images of people in various scenarios. YOLOv4 is a state-of-the-art object detection model known for its speed and accuracy, making it suitable for real-time applications such as surveillance and autonomous vehicles. Follow along to understand the process of training your own custom object detector to detect people in images and video streams.


# DATASET
The dataset for this project is taken from the Kaggle website. Here is the link for the dataset,https://www.kaggle.com/datasets/jonathannield/cctv-human-pose-estimation-dataset.

Here in the dataset you will find the various human images captured through CCTV cameras installed on various places.
But the dataset is not suitable for training for Yolo model.So,first we annotate the data according to format provided by Yolo.
We used LabelIMG to annotate image.

You can refer to https://machinelearningknowledge.ai/train-custom-yolov4-model-for-object-detection-in-google-colab/ for custom data preparation.


# WHAT I HAD DONE

* The script detects objects using YOLOv4 model with Darknet, configurable through command-line arguments.
* [Setup](#setup)
* [Preparing training data](#preparing)
- It supports both image and video inputs, including live streams from webcams and various protocols.
* [Training on a local PC](#training-locally)
- Detection results can be displayed, saved as images or videos, and exported as text files. 
- The script utilizes PyTorch for inference and CUDA for GPU acceleration if available.
- Training the model requires GPU.If GPU is not there then use google colab for training the model.Refer the yolo_model.ipynb file for detailed procedure of training and testing. 

* [Testing the custom-trained yolov4 model](#testing)

# MODEL IMPLEMENTED
##### DARKNET:-
Darknet, the neural network framework developed by Joseph Redmon, has been instrumental in the evolution of YOLO models and numerous other deep learning projects. Offering flexibility and efficiency, Darknet serves as the backbone for implementing cutting-edge algorithms like YOLOv4 and YOLOv7. Its modular architecture facilitates rapid prototyping and experimentation, enabling researchers and developers to push the boundaries of object detection and recognition. Moreover, Darknet's open-source nature fosters collaboration and innovation within the computer vision community, driving continual advancements in human detection and beyond.

##### YOLO4:-
You Only Look Once (YOLO) version 4 (YOLOv4) has been a significant advancement in human detection from CCTV footage, offering real-time processing capabilities and improved accuracy compared to its predecessors. YOLOv4 utilizes a single neural network to predict bounding boxes and class probabilities directly from full images in one evaluation. While it excels in detecting human figures swiftly and accurately, it falls short in discerning finer details such as facial features or subtle gestures. This limitation poses a challenge in scenarios where identifying specific individuals or analyzing intricate behaviors is crucial, highlighting the need for further refinement in detection algorithms.

##### YOLO7:-
In contrast, YOLO version 7 (YOLOv7) represents the latest evolution in human detection technology, boasting enhanced performance and robustness over YOLOv4. With advancements in model architecture and training techniques, YOLOv7 demonstrates superior accuracy in identifying human subjects from CCTV feeds while also addressing some of the limitations of its predecessors. Its improved ability to capture finer details ensures better recognition of human attributes and behaviors, making it a preferred choice for applications requiring precise analysis and tracking in complex environments.

# LIBRARIES NEEDED

# EDA RESULTS
#### Approach Using Yolov4
![image.png](https://miro.medium.com/max/785/1*f2diI7O28j2A875FwQPMJA.jpeg)
This model fails to perform with distant and finer object.

#### Approach Using Yolov7
![image.png](https://github.com/WongKinYiu/yolov7/raw/main/figure/performance.png)
This model performs much better than Yolov4 on distant objects

# COMPARING PERFORMANCE


# CONCLUSION
We have implemented two different approach Yolov4 and Yolov7 and, Yolov7 gives the best accuracy.

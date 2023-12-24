**HEAT SINK DEFECT DETECTION**

**GOAL**

To detect stains and scratches on the given heat sink images.

**DATASET**

https://www.kaggle.com/datasets/kaifengyang/heat-sink-surface-defect-dataset

**DESCRIPTION**

This project aims to develop a robust defect detection system utilizing U-Net architecture models, an effective neural network design for image segmentation tasks. By harnessing deep learning techniques, this project strives to accurately identify and localize defects within heat sinks.


**MODELS USED**

U-net - U-Net, a deep learning architecture, excels in image segmentation tasks. Its unique design incorporates encoder-decoder pathways, ideal for precise localization, widely applied in medical imaging and object detection.

Resnet50 - ResNet-50 is a 50-layer convolutional neural network (48 convolutional layers, one MaxPool layer, and one average pool layer). Residual neural networks are a type of artificial neural network (ANN) that forms networks by stacking residual blocks. It excels in image recognition tasks, offering high accuracy and efficiency in deep learning models.

Vgg16 - VGG16 is a deep convolutional neural network renowned for its 16 layers, characterized by a simple yet effective architecture. Its design, with small receptive fields and stacked layers, excels in image classification tasks, making it a popular choice for feature extraction and transfer learning in computer vision applications.

**ACCURACIES**

All 3 models gave accuracies of 97.8% on training upon 40 epochs of batch size 32.

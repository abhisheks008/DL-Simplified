# <h1 align = "center"> Durum Wheat Classification using DL </h1>
## Aim of the project: 
### The project focuses on identification of different wheat types and foreign matters using various Deep Learning Algorithms.

###  Libraries and Frameworks used:
1. Pandas
2. Numpy 
3. Matplotlib
4. Seaborn
5. Tensorflow
6. Keras
7. sklearn
8. glob
9. OpenCV


## Deep Learning Algorithms used:
1. InceptionNet
2. ResNet
3. DenseNet
4. EfficientNet

## Accuracy and training time comparison of all the Deep Learning Algorithms
|                    |   Accuracy    |
|--------------------|---------------|
|    InceptionNet    |     22%       |
|       ResNet       |     45%       |  
|      DenseNet      |     50%       |   
|    EfficientNet    |     50%       |   

# Representation of Durum Wheat
![EDA](https://github.com/the-silent-geek/DL-Simplified/blob/9f6fb51986e4b450ba8c205aa3037fbc3d702d44/Durum%20Wheat%20Classification%20using%20DL/images/eda.png)

# Orignal image vs grayscale image
![ovsg](https://github.com/the-silent-geek/DL-Simplified/blob/9f6fb51986e4b450ba8c205aa3037fbc3d702d44/Durum%20Wheat%20Classification%20using%20DL/images/original%20vs%20grayscale.png)

# Original vs Resized image(224*224 pixels)
![ovri](https://github.com/the-silent-geek/DL-Simplified/blob/9f6fb51986e4b450ba8c205aa3037fbc3d702d44/Durum%20Wheat%20Classification%20using%20DL/images/original%20vs%20resized.png)

# Data Augmentation (Flipped image)
![Flipped]()

# Data Augmentation (Rotated image)
![rotated](https://github.com/the-silent-geek/DL-Simplified/blob/9f6fb51986e4b450ba8c205aa3037fbc3d702d44/Durum%20Wheat%20Classification%20using%20DL/images/rotated.png)

# Accuracy plots of all models

## InceptionNet
![in](https://github.com/the-silent-geek/DL-Simplified/blob/9f6fb51986e4b450ba8c205aa3037fbc3d702d44/Durum%20Wheat%20Classification%20using%20DL/images/inceptionNet.png)

## DenseNet
![densenet](https://github.com/the-silent-geek/DL-Simplified/blob/9f6fb51986e4b450ba8c205aa3037fbc3d702d44/Durum%20Wheat%20Classification%20using%20DL/images/DenseNet.png)

## ResNet
![resnet](https://github.com/the-silent-geek/DL-Simplified/blob/9f6fb51986e4b450ba8c205aa3037fbc3d702d44/Durum%20Wheat%20Classification%20using%20DL/images/ResNet50.png)

## EfficientNet
![resnet](https://github.com/the-silent-geek/DL-Simplified/blob/9f6fb51986e4b450ba8c205aa3037fbc3d702d44/Durum%20Wheat%20Classification%20using%20DL/images/efficientnet.png)

# Conclusion
ResNet50 model performs better comparative to other models used on the above dataset.

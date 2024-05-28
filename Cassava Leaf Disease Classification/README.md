# <h1 align = "center"> Cassava Leaf Disease Classification</h1>
## Aim of the project: 
The aim of this project is to identify the defected leaf of the Cassava plant using Computer Vision and image processing methods.

##  Libraries and Frameworks used:
1. Pandas
2. Numpy 
3. Matplotlib
4. Seaborn
5. Tensorflow
6. Scikit-Learn
7. OpenCV


## Deep Learning Algorithms used:
1. EfficientNetB1
2. InceptionV3
3. DenseNet121
4. MobileNetV2

## Accuracy and training time comparison of all the Deep Learning Algorithms

|                |   Accuracy    |
|----------------|---------------|
| EfficientNetB1 |     90%       |
| InceptionV3    |     92%       |  
| DenseNet121    |     81%       |     
| MobileNetV2    |     86%       |

# Representation of types of cells
![EDA](./Images/sample_images.png)

# Accuracy and loss plots of all models

## EfficientNetB1
![EfficientNetB1](./Images/efficientnet_plots.png)

## InceptionV3
![InceptionV3](./Images/inceptionv3_plots.png)

## DenseNet121
![DenseNet121](./Images/densenet_plots.png)

## MobileNetV2
![MobileNetV2](./Images/mobilenetv2_plots.png)

# Confusion Matrices of all models

## EfficientNetB1
![EfficientNetB1_CM](./Images/efficientnet_cm.png)

## InceptionV3
![InceptionV3_CM](./Images/inceptionv3_cm.png)

## DenseNet121
![DenseNet121_CM](./Images/densenet_cm.png)

## MobileNetV2
![MobileNetV2_CM](./Images/mobilenet_cm.png)

# Conclusion
As evident from the plot below, InceptionV3 model performs better comparative to other models used on the above dataset with an accuracy of 74.4% on the test set.
![comparison](./Images/model_comparison.png)
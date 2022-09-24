# Military Aircraft Detection 
This project is an attempt to develop and train a neural Network model to classify the images of 40 of the best military fighter aircrafts collected from Google Images. I have used some of the best pretrained deep convolutional neural networks in roder to classify them efficiently. This project is a part of Social Summer of Code(SSOC) and is presented to the project DL-Simplified.

## How to install requirements
```
pip install -r requirements.txt (Python 2), or
pip3 install -r requirements.txt (Python 3)
```
## About Dataset
The dataset used here is provided at https://www.kaggle.com/datasets/a2015003713/militaryaircraftdetectiondataset.

The dataset consists of 12337 images that are divided into 40 categories of Aircrafts that 
are collected from Google Images. Since the author is not sure about the copyright of the images, there is no license to the images. So I would like to declare that the data I have used here is only used for purely research and academic(non-commercial) purpose. 
So I took the following optimizations in order to decrease the computation time and increase the accuracy of the output.
- Converting the variable sized images into standard sizes of 224 X 224 so that they can be supplied to each next layer(ReSize)
- For images smaller than 224X224, I want randomcrop and padding(reflecting) enacbled as it can help increase the amount of data provided by low resolution images
- Then the images are converted into pytorch tensors
- Then the images are normalized using empirical values of mean and standard deviation

## The Model
So the model I have used here is here is ResNet, EfficientNet and GoogleNet, commom industry standard models developed by researchers at Microsoft and Google respectively.
#### ResNet
<img src="./Images/Residual-Block.PNG" width="800" title="ResNet Model">
<p>Source: Google Images</p>

#### EfficientNet
<img src="./Images/EfficinetNet.png" width="800" title="EfficientNet Model">
<p>Source: Google Images</p>

#### GoogleNet
<img src="./Images/CNN-architecture-based-on-GoogLeNet-model.ppm.png" width="800" title="GoogleNet Model">
<p>Source: Google Images</p>

## Training and Testing of the Model
ResNet took approximately 22 minutes each to be fine-tuned and generate accurate results.And the EfficientNet and GoogleNet took approximately 30 minutes and 35 minutes of computational time respectvely. All models were trained on GoogleColab using 12 GB free GPU provided by Colab.

| Models | Best Train-Accuracy | Best Validation-Accuracy | Computation-Time| Number of Epochs|
|--------|---------------------|--------------------------|-----------------|-----------------|
| ResNet-18 | 75.81% | 57.92% | 22m 1s | 8 |
| GoogleNet | 13.16%  | 13.1939% | 30m 35s | 10 |
| EfficientNet | 8.47% | 9.7345% | 35m 57s | 8 |

## Conclusion

So the best model selected is going to be ResNet which is a very good model for Image Recognition. For more information on ResNet, read https://arxiv.org/abs/1512.03385

## Courses I followed to Build the Model 
- Michigan's Deep Learning for Computer Vision
(https://www.youtube.com/playlist?list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)
- Pytorch Tutorials
(https://www.youtube.com/playlist?list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4)

## Developer Details
Developed By Aryan Gupta 
(Electrical Engineering Student, IIT Roorkee)

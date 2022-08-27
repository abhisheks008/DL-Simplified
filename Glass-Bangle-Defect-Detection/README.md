# Glass Bangle Defects Detection
In this project, I have tried to come up with a deep convolutional model in order to classify the glass bangles based on their condition i.e. ["good", "defected", "broken"]. I had tried to develop the model myself using knowledge from various courses I referenced during the course of the project.

## How to install requirements
Run pip install -r requirements.txt (Python 2),
or pip3 install -r requirements.txt (Python 3)

## Dataset
The dataset I used is available on Kaggle as https://www.kaggle.com/datasets/almique/glass-bangle-defect-detection-classification
Since one of the most crucial aspects of bangle manufacturing process is to make sure bangles come out round and without defects. We have compiled a dataset which consists of human-labeled images collected from one of the bangle factories. The dataset consist total of 1080 images consisting broken, defected and good bangle images.
The dataset was with images if pixel density 3000x3000 and I had to reduce it to  500x500 in order for the GPU to render it. I also normalized the images to reduce overfitting.

## The Model
So the model I have used here is here is a simple CNN based model that has 1 CNN layer, followed by one pooling payer (MaxPool) and two fully connected layer.

<img src="./Images/CNN model.png" width="350" title="CNN Model">
<p>Source: https://medium.com/analytics-vidhyaintroduction-to-cnn-and-corona-virus-prediction-through-ct-scan-c9d6dbd67d26</p>

## Training and Testing of the Model
I trained the model using googlecolab and it took approximate 1 Hour of computation time on the GPU runtime. 
On testing the model with random images from the trainset onl, it generated an accuracy of 53.33% which means the model has learnt properties in the training. One can also use tranfer learning in order to train on the images from pretrained models like EfficientNet or MobileNet.

## Courses I followed to Build the Model 
- Michigan's Deep Learning for Computer Vision
(https://www.youtube.com/playlist?list=PL5-TkQAfAZFbzxjBHtzdVCWE0Zbhomg7r)
- Pytorch Tutorials
(https://www.youtube.com/playlist?list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4)

## Developer Details
Developed By Aryan Gupta 
(Electrical Engineering Student, IIT Roorkee)

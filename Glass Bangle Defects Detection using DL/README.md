# Glass Bangle Defects Detection
In this project, I have tried to come up with a deep convolutional model in order to classify the glass bangles based on their condition i.e. ["good", "defected", "broken"]. I had tried to develop the model myself using knowledge from various courses I referenced during the course of the project.

## How to install requirements
Run pip install -r requirements.txt (Python 2),
or pip3 install -r requirements.txt (Python 3)

## About Dataset
The dataset used here is provided at https://www.kaggle.com/datasets/almique/glass-bangle-defect-detection-classification.
Since one of the most crucial aspects of bangle manufacturing process is to make sure bangles come out round and without defects. We have compiled a dataset which consists of human-labeled images collected from one of the bangle factories. The dataset consist total of 1080 images consisting broken, defected and good bangle images.

The data images(about 1080 in number) were especially large (3000X3000 pixels). So I took the following optimizations in order to decrease the computation time and increase the accuracy of the output.
- Random Horizontal flip
- Resizing the images to (224 X 224) using Resize function in Pytorch Data Trasforms
- Normalized the data images using empirical values of mean and standard deviation.
- Finally all images were converted into batches and loaded into the pytorch model

- For CNN with Attention, we took images as 400 X 400, normalized them, and then flipped the colour intensity to highlight contours better.

## The Model
So the model I have used here is here is ResNet and GoogleNet, commom industry standard models developed by researchers at Microsoft and Google respectively.

#### ResNet
<img src="./Images/Residual-Block.PNG" width="800" title="CNN Model">

#### GoogleNet
<img src="./Images/CNN-architecture-based-on-GoogLeNet-model.ppm.png" width="800" title="CNN Model">
<p>Source: Google Images
</p>

#### Custom-Model
Also I have made a custom model using one convolutional layer and 2 fully connected layers in order to display the internal working of the CNN-architecture based Neural Networks.

<img src="./Images/Residual-Block.PNG" width="800" title="CNN Model">

#### CNN

A Deep neural network model which has feature selection and feature training components.

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/enhance_bangle_defect/Glass%20Bangle%20Defects%20Detection%20using%20DL/Images/CNN-Keras.png">

#### CNN with Attention

A Deep neural network model which has feature selection and feature training components, with an overhead attention mechanism to introduce probability distributions into training.

<img src="https://github.com/Arihant-Bhandari/DL-Simplified/blob/enhance_bangle_defect/Glass%20Bangle%20Defects%20Detection%20using%20DL/Images/CNN-Keras-Attention.png">

## Training and Testing of the Model
ResNet and GoogleNet took approximately 19 minutes each to be fine-tuned and generate accurate results.And the custom model took approximately 30 minutes of computational time. All models were trained on GoogleColab using 12 GB free GPU provided by Colab. CNN-Keras and Attention were trained on Kaggle with GPU-T4 boosting.

| Models | Best Train-Accuracy | Best Validation-Accuracy | Computation-Time| 
|--------|---------------------|--------------------------|-----------------|
| ResNet-18 | 86.21% | 89.8618% | 19m 31s |
| GoogleNet | 74.62%  | 77.8802% | 19m 42s | 
| Custom Model | 53.548% | 53.548 % | 30 minutes | 
| CNN (Keras) | 89.9% | 81.4% | 2.5 minutes | 
| CNN (Keras-Attention) | 99.32% | 88.27% | 1.67 minutes | 

## Conclusion

So the best model selected is going to be ResNet which is a very good model for Image Recognition, and another model to be considered is CNN with Attention mechanism with comes just as close.

## Your signature
Original Contribution: Aryan Gupta 

README and Model enhanced by: Arihant Bhandari [https://github.com/Arihant-Bhandari]

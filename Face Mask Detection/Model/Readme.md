# Face mask detection with Tensorflow CNNs

COVID-19 has been an inspiration for many software and data engineers during the last months.
This project demonstrates how a Convolutional Neural Network (CNN) can detect if a person in a picture is wearing a face mask or not.
As you can easily understand the applications of this method may be very helpful for the prevention and the control of COVID-19 as it could be used in public places like airports, shopping malls etc.

## Defining the problem
Detecting if an image contains a person wearing a mask or not is a simple **classification problem**.
We have to classify the images between **2 discrete classes**: The ones that contain a face mask and the ones that do not.

## The dataset
https://www.kaggle.com/datasets/shiekhburhan/face-mask-dataset

<img width="258" alt="Face Images" src="https://github.com/ranodeepbanerjee/DL-Simplified/assets/63450189/e574ae40-6780-48fb-843d-43d835d2b12e">


## Image classification and CNNs
A bit of theoretical background first.
Convolutional Neural Networks (CNN) are neural networks most commonly used to analyze images.
A CNN receives an image as an input in the form of a 3D matrix. The first two dimensions corresponds to the width and height of the image in pixels while the third one corresponds to the RGB values of each pixel. 

CNNs consist of the following sequential modules (each one may contain more than one layer)

1. Convolution
2. ReLu activation function
3. Pooling
4. Fully connected layers
5. Output layer

### Convolution
Convolution operation is an element wise matrix multiplication operation.
Convolutional layers take the three-dimensional input matrix we mentioned before and they pass a **filter** (also known as convolutional kernel) over the image, applying it to a small window of pixels at a time (i.e 3x3 pixels) and moving this window until the entire image has been scanned. The convolutional operation calculates the dot product of the pixel values in the current filter window along with the weights defined in the filter. The output of this operation is the final convoluted image.

The following animation (found in [Google developers portal](https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks)) shows how the sliding o the window is performed over an image
![Window sliding](https://developers.google.com/machine-learning/practica/image-classification/images/convolution_overview.gif)

The core of image classification CNNs is that as the model trains what it really does is that **it learns the values for the filter matrices that enable it to extract important features** (shapes, textures, colored areas etc) in the image. Each convolutional layer applies one new filter to the convoluted image of the previous layer that can extract one more feature. So, as we stack more filters, the more features the CNN can extract from an image. 

### ReLu activation function
After each convolution operation, CNN applies to the output a **Rectified Linear Unit** (ReLu) function to the convolved image. 
As you may remember from the Machine Learning 101 course in university, ReLu is very commonly used in machine learning applications because it introduces nonlinearity into the model. This helps our model to **generalize better** and avoid overfitting.

### Pooling 
Pooling is the process where the CNN downsamples the convolved image by reducing the number of dimensions of the feature map.
It does so to reduce processing time and the computing power needed.
During this process, it preserves the most important feature information. There are several methods that can be used for pooling. The most common ones are **Max pooling** and **Average pooling**.
In our application, we will use max pooling as it is the most effective most of the times.
Max pooling is very similar to the convolution process. A windows slides over the feature map and extracts tiles of a specified size. For each tile, max pooling picks the maximum value and adds it to a new feature map.

The following animation (found in [Google developers portal](https://developers.google.com/machine-learning/practica/image-classification/convolutional-neural-networks)) shows how max pooling operation is performed.
![Max Pooling](https://developers.google.com/machine-learning/practica/image-classification/images/maxpool_animation.gif)

### Fully connected layers
After pooling, there is always one or more fully connected layers. These layers perform the classification based on the features extracted from the image by the previously mentioned convolution processes. The last fully connected layer is the output layer which applies a softmax function to the output of the previous fully connected layer and returns a probability for each class.

The general form of an image classification CNN is the one shown below:
![image classification CNN](https://dev-to-uploads.s3.amazonaws.com/i/f3qp9loy9io16d3x5sjm.png)


### Results
<img width="289" alt="loss vs val_loss" src="https://github.com/ranodeepbanerjee/DL-Simplified/assets/63450189/0fb59d1d-5d62-4c34-b44b-be06a001b862">

<img width="272" alt="Categorical accuracy vs Val_categorical Accuracy" src="https://github.com/ranodeepbanerjee/DL-Simplified/assets/63450189/cdd13ae8-877d-44c2-894f-06763883f668">


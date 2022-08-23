## SARS COV 2 CT Scan Classification ##

### Goal ###
The goal of this project is to create a deep learning - image processing model which can identify the CT scan images of SARS COV 2 affected patients.

### Dataset ###
The dataset is collected from the following link,
https://www.kaggle.com/datasets/plameneduardo/sarscov2-ctscan-dataset

### Approach ###
Using 3 differnent algorithms to implement the models and comparing all the algorithms to find out the best fitted algorithm for the model by checking the accuracy
scores and performing data visualization and prediction

## Creating Training Dataset ##
Selecting Data directory and Categories: COVID & non-COVID
![image](https://user-images.githubusercontent.com/83596240/184601190-78fd0821-e5b2-4434-9dec-fa058c5b86f3.png)

![image](https://user-images.githubusercontent.com/83596240/184599934-1822a083-f0d7-473b-8dcf-0104b3d6f18a.png)

## Randomizing the dataset to prevent accidental bias and to help the training converge faster ##

![image](https://user-images.githubusercontent.com/83596240/184601066-84e7ce33-4940-4581-8ef9-8c55ccdf1ec8.png)

## Plotting Frequency Histogram of the created Dataset ##

![image](https://user-images.githubusercontent.com/83596240/184602162-237d60a0-6540-4f55-889c-ed1c7c12d666.png)

## Displaying images of COVID class from training Dataset ##

![image](https://user-images.githubusercontent.com/83596240/184603152-a77f8dc3-c820-40e0-a57b-23fb5c8a1062.png)

## Displaying images of non-COVID class from training Dataset ##

![image](https://user-images.githubusercontent.com/83596240/184603189-9cd013d7-5dfe-47db-852a-bf37dec281c7.png)

## Reading the images and resizing them to target size and Normalize the training dataset to change the values of dataset to a common scale, without distorting differences in the range of values ##

![image](https://user-images.githubusercontent.com/83596240/184603662-67259183-dea5-44f6-8b75-08f25578fcdd.png)

## Converting Labels to Categorical ##

![image](https://user-images.githubusercontent.com/83596240/184604052-fbb06524-c47a-4ad2-a441-a9d58803e49c.png)

## Spliting the created dataset into the training and validation sets for model building ##

![image](https://user-images.githubusercontent.com/83596240/184604005-68a1bf73-eabf-48f8-8c19-9aee5a8ab155.png)

## Setting the epoch, image size, batch size and no of channels and Creating the model ##
### 1. For MobileNetV2 model ###
![image](https://user-images.githubusercontent.com/83596240/184604413-74dc1bd9-cc25-4307-9c47-b01c5d0cbe12.png)

![image](https://user-images.githubusercontent.com/83596240/184604830-82cadbf6-8928-42dd-a589-8a0ae7b7ded4.png)

### 2. For InceptionV3 model ###

![image](https://user-images.githubusercontent.com/83596240/184604964-7203c761-bdd9-483a-8a09-66e70bdebeed.png)

### 3. For keras-VGG19 model ###

![image](https://user-images.githubusercontent.com/83596240/184605414-e412c395-ccb9-4374-a225-18923da2194b.png)

## Performing Data Augmentation for all the three model to prevent overfitting when training the model ##

![image](https://user-images.githubusercontent.com/83596240/184605343-7e73c1de-1ad5-495c-88c6-c3c2ca1a7f36.png)

## Training all the MobileNetV2, InceptionV3 and VGG19 model ###

![image](https://user-images.githubusercontent.com/83596240/184606808-5e0035af-c58b-4de6-b571-c01e18974504.png)

## Comparing the final accuracy and loss of the above three models ##

### 1. For MobileNetV2 model ###

![image](https://user-images.githubusercontent.com/83596240/184608080-670febc8-15b5-4cdc-adb2-af3e9b60d7eb.png)

### 2. For InceptionV3 model ###

![image](https://user-images.githubusercontent.com/83596240/184608245-2054cf9e-d0e6-4132-ba16-dab68418b895.png)

### 3. For VGG19 model ###

![image](https://user-images.githubusercontent.com/83596240/184608479-be495d09-11fe-4265-ab68-813cd90c03ee.png)

### Comparing the Confusion Matrix for all the three model ###

### 1. For MobileNetV2 model ###

![image](https://user-images.githubusercontent.com/83596240/184609020-a2f5ba87-66a7-4553-ab77-943993cd4a8c.png)
![image](https://user-images.githubusercontent.com/83596240/184608845-40f22a87-b361-407d-860d-00c2098c332c.png)

### 2. For InceptionV3 model ###

![image](https://user-images.githubusercontent.com/83596240/184608794-36e48f63-1297-482c-b5b5-140c84561e8f.png)
![image](https://user-images.githubusercontent.com/83596240/184609142-7b628b22-da39-434e-a619-840e2f3e1253.png)

### 3. For VGG19 model ###

![image](https://user-images.githubusercontent.com/83596240/184608916-0fc9b21c-e5c7-4010-b09e-31ea9cbcdaa1.png)
![image](https://user-images.githubusercontent.com/83596240/184608962-0335d763-161c-4096-a2bb-7e25cfeff809.png)

## Graphing the model accuracy and model loss for all the three model ##

### 1. For MobileNetV2 model ###

![image](https://user-images.githubusercontent.com/83596240/184609677-cf80d444-bed3-4417-9ffc-048afabbf101.png)

### 2. For InceptionV3 model ###

![image](https://user-images.githubusercontent.com/83596240/184609805-249c727a-1584-4488-b29f-01b38a7198d9.png)

### 3. For VGG19 model ###

![image](https://user-images.githubusercontent.com/83596240/184610190-ad7b046b-c559-4a38-9c54-1b16c12b1113.png)

## Performing prediction using all the three model ##

### 1. For MobileNetV2 model ###

![image](https://user-images.githubusercontent.com/83596240/184610446-223b5b4e-f6a4-4744-9fce-69622e924bfa.png)

For an Covid CT image the model predicts it as non-Covid which is incorrect

### 2. For InceptionV3 model ###

![image](https://user-images.githubusercontent.com/83596240/184610362-b857df02-8ae5-487a-b936-09dd8554905f.png)

For an Covid CT image the model predicts it as Covid which is correct

### 3. For VGG19 model ###

![image](https://user-images.githubusercontent.com/83596240/184610368-6dc7204d-04c0-49e8-8ba3-789a4ec1be3c.png)

For an Covid CT image the model predicts it as Covid which is correct


## Conclusion ##
### We conclude that VGG19 model works better than other model when compared, having accuracy of 84.50% and loss of 35.17% ###



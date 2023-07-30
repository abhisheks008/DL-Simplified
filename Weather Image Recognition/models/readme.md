# weather image recognition 
![image](https://github.com/aditya0929/Weather-Image-Recognition/assets/127277877/1e900ca3-2d25-452c-8ae3-8e9a3ebf28b6)

## SOCIAL SUMMER OF CODE 2023

**The models that i have created are based on the approach for making a Deep Learning Model which deals with mutli isntance image classification as in the dataset selected we had fifteen classes of images:**

1. `dew`
2.  `fogsmog`
3.  `frost`
4.  `glaze`
5.  `hail`
6.  `lightning`
7.  `rain`
8.  `lightning`
9.  `rain`
10.  `rainbow`
11.  `rime`
12.  `sandstorm`
13.  `snow`

### Important note:-
for all the three models that i have created, the parts excluding the model architecture and its definition are mostly the same for the accuracy result to be based out on the same parameters.

## Approach for Multi-Instance Image Classification
1. Importing important libaries

2. Loading the datasets and creating image and label list for each category

3. Division of train test ad split of the dataset

4. Data preprocessing and Image data generators

5. Division for images in training , testing and validation categories

6. Making of the models

    **A. VGG19**
   
   
        The VGG19 model is a deep convolutional neural network that has been pre-trained on the ImageNet dataset.
   
       Fine-tuning involves taking the pre-trained model and adapting it to a new task or 
       dataset by training the top layers while keeping the lower layers frozen.
   
       Load the pre-trained VGG16 model
   
       Freeze the layers in the base model
   
       Add custom top layers
   
       Create the fine-tuned model
   
       Compile the model
   
       Train the model                          

   **B. ResNet152V2**
   
       The ResNet50V2 model is pre-trained on the ImageNet dataset and is used as a feature extractor.
       A sequential model is created. The base ResNet50V2 model is added as the first layer. 

        Global average pooling is applied to reduce the spatial dimensions of the output.
        Dropout layers are introduced to mitigate overfitting. 

        Two dense layers with ReLU activation are added, followed by a final dense layer with 
          softmax activation for multi-class classification.

        the model is compiled by specifying the loss function, optimizer, and evaluation metrics.

        the model is trained usinf the fit() function to the training data (train_images)
        and validate it on the validation data (val_images) 
        using the provided training parameters after defining earlystopping and reduction in learning rate using reduce_lr

   **InceptionV3**
      

       InceptionV3 is a deep convolutional neural network architecture that is widely used for image classification tasks.


           Import the necessary libraries such as :
           - `InceptionV3` from `tensorflow.keras.applications`
           - `Sequential`, `GlobalAveragePooling2D`, `Dropout`, `Dense` from `tensorflow.keras.layers`
           - `Adam` from `tensorflow.keras.optimizers`
       Create a sequential model and add the base model (pre-trained InceptionV3) as the first layer::
   

        Add the base model (pre-trained InceptionV3) as the first layer and apply global average pooling to reduce the spatial dimensions of the output:
           
        Add dropout layers to mitigate overfitting:
        Add two dense layers with ReLU activation:
   
        Add the output layer with softmax activation for multi-class classification:
       Compile the model:
  
        Train the model using the `fit()` function:

7.Training and Validation Metrics Visualization

    plotting graphs showing training loss,
    validation loss,
    training accuracy,
    validation accuracy,
    
8. Model prediction and evaluation

9. Finally, Training and Validation Metrics Visualization

10. Accuracy Evaluation and Confusion Matrix

11. Additionally , the model architecture can also be visualized .
12. 
### Learning resources 
  
  
  1.[Transfer Learning using mobilenet and keras](https://medium.com/towards-data-science/transfer-learning-using-mobilenet-and-keras-c75daf7ff299)
  
  2.[cnn-architectures](https://medium.com/@RaghavPrabhu/cnn-architectures-lenet-alexnet-vgg-googlenet-and-resnet-7c81c017b848)
  
  3.[how to build your own neural network](https://medium.com/towards-data-science/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6)
  
  4.[cnn- deep learning](https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148)

  

 ### GITHUB LINK - https://github.com/aditya0929

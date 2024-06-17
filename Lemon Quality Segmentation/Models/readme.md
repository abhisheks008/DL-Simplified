# Lemon Quality Segmentation 

![image](https://github.com/aditya0929/Lemon-quality-segmentation/assets/127277877/5c45f311-5a2e-4ad8-b49f-4a228448d5d8)

**SOCIAL SUMMER OF CODE 2023**

**The models that i have created are based on the approach for making a Deep Learning Model which deals with mutli isntance image classification as in the dataset provided we had three classes of images:-**
1. bad_quality 
2. empty_background 
3. good_quality 

## Important note:-
**for all the three models that i have created, the parts excluding the model architecture and its definition are mostly the same for the accuracy result to be based out on the same parameters.**


# Approach for Multi-Instance Image Classification

**1. importing important libaries**

**2. loading the datasets and creating image and label list for each category** 

**3. creating and shuffling the dataframe**

**4. division of train test ad split of the dataset**

**5. Data preprocessing and Image data generators**

   **a. rescaling and data augmentation**
   
   **b. diviion for images in training , testing and validation categories**

**6.**

  **A. ALEXNET**
     
     
     Implementing AlexNet architecture using Keras. 
     It defines a sequential model and adds convolutional, pooling, and dense layers to construct the network.
     
     The model consists of 8 convolutional layers with ReLU activation, max pooling, and zero padding. 
     It also includes 3 fully connected    layers with dropout for regularization.
     
     The output layer has softmax activation for multi-class classification.
     The model is compiled with the ADAM optimizer and categorical cross-entropy loss.
     Two callbacks, early stopping and reduce learning rate on plateau, are defined. 
     
     The model is trained using the fit() function with provided training and validation datasets
     
   **B. VGG16**
   
   
    -The VGG16 model is a deep convolutional neural network that has been pre-trained on the ImageNet dataset. 
    -Fine-tuning involves taking the pre-trained model and adapting it to a new task or 
     dataset by training the top layers while keeping the lower layers frozen.
    -Load the pre-trained VGG16 model
    -Freeze the layers in the base model
    -Add custom top layers
    -Create the fine-tuned model
    -Compile the model
    -Train the model
   
   **C. Simple CNN**
   
   
    The model architecture is defined using a Sequential model from Keras. 
    Several layers are added to the model,
    including convolutional layers (Conv2D), 
    max-pooling layers (MaxPooling2D), 
    batch normalization (BatchNormalization), 
    flatten layer (Flatten), 
    dropout layers (Dropout),
    fully connected dense layers (Dense). 
    The last dense layer has three units with softmax activation, 
    which corresponds to the number of classes in the classification task.
    The model is compiled with the ADAM optimizer and categorical cross-entropy loss.
   
**7.Training and Validation Metrics Visualization**
 
 
    plotting graphs showing training loss,
    validation loss,
    training accuracy,
    validation accuracy,
    mean squared error in terms of ALEXnet and SimpleCNN 
    
**8. Model prediction and evaluation**

**9. Accuracy Evaluation and Confusion Matrix**

**10. Finally, Training and Validation Metrics Visualization**

**11. Additionally , the model architecture can also be visualized .**

### Learning resources 
  
  
  1.[Transfer Learning](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a)
  
  2.[cnn-architectures](https://medium.com/@RaghavPrabhu/cnn-architectures-lenet-alexnet-vgg-googlenet-and-resnet-7c81c017b848)
  
  3.[how to build your own neural network](https://medium.com/towards-data-science/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6)
  
  4.[cnn- deep learning](https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148)
  
  5.[vgg implementations](https://medium.com/towards-data-science/step-by-step-vgg16-implementation-in-keras-for-beginners-a833c686ae6c)

 ### GITHUB LINK - https://github.com/aditya0929





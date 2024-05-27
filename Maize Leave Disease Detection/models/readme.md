# Maize Leave Disease Detection 
![image](https://github.com/aditya0929/Maize-Leave-Disease-Detection/assets/127277877/5c379091-8da0-4bb3-b819-43bffb843f40)


**The models that i have created are based on the approach for making a Deep Learning Model which deals with mutli isntance image classification as in the dataset selected we had 4 classes of images:-**

| leave disease classes            |
|----------------------------|
|   Healthy - 1162 images        |
|  Blight -1146 images             |
|  Gray Leaf Spot - 574 images   |
|  Common Rust - 1306 images     |

## Important note:-
**for all the three models that i have created, the parts excluding the model architecture and its definition are mostly the same for the accuracy result to be based out on the same parameters.**


# Approach for Multi-Instance Image Classification

**1. Importing important libaries**

**2. Loading the datasets and creating image and label list for each category** 

**3. Division of train test ad split of the dataset**

**4. Data preprocessing and Image data generators**

**5. Division for images in training , testing and validation categories**

**6. Making of the models**

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

**MOBILENET**
     
     
     Implementing MobileNet architecture using Keras. 
     MobileNet is a lightweight convolutional neural network architecture designed for mobile and embedded vision applications.
     It defines a sequential model and sequential layers are added to construct the MobileNet architecture
     
     The desired input image size is (224x224x3)  MobileNet model is initialized as the base model. 
     This include_top=False argument to ensure that the top classification layer of the MobileNet model is excluded.
     
     After the convolutional layers, output is flattened and fully connected layers with dropout for regularization are added  
     
     Finally, the model ends with an output layer using softmax activation for multi-class classification.
     
     the model is compiled by specifying the loss function, optimizer, and evaluation metrics.
     
     The model is trained using the fit() function with provided training and validation datasets

 **VGG16**
   
   
    -The VGG16 model is a deep convolutional neural network that has been pre-trained on the ImageNet dataset. 
    -Fine-tuning involves taking the pre-trained model and adapting it to a new task or 
     dataset by training the top layers while keeping the lower layers frozen.
    -Load the pre-trained VGG16 model
    -Freeze the layers in the base model
    -Add custom top layers
    -Create the fine-tuned model
    -Compile the model
    -Train the model

    **7.Training and Validation Metrics Visualization**
 
 
    plotting graphs showing training loss,
    validation loss,
    training accuracy,
    validation accuracy,
   
    
**7. Model prediction and evaluation**

**8. Accuracy Evaluation and Confusion Matrix**

**9. Finally, Training and Validation Metrics Visualization**

**10. Additionally , the model architecture can also be visualized .**

### Learning resources 

  
  1.[Transfer Learning](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a)
  
  2.[cnn-architectures](https://medium.com/@RaghavPrabhu/cnn-architectures-lenet-alexnet-vgg-googlenet-and-resnet-7c81c017b848)
  
  3.[how to build your own neural network](https://medium.com/towards-data-science/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6)
  
  4.[cnn- deep learning](https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148)
  
  5.[vgg implementations](https://medium.com/towards-data-science/step-by-step-vgg16-implementation-in-keras-for-beginners-a833c686ae6c)

 ### GITHUB LINK - https://github.com/aditya0929

  

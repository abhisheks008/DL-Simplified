# Artwork Image Recognition 
![image](https://github.com/aditya0929/Surreal-Symphonies-artwork-image-recognition-/assets/127277877/820efb2f-9bcd-4198-b973-b95f3727381d)

**The models that i have created are based on the approach for making a Deep Learning Model which deals with mutli isntance image classification as in the dataset selected we had 36 classes of images:-**

| Art Movements              |
|----------------------------|
| Minimalism art             |
| Pop art                    |
| Romanticism paintings      |
| Symbolism artwork          |
| Digital art               |
| Mannerism paintings        |
| Neoclassical art           |
| Academic art              |
| Art deco paintings         |
| Impressionism artwork      |
| Baroque paintings          |
| Fauvism paintings          |
| Abstract art               |
| Expressionism paintings    |
| Realism paintings          |
| Pre-Raphaelite paintings   |
| Surrealism artwork         |
| Dadaism artwork            |
| Neo-expressionism art      |
| Modernism artwork          |
| Naïve art                  |
| Constructivism art         |
| Post-impressionism artwork |
| Contemporary art           |
| Art Nouveau paintings      |
| Gothic art                 |
| Renaissance paintings      |
| Surrealist paintings       |
| Cubism art                 |
| Abstract expressionism paintings |

## Important note:-
**for all the three models that i have created, the parts excluding the model architecture and its definition are mostly the same for the accuracy result to be based out on the same parameters.**


# Approach for Multi-Instance Image Classification

**1. Importing important libaries**

**2. Loading the datasets and creating image and label list for each category** 

**3. Division of train test ad split of the dataset**

**4. Data preprocessing and Image data generators**

**5. Division for images in training , testing and validation categories**

**6. Making of the models**

 **ResNet152V2**
   
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

  **Xception**

     Xception is a deep convolutional neural network architecture widely used for image classification tasks. It is based on the Inception architecture but introduces modifications for improved performance.

     To implement Xception:
     1. Import necessary libraries: `Xception` from `tensorflow.keras.applications`, and relevant layers and optimizers.
     2. Create a sequential model and add the pre-trained Xception as the first layer.
     3. Apply global average pooling to reduce spatial dimensions.
     4. Add dropout layers to mitigate overfitting.
     5. Add two dense layers with ReLU activation.
     6. Add the output layer with softmax activation for multi-class classification.
     7. Compile the model with appropriate optimizer, loss, and metrics.
     8. Train the model using the `fit()` function with your training data.
Replace placeholders with specific values for your classification task and data. 

7.Training and Validation Metrics Visualization

    plotting graphs showing training loss,
    validation loss,
    training accuracy,
    validation accuracy

8. Model prediction and evaluation

9. Finally, Training and Validation Metrics Visualization

10. Accuracy Evaluation and Confusion Matrix

11. Additionally , the model architecture can also be visualized .

### Learning resources 
  
  
   1.[Transfer Learning using mobilenet and keras](https://medium.com/towards-data-science/transfer-learning-using-mobilenet-and-keras-c75daf7ff299)
  
   2.[cnn-architectures](https://medium.com/@RaghavPrabhu/cnn-architectures-lenet-alexnet-vgg-googlenet-and-resnet-7c81c017b848)
  
   3.[how to build your own neural network](https://medium.com/towards-data-science/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6)
  
   4.[cnn- deep learning](https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148)

  

 ### GITHUB LINK - https://github.com/aditya0929

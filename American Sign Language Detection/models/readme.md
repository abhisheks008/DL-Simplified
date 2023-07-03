 # American Sign Language Detection
![image](https://github.com/aditya0929/DL-Simplified/assets/127277877/c149f669-ed35-4751-87bd-b148495fafc4)


**SOCIAL SUMMER OF CODE 2023**
github link - [aditya0929](https://github.com/aditya0929)

**The models that i have created are based on the approach for making a Deep Learning Model which deals with mutli isntance image classification as in the dataset selected we had 36 classes of images:-**

 Here are the classes present in the ASL Dataset, formatted in a table for better readability:

| Classes |
|---------|
| A       |
| B       |
| C       |
| D       |
| E       |
| F       |
| G       |
| H       |
| I       |
| J       |
| K       |
| L       |
| M       |
| N       |
| O       |
| P       |
| Q       |
| R       |
| S       |
| T       |
| U       |
| V       |
| W       |
| X       |
| Y       |
| Z       |
| 0       |
| 1       |
| 2       |
| 3       |
| 4       |
| 5       |
| 6       |
| 7       |
| 8       |
| 9       |

These classes represent the hand gestures corresponding to the English alphabets (A-Z) and numbers (0-9) in American Sign Language.

## Important note:-
**for all the three models that i have created, the parts excluding the model architecture and its definition are mostly the same for the accuracy result to be based out on the same parameters.**


# Approach for Multi-Instance Image Classification

**1. Importing important libaries**

**2. Loading the datasets and creating image and label list for each category** 

**3. Division of train test ad split of the dataset**

**4. Data preprocessing and Image data generators**

**5. Division for images in training , testing and validation categories**

**6. Making of the models**

 **A. MOBILENET**
     
     
     Implementing MobileNet architecture using Keras. 
     MobileNet is a lightweight convolutional neural network architecture designed for mobile and embedded vision applications.
     It defines a sequential model and sequential layers are added to construct the MobileNet architecture
     
     The desired input image size is (64x64x3)  MobileNet model is initialized as the base model. 
     This include_top=False argument to ensure that the top classification layer of the MobileNet model is excluded.
     
     After the convolutional layers, output is flattened and fully connected layers with dropout for regularization are added  
     
     Finally, the model ends with an output layer using softmax activation for multi-class classification.
     
     the model is compiled by specifying the loss function, optimizer, and evaluation metrics.
     
     The model is trained using the fit() function with provided training and validation datasets

 **b. VGG16**
   
   
    -The VGG19 model is a deep convolutional neural network that has been pre-trained on the ImageNet dataset. 
    -Fine-tuning involves taking the pre-trained model and adapting it to a new task or 
     dataset by training the top layers while keeping the lower layers frozen.
    -Load the pre-trained VGG16 model
    -Freeze the layers in the base model
    -Add custom top layers
    -Create the fine-tuned model
    -Compile the model
    -Train the model

**B. INCEPTIONRESNET50**

    -Implementing the InceptionResNetV2 architecture using Keras. InceptionResNetV2 is a deep convolutional neural network model that combines the concepts of Inception and ResNet models.

    -To construct the InceptionResNetV2 architecture, a sequential model is defined, and sequential layers are added. The desired input image size is (64x64x3). 
    The InceptionResNetV2 model is initialized as the base model with include_top=False, which excludes the top classification layer.

    -After the convolutional layers, the output is flattened, and fully connected layers with dropout regularization are added. 
    These layers enable the model to learn complex representations and generalize well to unseen data.

    -The model ends with an output layer using softmax activation for multi-class classification. 
    The model is compiled by specifying the loss function, optimizer, and evaluation metrics.

    -Training is performed using the fit() function, where the provided training and validation datasets are used to update the model's weights based on the defined loss function.
    The model's performance is evaluated using the specified metrics on the validation set.


**7.Training and Validation Metrics Visualization**
 
 
    plotting graphs showing 
    training accuracy,
    validation accuracy,
    
**8. Model prediction and evaluation**

**9. Accuracy Evaluation and Confusion Matrix**

**10. Finally, Training and Validation Metrics Visualization**

**11. Additionally , the model architecture can also be visualized .**
  
**12. Learning Resources - ** 

  
   
   1.[Transfer Learning](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a)
  
   2.[cnn-architectures](https://medium.com/@RaghavPrabhu/cnn-architectures-lenet-alexnet-vgg-googlenet-and-resnet-7c81c017b848)
  
   3.[how to build your own neural network](https://medium.com/towards-data-science/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6)
   
4. [popular deep learning architectures](https://blog.paperspace.com/popular-deep-learning-architectures-resnet-inceptionv3-squeezenet/)

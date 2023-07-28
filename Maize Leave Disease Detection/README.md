# Maize-Leave-Disease-Detection /  https://github.com/World-of-ML/DL-Simplified/issues/363
classification of corn or maize plant leaf diseases

Full name : Aditya Narayan Jha

GitHub Profile Link : https://github.com/aditya0929

Email ID : adityajha8906@gmail.com

Participant ID (if applicable): (certificate_id) - 7e43ecd9-76ff-4713-917e-f884b9fedf02

Approach for this Project :

**Image segmentation**

is a crucial task in computer vision that involves identifying and classifying different regions or objects within an image. In this project, I will explore three different approaches for image segmentation using deep learning models: **InceptionV3**, **MobileNet**, **VGG16**, and **VGG19**.

**MobileNet** 

By utilizing **transfer learning** with the MobileNet model, we can leverage pre-trained weights and significantly reduce the training time required for our image classification task. This approach is particularly useful when working with limited training data, as we can benefit from the rich representations learned by the base model on a large-scale dataset like ImageNet.

**InceptionV3**

To implement InceptionV3, we start by loading the pre-trained model, which comes with weights learned from the ImageNet dataset. We freeze the layers of the pre-trained model to prevent them from being updated during training, preserving their valuable representations. Next, we add custom layers on top of the pre-trained model, including BatchNormalization, Dense, Dropout, and a final Dense layer with softmax activation for classification. These additional layers enable us to adapt the model to our specific dataset. Finally, we compile the model by specifying an optimizer, a suitable loss function, and metrics for evaluation. This compilation step prepares the model for fine-tuning and training on our dataset.

**VGG16**

**Lastly,** I will utilize the **VGG16** (Visual Geometry Group) architecture, which have deeper and complex structures. These models are renowned for their exceptional performance on various image recognition tasks. By leveraging the pre-trained weights of VGG, I can benefit from the learned features and fine-tune the network for image segmentation task



**Throughout the project,** 

I will preprocess the dataset by resizing the images and splitting it into training and testing sets. For training, I will employ a loss function suitable for image segmentation, such as the Dice coefficient or cross-entropy loss, and optimize the models using techniques like stochastic gradient descent, rms prop or Adam optimization.

**After training the models,**

I will evaluate their performance using appropriate metrics. Additionally, I will visualize the segmentation results to gain insights into how well the models can accurately identify and classify different regions within the images.
the comparison.ipynb shows different graphical representation for the metrics evaluation and the model with the best accuracy score can be selected eventhough the other models are also highly accurate.


**Accuracy Comparison**

| `Model`  | `Accuracy` |
|--------|----------|
| VGG16  |   91%    |
| InceptionV3 | 88% |
| vgg19 | 88% |
| MobileNet | 91% |

Since the models' decent levels of accuracy(88% and above) means that most of their pictures will be almost havinG similar predicted labels with a small room for mistake, the anticipated labels for the disease image labels are as are visualised as follows.

**Throughout the project,** 

I will preprocess the dataset by resizing the images and splitting it into training,validation and testing sets. For training, I will employ a loss function suitable for image segmentation, such as cross-entropy loss, and optimize the models using technique like  Adam optimization

**After training the models,**

I will evaluate their performance using appropriate metrics. Additionally, I will visualize the segmentation results to gain insights into how well the models can accurately identify and classify different regions within the leave images.

## predicted labels 

![image](https://github.com/aditya0929/Maize-Leave-Disease-Detection/assets/127277877/7b5f4c85-b0ad-4502-9f24-d928f0a95a6f)



## after evaluation, `MobileNet` model looks to be the best fit model in this case of  Maize Leave Disease Detection .

**Future Scope**

ON DEPLOYMENT THESE MODEL WILL HAVE A PURPOSE OF DEVELOPING SENSE AND LEAVE DISEASE DETECTION

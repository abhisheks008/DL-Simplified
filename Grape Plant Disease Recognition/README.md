# Grape Plant Disease Recognition / https://github.com/World-of-ML/DL-Simplified/issues/342

Full name : Aditya Narayan Jha

GitHub Profile Link : https://github.com/aditya0929

Email ID : adityajha8906@gmail.com

Participant ID (if applicable): (certificate_id) - 7e43ecd9-76ff-4713-917e-f884b9fedf02

Approach for this Project :

**Image segmentation**

is a crucial task in computer vision that involves identifying and classifying different regions or objects within an image. In this project, I will explore three different approaches for image segmentation using deep learning models: **VGG16**, **MobileNet**, and **ResNet50V2**.

**ResNet50V2** 

I have implemented a ResNet50V2 model for image classification using Keras. The ResNet50V2 model, pre-trained on the **ImageNet dataset**, serves as a powerful feature extractor. By freezing the pre-trained layers and adding additional layers for classification, we were able to achieve good performance on our image classification task.

**MobileNet** 

By utilizing **transfer learning** with the MobileNet model, we can leverage pre-trained weights and significantly reduce the training time required for our image classification task. This approach is particularly useful when working with limited training data, as we can benefit from the rich representations learned by the base model on a large-scale dataset like ImageNet.

**VGG16**

**Lastly,** I will utilize the **VGG16** (Visual Geometry Group) architecture, which have deeper and complex structures. These models are renowned for their exceptional performance on various image recognition tasks. By leveraging the pre-trained weights of VGG, I can benefit from the learned features and fine-tune the network for image segmentation on the Grape Plant Disaease Recognition.

**Throughout the project,** 

I will preprocess the dataset by resizing the images and splitting it into training,validation and testing sets. For training, I will employ a loss function suitable for image segmentation, such as cross-entropy loss, and optimize the models using technique like  Adam optimization

**After training the models,**

I will evaluate their performance using appropriate metrics. Additionally, I will visualize the segmentation results to gain insights into how well the models can accurately identify and classify different regions within the vegetable images.

**Accuracy Comparison**

| `Model`  | `Accuracy` |
|--------|----------|
| VGG16  |   88%    |
| MobileNet | 97% |
| ResNet50V2 | 93% |

Since the models' decent levels of accuracy(88% and above) means that most of their pictures will be almost havinG similar predicted labels with a small room for mistake, the anticipated labels for the sign image labels are as are visualised as follows.

![image](https://github.com/aditya0929/Grape-Plant-Disease-Recognition/assets/127277877/8c41d198-44bf-4d36-87ac-b7a9f3e98820)
![image](https://github.com/aditya0929/Grape-Plant-Disease-Recognition/assets/127277877/4eddf30d-1db1-4f8a-b4f9-291ea46124c0)


## after evaluation, `MobileNet`  model looks to be the best fit model in this case of American Sign Language Classification .


**Future Scope**

This project will contribute to advancing the understanding and application of deep learning in the field of computer vision and could potentially find applications in sorting of Grape Plant Disease Recognition
 in different classes.


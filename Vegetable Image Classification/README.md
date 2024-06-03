## SOCIAL SUMMER OF CODE-2023 /https://github.com/World-of-ML/DL-Simplified/issues/282
# Vegetable Image Classification #282


Full name : Aditya Narayan Jha

GitHub Profile Link : https://github.com/aditya0929

Email ID : adityajha8906@gmail.com

Participant ID (if applicable): (certificate_id) - 7e43ecd9-76ff-4713-917e-f884b9fedf02

Approach for this Project :

**Image segmentation**

is a crucial task in computer vision that involves identifying and classifying different regions or objects within an image. In this project, I will explore three different approaches for image segmentation using deep learning models: **Simple_CNN**, **MobileNet**, and **ResNet50V2**.

 **Simple_CNN** 
 
**To begin,** I will leverage the **Simple_CNN** architecture, which is a lightweight convolutional neural network suitable for multi-scale image segmentation tasks. With its simplicity, this model can process the image dataset in their respective classes [Dataset link](https://www.kaggle.com/datasets/misrakahmed/vegetable-image-dataset).

**ResNet50V2** 

I have implemented a ResNet50V2 model for image classification using Keras. The ResNet50V2 model, pre-trained on the **ImageNet dataset**, serves as a powerful feature extractor. By freezing the pre-trained layers and adding additional layers for classification, we were able to achieve good performance on our image classification task.

**MobileNet** 

By utilizing **transfer learning** with the MobileNet model, we can leverage pre-trained weights and significantly reduce the training time required for our image classification task. This approach is particularly useful when working with limited training data, as we can benefit from the rich representations learned by the base model on a large-scale dataset like ImageNet.

**Visualization**

![image](https://github.com/aditya0929/vegetable-image-classification/assets/127277877/c8d094de-1cf0-43f7-bdcc-6ac0b4997c7d)
![image](https://github.com/aditya0929/vegetable-image-classification/assets/127277877/cba220ab-2df5-4ca1-a798-44f9adac8f15)

Since the models' high levels of accuracy(96% and above) means that most of their pictures will be almost havin similar predicted labels with little room for mistake, the anticipated labels for the vegetables are visualised as follows.

**Throughout the project,** 

I will preprocess the dataset by resizing the images and splitting it into training,validation and testing sets. For training, I will employ a loss function suitable for image segmentation, such as cross-entropy loss, and optimize the models using technique like  Adam optimization

**After training the models,**

I will evaluate their performance using appropriate metrics. Additionally, I will visualize the segmentation results to gain insights into how well the models can accurately identify and classify different regions within the vegetable images.

**Performance checker**

![image](https://github.com/aditya0929/vegetable-image-classification/assets/127277877/98fca8f7-f1f3-4d00-8597-327dcef12beb)

## after evaluation, `MOBILENET` model looks to be the best fit model in this case of Vegetable Image Classification .

## even though the other models also have a high accuracy and have complete capacity for executing the task and predicting the labels.

**Future Scope**

This project will contribute to advancing the understanding and application of deep learning in the field of computer vision and could potentially find applications in quality assessment and sorting of vegetables based on different classes.
















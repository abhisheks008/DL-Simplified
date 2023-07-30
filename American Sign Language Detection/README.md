# American Sign Language Detection/https://github.com/World-of-ML/DL-Simplified/issues/312
to predict correct sign language labels corresponding to their corresponding sign images



Full name : Aditya Narayan Jha

GitHub Profile Link : https://github.com/aditya0929

Email ID : adityajha8906@gmail.com

Participant ID (if applicable): (certificate_id) - 7e43ecd9-76ff-4713-917e-f884b9fedf02

Approach for this Project :

**Image segmentation**

is a crucial task in computer vision that involves identifying and classifying different regions or objects within an image. In this project, I will explore three different approaches for image segmentation using deep learning models: **VGG16**,  **MobileNet** . **InceptionV3** and **InceptionResNetV2**.


`InceptionResNetV2` 

When implementing the InceptionResNetV2 model in code, we leverage its powerful architecture to enhance our image classification tasks. By loading the pre-trained InceptionResNetV2 model with weights from the ImageNet dataset, we benefit from its extensive knowledge. To fine-tune the model for our specific dataset, we freeze the layers to preserve the learned representations. The combination of residual blocks and Inception modules allows the network to effectively capture multi-scale features and learn intricate representations. The skip connections in the residual blocks address the vanishing gradient problem and facilitate smooth gradient flow during training. With its exceptional performance on image classification, InceptionResNetV2 serves as an excellent choice for deep learning practitioners seeking accurate and efficient models.

`MobileNet` 

By utilizing **transfer learning** with the MobileNet model, we can leverage pre-trained weights and significantly reduce the training time required for our image classification task. This approach is particularly useful when working with limited training data, as we can benefit from the rich representations learned by the base model on a large-scale dataset like ImageNet.

`InceptionV3`

To implement InceptionV3, we start by loading the pre-trained model, which comes with weights learned from the ImageNet dataset. We freeze the layers of the pre-trained model to prevent them from being updated during training, preserving their valuable representations. Next, we add custom layers on top of the pre-trained model, including BatchNormalization, Dense, Dropout, and a final Dense layer with softmax activation for classification. These additional layers enable us to adapt the model to our specific dataset. Finally, we compile the model by specifying an optimizer, a suitable loss function, and metrics for evaluation. This compilation step prepares the model for fine-tuning and training on our dataset.

`vgg16`

I will utilize the **VGG16** (Visual Geometry Group) architecture, which have deeper and complex structures. These models are renowned for their exceptional performance on various image recognition tasks. By leveraging the pre-trained weights of VGG, I can benefit from the learned features and fine-tune the network for image segmentation on the Lemon Quality Dataset.


**Accuracy Comparison**

| `Model`  | `Accuracy` |
|--------|----------|
| VGG16  |   97%    |
| InceptionV3 | 88% |
| InceptionResNetV2 | 88% |
| MobileNet | 97% |

Since the models' decent levels of accuracy(88% and above) means that most of their pictures will be almost havinG similar predicted labels with a small room for mistake, the anticipated labels for the sign image labels are as are visualised as follows.

**Throughout the project,** 

I will preprocess the dataset by resizing the images and splitting it into training,validation and testing sets. For training, I will employ a loss function suitable for image segmentation, such as cross-entropy loss, and optimize the models using technique like  Adam optimization

**After training the models,**

I will evaluate their performance using appropriate metrics. Additionally, I will visualize the segmentation results to gain insights into how well the models can accurately identify and classify different regions within the vegetable images.


![predicted labels](https://github.com/aditya0929/DL-Simplified/assets/127277877/6f459067-2939-4436-b19a-5c8177a7e7bb)


## after evaluation, `MobileNet` or `VGG16` model looks to be the best fit model in this case of American Sign Language Classification .


**Future Scope**

This project will contribute to advancing the understanding and application of deep learning in the field of computer vision and could potentially find applications in sorting of sign languages in different classes.


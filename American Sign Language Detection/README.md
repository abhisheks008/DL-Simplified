# New enanchements has been made in the model , please check it below
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

`new models implemented with new approach for enanchement`
- ResNet101V2
- ResNet50V2
- MobileNetV3Large
- MobileNetV3Small
- InceptionV3
- NASNetMobile

**Accuracy Comparison**

| `Model`  | `Accuracy` |
|--------|----------|
| VGG16  |   97%    |
| InceptionV3 | 88% |
| InceptionResNetV2 | 88% |
| MobileNet | 97% |

Since the models' decent levels of accuracy(88% and above) means that most of their pictures will be almost havinG similar predicted labels with a small room for mistake, the anticipated labels for the sign image labels are as are visualised as follows.

`new models accuracy`
| Rank | Model Name       | Test Accuracy | Trained Model Size | Training Accuracy | Training Loss |
|------|------------------|---------------|--------------------|-------------------|---------------|
| 1    | MobileNetV3Small | 100.0%        | 19.1MB             | 96.97%            | 0.1574        |
| 2    | NASNetMobile     | 100.0%        | 67.1MB             | 97.96%            | 0.1058        |
| 3    | MobileNetV3Large | 100.0%        | 48.6MB             | 97.98%            | 0.1026        |
| 4    | InceptionV3      | 100.0%        | 287.8MB            | 98.65%            | 0.0712        |
| 5    | ResNet50V2       | 100.0%        | 308.6MB            | 98.67%            | 0.0625        |
| 6    | ResNet101V2      | 100.0%        | 537.5MB            | 98.74%            | 0.0605        |

- ranking based on Trained Model size

**Throughout the project,** 

I will preprocess the dataset by resizing the images and splitting it into training,validation and testing sets. For training, I will employ a loss function suitable for image segmentation, such as cross-entropy loss, and optimize the models using technique like  Adam optimization

**After training the models,**

I will evaluate their performance using appropriate metrics. Additionally, I will visualize the segmentation results to gain insights into how well the models can accurately identify and classify different regions within the vegetable images.


![predicted labels](https://github.com/aditya0929/DL-Simplified/assets/127277877/6f459067-2939-4436-b19a-5c8177a7e7bb)


## after evaluation, `MobileNet` or `VGG16` model looks to be the best fit model in this case of American Sign Language Classification .

## New models conclusian after enanchement
- All models achieve a remarkable test accuracy of 100.0%, demonstrating their effectiveness in classification tasks.
  - MobileNetV3Small stands out with a compact size of 19.1MB, offering high accuracy while minimizing resource usage, making it suitable for memory-constrained environments.
  - NASNetMobile and MobileNetV3Large also deliver impressive accuracy with moderate model sizes, providing versatility in deployment scenarios.
  - InceptionV3, ResNet50V2, and ResNet101V2, although larger in size, exhibit robust performance, with ResNet101V2 achieving the highest training accuracy of 98.74%.

**Future Scope**

This project will contribute to advancing the understanding and application of deep learning in the field of computer vision and could potentially find applications in sorting of sign languages in different classes.

### ✒️ Improvements in this project is made by **Adhithyan VP**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adhithyanvp)
[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/AdhiVp3)](https://x.com/AdhiVp3)

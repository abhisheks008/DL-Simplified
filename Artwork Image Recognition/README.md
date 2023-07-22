# Artwork Image Recognition / https://github.com/World-of-ML/DL-Simplified/issues/356

to predict correct artwork image labels corresponding to their corresponding artwork images




Full name : Aditya Narayan Jha

GitHub Profile Link : https://github.com/aditya0929

Email ID : adityajha8906@gmail.com

Participant ID (if applicable): (certificate_id) - 7e43ecd9-76ff-4713-917e-f884b9fedf02

Approach for this Project :
**Image segmentation**

is a crucial task in computer vision that involves identifying and classifying different regions or objects within an image. In this project, I will explore three different approaches for image segmentation using deep learning models:  **Resnet152v2** . **Xception** and **InceptionV3**.

`InceptionV3`

To implement InceptionV3, we start by loading the pre-trained model, which comes with weights learned from the ImageNet dataset. We freeze the layers of the pre-trained model to prevent them from being updated during training, preserving their valuable representations. Next, we add custom layers on top of the pre-trained model, including BatchNormalization, Dense, Dropout, and a final Dense layer with softmax activation for classification. These additional layers enable us to adapt the model to our specific dataset. Finally, we compile the model by specifying an optimizer, a suitable loss function, and metrics for evaluation. This compilation step prepares the model for fine-tuning and training on our dataset.

`ResNet152v2`

i had tried different resnet models for the task but ResNet152v2 seems to have performed the best as it reached an accuracy score of 94% within 10 iterations .  To fine-tune the model for our specific dataset, i had freezed the layers to preserve the learned representations. residual blocks  allows the network to effectively capture multi-scale features and learn intricate representations

`Xception`

Xception is a powerful deep convolutional neural network architecture widely utilized in image classification tasks. Developed by Google researchers, Xception is inspired by the Inception architecture but introduces notable modifications to enhance its performance. The key innovation lies in the novel use of depth-wise separable convolutions, which aim to efficiently capture spatial and channel-wise information separately. This approach drastically reduces the number of parameters in the model, resulting in a more lightweight yet highly accurate network. Xception has demonstrated exceptional results on various image recognition challenges, making it a popular choice for tasks that demand both accuracy and efficiency. Its ability to handle complex feature extraction and its relatively smaller model size make it particularly well-suited for applications in resource-constrained environments, such as mobile devices and embedded systems.


**Accuracy Comparison**

| `Model`  | `Accuracy` |
|--------|----------|
| Xception  |   94%    |
| InceptionV3 | 94% |
| ResNet152V2 | 97% |


Since the models' decent levels of accuracy(94% and above) means that most of their pictures will be almost having similar predicted labels with a small room for mistake, the anticipated labels for the artwork image labels are as are visualised as follows.

**Throughout the project,** 

I will preprocess the dataset by resizing the images and splitting it into training,validation and testing sets. For training, I will employ a loss function suitable for image segmentation, such as cross-entropy loss, and optimize the models using technique like  Adam optimization

**After training the models,**

I will evaluate their performance using appropriate metrics. Additionally, I will visualize the segmentation results to gain insights into how well the models can accurately identify and classify different regions within the weather condition images.


![image](https://github.com/aditya0929/Surreal-Symphonies-artwork-image-recognition-/assets/127277877/028bc26c-e372-47ba-b494-80111950d156)


## after evaluation, `ResNet152V2`  model looks to be the best fit model in this case of Artwork Image Recognition .


**Future Scope**

This project will contribute to advancing the understanding and application of deep learning in the field of computer vision and could potentially find applications in sorting of art image labels in different classes.


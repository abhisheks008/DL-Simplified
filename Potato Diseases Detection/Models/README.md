*Potato Diseases Detection #458*<br>
<br>

*🎯 Goal*<br>
The primary objective of this project is to perform image classification using a custom Convolutional Neural Network (CNN) architecture, as well as leveraging the pre-trained models VGG16 and ResNet50. The models are trained to categorize images into seven classes, providing a versatile solution for various image processing tasks.<br>

*🖼️ Dataset*<br>
The dataset used for this project consists of images distributed across seven classes. Each class has its own subdirectory within the main training and validation directories. The dataset is organized to facilitate supervised learning, with images labeled according to their respective classes. <br>
Dataset link : https://www.kaggle.com/datasets/mukaffimoin/potato-diseases-datasets <br>
<br>

*🧾 Description*<br>
This project utilizes a custom CNN architecture, VGG16, and ResNet50 for image classification. The custom CNN model is designed to capture specific features of the dataset, while the pre-trained VGG16 and ResNet50 models bring in the advantages of transfer learning, enhancing the model's ability to generalize across diverse images.<br>
<br>

*🧮 What I had done!*<br>
1. Data Preprocessing:<br>

Resizing images to match the input size of the models (e.g., 224x224 pixels for VGG16 and ResNet50).<br>
Normalization of pixel values to the range [0, 1].<br>

2. Model Architectures:<bt>
   - Custom CNN: Designed for specific features of the dataset.
   - VGG16: Leveraging the pre-trained VGG16 architecture.
   - ResNet50: Utilizing the pre-trained ResNet50 architecture.

3. Data Augmentation:<br>
Applying image data augmentation techniques using TensorFlow's ImageDataGenerator to enhance model generalization.<br>

4. Model Training:<br>

   - Training the CNN model, VGG16, and ResNet50 on the preprocessed and augmented dataset.
   - Evaluating the models on the validation set to monitor performance.

5. Save Models:<br>
Saving the trained models for future use and predictions.<br>

<br>

*🚀 Models Implemented*<br>
   - Custom CNN
   - VGG16-based Convolutional Neural Network
   - ResNet50-based Convolutional Neural Network

Why these models:<br>

   - Custom CNN: Designed for dataset-specific features.
   - VGG16: Known for simplicity and effectiveness in image classification tasks.
   - ResNet50: Utilizes residual learning to handle deep architectures, improving model performance.<br>
<br>

*📚 Libraries Needed*<br>
1. TensorFlow
2. Matplotlib
3. Numpy
4. Scikit-learn (for additional evaluation metrics if required)


<br>

*📊 Model Training Results*<br>

Training Loss and Validation Loss Plot<br>

Insight: The loss plot visualizes the convergence of the models during training and validation, ensuring effective learning without overfitting or underfitting.<br>

Training Accuracy and Validation Accuracy Plot<br>

Insight: The accuracy plot provides a snapshot of the models' performance, showcasing improvements over epochs and helping identify potential issues like overfitting.<br>
Feel free to replace the placeholder text with actual links to your visualizations or images and provide specific insights derived from your training results.<br>
<br>


*📊 Exploratory Data Analysis Results*<br>
**Distribution of Classes**<br>
To gain an understanding of the dataset, we analyzed the distribution of images across the seven classes. The table below shows the number of images in each class.<br>

| Class | Number of Images |
|-------|-------------------|
| Black Scurf      |  97 |
| Blackleg         |  94 |
| Common Scab      | 101 |
| Dry Rot          |  89 |
| Healthy Potatoes |  96 |
| Miscellaneous    | 104 |
| Pink Rot         |  87 |

**Insight:** The class distribution showcases a relatively balanced dataset, aiding in effective model training.<br>


*📈 Model Performance based on Accuracy Scores*<br>
   - Custom CNN Model Accuracy: 60%
   - VGG16 Model Accuracy: 98%
   - ResNet50 Model Accuracy: 46%%

*📢 Conclusion*<br>
The image classification project using custom CNN, VGG16, and ResNet50 models demonstrates effective learning and categorization across seven classes. The models achieve promising accuracy on both training and validation sets, showcasing their potential for various image processing applications.<br>

<br>

✒️ Your Signature<br>
Dipayan Majumder<br>
github.com/dipayan22<br>


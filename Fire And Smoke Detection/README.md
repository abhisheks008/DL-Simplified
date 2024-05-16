*Fire Detection #458*<br>
<br>

*🎯 Goal*<br>
The primary objective of this project is to perform image classification using a custom Convolutional Neural Network (CNN) architecture, as well as leveraging the pre-trained models VGG19,ResNetRS50,InceptionV3,Xception. The models are trained to categorize images into two classes, providing a versatile solution for various image processing tasks.<br>

*🖼️ Dataset*<br>
The dataset used for this project consists of images distributed across two classes.Fire and non fire.Original dataset alloted for this project was no longer available as open source so alternative dataset is used <br>
Dataset link : https://www.kaggle.com/datasets/atulyakumar98/test-dataset/data <br>
<br>

*🧾 Description*<br>
This project utilizes a custom CNN architecture, VGG19,ResNetRS50,InceptionV3,Xception for image classification. The custom CNN model is designed to capture specific features of the dataset, while the pre-trained VGG16 and ResNet50 models bring in the advantages of transfer learning, enhancing the model's ability to generalize across diverse images.<br>
<br>

*🧮 What I had done!*<br>
1. Data Preprocessing:<br>

Resizing images to match the input size of the models (e.g., 128*128 pixels for pretrained models).<br>
Normalization of pixel values to the range [0, 1].<br>

2. Model Architectures:<bt>
   - Custom CNN: Designed for specific features of the dataset.
   - VGG19: Leveraging the pre-trained VGG19 architecture.
   - ResNetRS50: Utilizing the pre-trained ResNetRS50 architecture.
   - InceptionV3: Utilizing pretrained model with version V3.
   - Xception: Leveraging powerful Xception model.

3. Model Training:<br>

   - Training the the models over image dataset
   - Evaluating the models on the validation set to monitor performance.

5. Save Models:<br>
Saving the trained models for future use and predictions.<br>



*📚 Libraries Needed*<br>
1. TensorFlow
2. Matplotlib
3. Numpy
4. Scikit-learn (for additional evaluation metrics if required)
5. Seaborn


<br>


***Visualization Results***
![](Images/Fire And Smoke Detection/Images/Screenshot 2024-05-15 200402.png)

![](Images/Fire And Smoke Detection/Images/Screenshot 2024-05-15 200402.png)

***📈 Model Performance based on Accuracy Scores***


|-------|-----------------|
| CNN              | 100  |
| Xception         | 87.5 |
| ResnetRS50       | 96.8 |
| InceptionV3      |  89  |
| VGG19            | 90.6 |


*📢 Conclusion And Result*<br>
The image classification project using different models demonstrates effective learning and categorization across two classes. The models achieve promising accuracy on both training and validation sets, showcasing their potential for various image processing applications. Our custom CNN scored highest wwith 100% accuracy and xception scored lowest with 87% <br>

<br>

✒️ Your Signature<br>
Keshav Arora <br>

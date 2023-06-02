# Children vs Adults Classification

**PROJECT TITLE**

Children vs Adults Classification

**GOAL**

The main goal of this project is to develop a classification model that can accurately distinguish between images of children and adults. The purpose of the project is to explore the performance of different deep learning models in this specific classification task.

**DATASET**

The dataset used for this project can be found at [link to dataset](https://www.kaggle.com/datasets/die9origephit/children-vs-adults-images). The dataset consists of a collection of images labeled as either children or adults.

**DESCRIPTION**

This project aims to build a classification model that can analyze facial features and classify images as either children or adults. By leveraging deep learning models, the project seeks to achieve accurate and reliable classification results.

**WHAT I HAD DONE**

1. Data collection: Gathered a diverse dataset of images containing children and adults.
2. Data preprocessing: Performed necessary preprocessing steps such as resizing, normalization, and augmentation.
3. Model selection: Chose popular deep learning models, including VGG19, ResNet50, InceptionV3, and MobileNetV2, for the classification task.
4. Model training: Trained each model using the labeled dataset and appropriate training configurations.
5. Model evaluation: Evaluated the trained models on a separate test dataset to measure their performance.
6. Comparative analysis: Compared the accuracy and results of each model to determine the best-performing model.

**MODELS USED**

The following models were used in this project:

1. VGG19
2. ResNet50
3. InceptionV3
4. MobileNetV2

The choice of these models was based on their proven performance in image classification tasks and their varying architectural complexities. This allowed for a comprehensive analysis of different model types.

**LIBRARIES NEEDED**

The following libraries are required to run this project:

- TensorFlow
- Keras
- numpy
- matplotlib
- pandas

**VISUALIZATION**

<img src="Children vs Adults Classification using DL/Images/comparison2.png" alt="Comparison Image">

**ACCURACIES**

The accuracy results obtained for each model on the test dataset are as follows:

- VGG19: 0.73
- ResNet50: 0.67
- InceptionV3: 0.74
- MobileNetV2: 0.79

**CONCLUSION**

Based on the accuracy results, MobileNetV2 achieved the highest accuracy of 79% on the test dataset, making it the best-fitted model for this particular project. The other models also performed well but had slightly lower accuracies.

This project demonstrates the effectiveness of deep learning models in classifying images of children and adults based on facial features. The findings suggest that MobileNetV2 can reliably classify images in this domain, paving the way for potential applications in age estimation or child/adult recognition systems.


# Cats vs Dogs Classification using DL

## PROJECT TITLE

Cats vs Dogs Classification using DL

## 🎯 Goal

The aim is to create a deep-learning model that will identify cats and dogs in the image. 

## 🧵 Dataset

The link for the dataset used in this project: https://www.kaggle.com/datasets/samuelcortinhas/cats-and-dogs-image-classification and https://www.kaggle.com/datasets/tongpython/cat-and-dog

## 🧾 Description
The main goal of the project is to develop a deep-learning model that can accurately predict and identify cats and dogs in the given image based on various features.

## 🧮 What I had done!

1. Data collection: The data is loaded from the links provided above and its structure is 
   explore 
2. Data preprocessing: The data is then preprocessed, where steps such as setting batch 
   size, and image size, converting the image type to a specific type, and scaling are 
   done 
   to prepare the data for model training
3. Model selection: Three models were developed: Convolutional Neural Network (CNN) with 
   Visual Geometry Group 16 (VGG16) and Residual Network with 50 layers (ResNet50) for 
   image detection.  
4. Comparative analysis: The developed models are compared based on their accuracy.

## 🚀 MODELS USED

 1. CNN: CNN is chosen for classifying cats and dogs because of their ability to learn 
    hierarchical features from raw pixel data automatically. CNN networks are built 
    for capturing significant spatial patterns as well as characteristics and so are   
    designed for tasks relating to image comprehension. As a result of their property of 
    spatial invariance, the variation of an object’s size or position can be handled 
    easily.
2. VGG16: VGG16 learns intricate hierarchical features from raw pixel data, enabling 
   discrimination between visual categories. It uses small convolutional filters which 
   maintains its simplicity and effectiveness for tasks like distinguishing between cats 
   and dogs.
3. ResNet50: ResNet50 has a unique architecture comprising 50 layers which helps it to 
   effectively capture complex hierarchical features from images, making them adaptable to 
   discriminate between images like cats and dogs.


## 📚 LIBRARIES NEEDED

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## 📊 Exploratory Data Analysis Results
#### Accuracy of CNN model:
![val_acc2](https://github.com/abhisheks008/DL-Simplified/blob/main/Cats%20vs%20Dogs%20Classification%20using%20DL/Images/val_acc2.JPG)

#### Loss of CNN model:
![val_loss2](https://github.com/abhisheks008/DL-Simplified/blob/main/Cats%20vs%20Dogs%20Classification%20using%20DL/Images/val_loss2.JPG)

#### Accuracy of VGG16 model:
![val_acc3](https://github.com/abhisheks008/DL-Simplified/blob/main/Cats%20vs%20Dogs%20Classification%20using%20DL/Images/val_acc3.JPG)

#### Loss of VGG16 model:
![val_loss3](https://github.com/abhisheks008/DL-Simplified/blob/main/Cats%20vs%20Dogs%20Classification%20using%20DL/Images/val_loss3.JPG)

#### Accuracy of ResNet50 model:
![val_acc1](https://github.com/abhisheks008/DL-Simplified/blob/main/Cats%20vs%20Dogs%20Classification%20using%20DL/Images/val_acc1.JPG)

#### Loss of ResNet50 model:
![val_loss1](https://github.com/abhisheks008/DL-Simplified/blob/main/Cats%20vs%20Dogs%20Classification%20using%20DL/Images/val_loss1.JPG)


## 📈 Performance of the Models based on the Accuracy Scores
The evaluation metrics I used to assess the models:

- Accuracy 
- Loss

| Model      | Accuracy | Loss    |
|------------|----------|---------|
| CNN    | 0.728     | 1.159   |
| VGG16    | 0.925     | 0.218    |
| ResNet50    | 0.735     | 1.688    |


## 📢 Conclusion
Based on the results we can draw the following conclusions:
1. CNN: The CNN model achieved an accuracy of 0.728 and a loss of 1.159. It performed reasonably well, but there is room for improvement.
2. VGG16: The VGG16 model achieved a higher accuracy of 0.925 and a lower loss of 0.218. It outperformed the basic CNN model, indicating that the deeper architecture of VGG16 with more trainable parameters could capture more complex features and generalize better.
3. ResNet50: The ResNet50 model achieved an accuracy of 0.735 and a loss of 1.688. It performed slightly better than the basic CNN model but was outperformed by VGG16. ResNet50's residual connections helped mitigate the vanishing gradient problem and allowed for the training of deeper networks.

✒️ Author
  ##### Code contributed by: Abhishek Sharma
  ##### Email: abhishek.opensource@gmail.com

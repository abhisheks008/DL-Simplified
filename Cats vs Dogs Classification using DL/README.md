# Cats vs Dogs Classification using DL

## 🎯 Goal

Create a DL model which will identify the Cats and Dogs.

## 🧵 Dataset

The link for the dataset used in this project: [Cats and Dogs Image Classification Dataset 1](https://www.kaggle.com/datasets/samuelcortinhas/cats-and-dogs-image-classification) and [Cats and Dogs Image Classification Dataset 2](https://www.kaggle.com/datasets/tongpython/cat-and-dog).

## 🧾 Description


This project aims to identify cats and dogs in images. It is trained on a dataset containing cats and dogs.

## 🧮 What I had done!

1. Data collection: From the links of the datasets given above.
2. Data preprocessing: Preprocessed the images to have all images in equal shape.
3. Model selection: Chose traditional CNN along with Image detection architectures VGG16 and ResNet50 for Image detection.
4. Comparative analysis: Compared the accuracy score of all the models.

## 🚀 Models Used

- CNN
- VGG16
- ResNet50

## 📚 Libraries Needed

The following libraries are required to run this project:

- numpy==1.24.3
- pandas==1.5.0
- matplotlib==3.6.0
- tensorflow==2.6.0

## 📊 Exploratory Data Analysis Results

#### Best performing model accuracy:
[val_acc3](https://github.com/achrekarom12/DL-Simplified/assets/88442486/b48589ab-83e6-4ce7-86df-eebdbe35921f)

#### Best performing model loss:
[val_loss3](https://github.com/achrekarom12/DL-Simplified/assets/88442486/55072c0f-1fdb-433a-87be-c442c25d84a7)


## 📈 Performance of the Models based on the Accuracy Scores

Results on Val dataset:

| Model   | Accuracy | Loss  |
| ------- | -------- | ----- |
| CNN     | 0.728    | 1.159 |
| VGG16   | 0.925    | 0.218 |
| ResNet50| 0.735    | 1.688 |

## 📢 Conclusion

Based on the results, we can draw the following conclusions:

- CNN: The CNN model achieved an accuracy of 0.728 and a loss of 1.159. It performed reasonably well, but there is room for improvement.
- VGG16: The VGG16 model achieved a higher accuracy of 0.925 and a lower loss of 0.218. It outperformed the basic CNN model, indicating that the deeper architecture of VGG16 with more trainable parameters was able to capture more complex features and generalize better.
- ResNet50: The ResNet50 model achieved an accuracy of 0.735 and a loss of 1.688. It performed slightly better than the basic CNN model but was outperformed by VGG16. ResNet50's residual connections helped in mitigating the vanishing gradient problem and allowed for the training of deeper networks.


# Honey Bee pollen Detection
## Goal

The main goal of this project is to develop deep learning model that can accurately identify and detect pollen present on honeybees from their images. This automation can save time and effort compared to manual inspection of images, making it a valuable tool for researchers, beekeepers, and environmentalists.

## Dataset

The dataset for this project can be found at link given below.



[![AGPL License](https://img.shields.io/badge/Dataset-Link-blue.svg)](https://www.kaggle.com/datasets/ivanfel/honey-bee-pollen)

##


## Approach

- Data loading and Data preprocessing: 
     Loaded and organize honeybee image dataset.Ensure that the images are properly labeled as "contains pollen" or "does not contain pollen."    Preprocessd the images, which involve resizing, normalization, and data augmentation to increase the diversity of the dataset and improve generalization.
- Split the Dataset: Splitted the  dataset into training, validation, and testing sets. The training set will be used to train the model, the validation set for hyperparameter tuning and model selection, and the testing set for final evaluation.
- Model building:

```bash
  1.Convolutional Neural Network (CNN): Builds a cnn for pollen detection in 
  honeybee images.Chooses a suitable CNN architecture, add convolutional 
  and pooling layers for feature extraction, and fully connected layers for 
  classification. Train the model using labeled data, optimizes hyperparameters,
   and evaluate its performance on test data.
```
```bash
  2.VGG16: Builds a VGG16 model for pollen detection in honeybee images. 
  Loaded the VGG16 architecture with pre-trained weights, removing the
   classification head. Added a new head for binary classification 
   (pollen or not). Fine-tune the model on labeled data, optimizes  
   hyperparameters, and evaluate performance on test data.
```
```bash
 3.DensNet: Build a DenseNet model for pollen detection in honeybee images. 
 Load the DenseNet architecture with pre-trained weights, modify the classification 
 head for binary classification (pollen or not). Fine-tune the model on labeled data, 
 optimize hyperparameters, and evaluate performance on test data.
```
- Model evaluation: Evaluated the performance of each model using appropriate metrics such as accuracy and precision.

## Libraries Needed
1.  Pandas
2.  Tensorflow
3.  Seaborn
4.  sklearn
5.  pathlib
6.  numpy
7.  keras

## Accuracies

| Model            | Accuracy                             |
| ----------------- | ----------------------------------------------------------- |
| CNN | 85.12% |
| VGG16 | 92.09% |
| DensNet| 92.56% |

## Conclusion
 In conclusion, this project aimed to predict wether a honey bee conatins pollen or not using dl models. Among the models developed, the DensNet achieved the highest accuracy of 92.56%. 

 ## Harsh Raj



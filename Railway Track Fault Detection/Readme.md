# <h1 align = "center"> (Enhanced) Railway Track Fault Detection using Deep Learning </h1>
## Aim of the project: 
### The project focuses on detecting the faults in the railway tracks using various Deep Learning Algorithms
### Dataset Link: [railway Track fault Detection Resized (224 X 224) | Kaggle](https://www.kaggle.com/datasets/gpiosenka/railway-track-fault-detection-resized-224-x-224)

###  Libraries and Frameworks used:
1. Pandas
2. Numpy
3. Matplotlib
4. Imutils
5. OpenCV
6. Pathlib
7. Tqdm
8. Skimage
9. Tensorflow
10. Keras


## Deep Learning Algorithms used:
1. Convolutional Deural Network woth Maxpooling and Batchnormalization
2. EfficientNet50 algorithm
3. InceptionV# algorithm

Loss and accuracy of the EfficientNet50 algorithm

## Evaluation Metrics used:
1. Mean Absolute Error

## Loss Functions used for CNN:
1. Rectified Linear Unit for processing kayers
2. Softmax for the last layer

## Output Images of the Detection
#### <p align = "center"> Prediction using the CNN algorithm </p>
![CNN prediction](https://github.com/PiyushBL45t/DL-Simplified/assets/75735209/54da683b-9092-4091-a0c4-4e2a2fc3484f)

#### <p align = "center"> Prediction using InceptionV3 </p>
![Inceptionv3 prediction](https://github.com/PiyushBL45t/DL-Simplified/assets/75735209/283ca821-40fb-429c-86eb-da3ac2847f58)

#### <p align = "center"> Loss and accuracy of the EfficientNet50 algorithm </p>
![Efficinet Loss](https://github.com/PiyushBL45t/DL-Simplified/assets/75735209/fa7e7313-e4c9-49b0-9417-fa4f64993170)
![Efficient accuracy](https://github.com/PiyushBL45t/DL-Simplified/assets/75735209/804a5717-fec4-48ab-bc0b-805a99d55ccc)

## Accuracy and training time comparison of all the Deep Learning Algorithms
|             | Normal CNN | EfficientNet50 | InceptionV3 |
|-------------|------------|----------------|-------------|
|Accuracy     | 90%        | 98%            | 92%         |
|Eval Metrics | None       | MAE            | MAE         |
|Train Time   | 10 mins    | 8 mins         | 10 mins     |
|Epochs       | 20         | 50             | 50          |


## Techniques used for data preprocssing:
1. Image Prepreocssing
2. Data Preprocessing
3. Image visualizations
4. Setting up the path for defective and non defective images
5. Data Labellling and annotations
6. Building the CNN model
7. Using the pretrained models and fine tuning them
8. Converting the image data to numpy arrays
9. Checking the loss and accuracy graphs for each DL algorithm used

> ## Note: 
> ### The images were not properly named for the training purposes, so there is a script named conv.py that will change the image annotations and then creates a separate folder for processed images that can be used for model training and visualizations.





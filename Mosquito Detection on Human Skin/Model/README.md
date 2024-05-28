# Mosquito Detection on Human Skin

**GOAL**

Create a DL model which will detect the mosquito on the human skin.

**DATASET**

https://www.kaggle.com/datasets/naiborhujosua/mosquito-on-human-skin

**DESCRIPTION**

The dataset contains images of 7 different types of mosquitoes. There are 250 images of each type. The task is to classify the images by using a deep learning architecture.

**WHAT I HAD DONE**

First I imported all the required libraries and dataset for this project. Then I imported the dataset and split it into training, validation and testing sets in the ratio 70:20:10. Then I proceeded to build the model. 

I have developed 5 deep learning models to classify the images. First I used a ANN to classify the images. But I didn't get a good accuracy. Secondly I used a CNN to classify the images, but the model wasn't performing well. Lastly, I used a CNN with MaxPooling layers but I didn't get a satisfactory accuracy score. 

Then I proceeded with Transfer Learning. I used the [ResNet 50](https://tfhub.dev/google/imagenet/resnet_v2_50/feature_vector/5) model and trained this model on the images from the dataset. I first got some improvements in the accuracy, but after training the model for more epochs I got an accuracy score of 84.88

**MODELS USED**

The models are:

1. Artificial Neural Network (ANN)
2. Convolutional Neural Network (CNN)
3. Convolutional Neural Network (CNN) with MaxPooling layer
4. Transfer Learning Model (ResNet) 5 epochs
5. Transfer Learning Model (ResNet) 20 epochs

**LIBRARIES NEEDED**

* kaggle
* tensorflow
* tensorflow_hub
* matplotlib

**VISUALIZATION**

### Images of different Rice classes
![Images of different Rice classes](../Images/images_from_dataset.png)

### Model 1 (ANN Model) performance graphs
![Model 1 (ANN Model) performance graphs](../Images/model_1_plot.png)

### Model 2 (Basic CNN Model) performance graphs
![Model 2 (Basic CNN Model) performance graphs](../Images/model_2_plot.png)

By viewing the graphs, we can conclude that the model is not performing well. It is overfitting on the training data.

### Model 3 (CNN Model with MaxPooling layer) performance graphs
![Model 3 (CNN Model with MaxPooling layer) performance graphs](../Images/model_3_plot.png)

By adding the MaxPooling layer, the model is now performing better than before.

### Model 4 (Transfer Learning Model (ResNet)) performance graphs
![Model 4 (Transfer Learning Model (ResNet) 5 epochs) performance graphs](../Images/model_4_plot.png)

### Model 5 (Transfer Learning Model (ResNet) 20 epochs) performance graphs
![Model 5 (Transfer Learning Model (ResNet) 20 epochs) performance graphs](../Images/model_5_plot.png)

### Prediction

Prediction on a random image from the testing dataset.

![Prediction](../Images/prediction.png)

**ACCURACIES**

| Model         | Architecture              | Accuracy in % (on testing data) |
| ------------- |:-------------------------:|:-------------:|
| Model 1       | ANN Model                 |16.67          |
| Model 2       | Basic CNN Model           |51.13          |
| Model 3       | CNN Model with MaxPooling |71.20          |
| Model 4       | Transfer Learning Model (ResNet) 5 epochs |81.54          |
| Model 5       | Transfer Learning Model (ResNet) 20 epochs |84.88          |

**CONCLUSION**

I was successfully able to develop a Deep Learning model that can classify images from the given mosquito dataset of 7 classes.

**Omkar Jahagirdar**

Connect with me on Linkedin: https://www.linkedin.com/in/omkar-jahagirdar/
Check out my Github profile: https://github.com/omkar3602
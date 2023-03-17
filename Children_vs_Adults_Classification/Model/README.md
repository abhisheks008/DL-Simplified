# DL Simplified
Deep Learning has many application in the field of computer vision and one such application is Facial Detection & Recognition in which we also coined the work for Children vs Adults Classification 

## ✨Children vs Adults Classification✨

### Aim 
The objective of the project is to Create a DL based model which can detect gender and age using facial images. Convolutional Neural Network is used to classify the images. There are 2 output types namely, Children and Adults Classification.

### Datasets
I have used Kaggle's [EMİRHAN BULUT] (https://www.kaggle.com/datasets/die9origephit/children-vs-adults-images)

##### About Dataset
The dataset consists of over 20,000 face images with annotations of Children vs Adults Classification,  The dataset is a large-scale face dataset with long Images cover large variation in pose, facial expression, illumination, occlusion, resolution, etc. Dataset could be used on a variety of tasks, e.g., face detection, age estimation, age progression/regression, landmark localization, etc.

dataset image sample - 

![image]()
### Approach
In the notebook we have trained an pretrained CNN model using the above dataset  and adjusting the algorithm. It also uses Convolutional Layers from Convolutional Neural Networks and compare the accuracy for age and gender and it also figure out the loss during model training. We have trained the model with large variation of images which covers pose, facial expression, illumination,  occlusion, resolution, etc so that we can enhance the accuracy of the model.


Model Used 

![image]()


### Output

- Frequency Distribution of age of images used in dataset.

![image]()

- Grid View of few Images used in Dataset 

![image]()

- Children and Adults Classification

![image]()

## Testing 
Testing on random image from index 1-23708, you can also test by changing index of the image used for test, variable name image_index.

- Test Image 

Original image: Adult

Predicted image: Adult 92%

![image]()



- Test Image 

Original image: Children

Predicted image: Children 93%

![image]()




## Conclusion
We can vary the number of epochs to get more accuracy on models, here we have achieved the accuracy of more than 95% 


## License
MIT

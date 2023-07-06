
- ## Download the dataset from kaggle : https://www.kaggle.com/datasets/adityadas7888/fire-detection-dataset

The first model is a customized basic CNN architecture inspired by AlexNet architecture. To balance the efficiency and accuracy, the model is fine-tuned considering the nature of the target problem and fire data. We are going to use a datasets for training our models. The links for the datasets are available at the top of the file. 


- ## Creating the customized CNN architecture

We are going to use TensorFlow API Keras for building our model. Let’s first create our ImageDataGenerator for labeling our data. Datasets are used here for training. Finally, we will have 980 images for training and 239 images for validation.

We will use Adam as an optimizer with a learning rate of 0.0001. After training for 50 epochs, we get the training accuracy of 96.83 and validation accuracy of 94.98. The training and validation loss is 0.09 and 0.13 respectively.

![001_FireDetectionCNN](https://github.com/ADITYADAS1999/DL-Simplified/assets/58718316/3b24915a-d963-4b1a-b170-ffcd441f7607)

![002_FireDetectionCNN](https://github.com/ADITYADAS1999/DL-Simplified/assets/58718316/a8825a78-2e2b-4f2c-9978-7c0f7615c3c7)

![003_FireDetectionCNN](https://github.com/ADITYADAS1999/DL-Simplified/assets/58718316/a485f4bc-1b87-4fd0-adce-867d02ee9e42)

- ## Creating customized Inception model

Let’s import our Inception model from the Keras API. We will add our layers at the top of the Inception model as shown below. We will add a global spatial average pooling layer followed by 2 dense layers and 2 dropout layers to ensure that our model does not overfit. At last, we will add a softmax activated dense layer for 2 classes.
Next, we will first train only the layers that we added and are randomly initialized. We will use RMSprop as an optimizer here.


![004_InceptionFireDetection](https://github.com/ADITYADAS1999/DL-Simplified/assets/58718316/15b8fd56-acb6-43ca-b3ab-0f3492ea23aa)

![005_InceptionFireDetection](https://github.com/ADITYADAS1999/DL-Simplified/assets/58718316/6709cb99-831c-4094-a40e-80e89e14846d)

![006_InceptionFireDetection](https://github.com/ADITYADAS1999/DL-Simplified/assets/58718316/072a152d-d103-4c0c-aa11-ad129d58f771)

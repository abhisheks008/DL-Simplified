<h1>PROJECT TITLE</h1>
<br>
Staircases Segmentation Using DL
<br>
<h1>GOAL</h1>
<br>

The project uses 50 images of ascending and 50 images of descending stairs.The aim is to classify the stair image as ascending and descending.<br>
The models used are Transfer Learning models which are pretrained on the imagenet weights.
<br>
Staircase Segmentation has usage in robot training in the area of surveillance for military and industrial applications.For behaviour cloning and automation puroses.
<br>



<h1>DATASET</h1>
<br>
The  Dataset is taken from Kaggle
<br>
Dataset Link :- https://www.kaggle.com/datasets/akshaydattatraykhare/ascending-and-descending-staircases
<br>
Description 
<br>
There are two folders within the dataset ,one for images of ascending staircases and the other one for descending staircases.Each foldercontains 50 images of ascending staircases and 50 images of descending staircases respectively. These images have been taken using mobile phone's camera. This dataset includes interior staircases and exterior staircases of various houses. This dataset can be helpful in detection and classification of ascending and descending staircases.<br>

<h1>DESCRIPTION</h1>

The project aims at classifying the images of the staircases as ascending and descending by using Transfer Learning Models which are pretrained on imagenet weights.<br>
<br>
<h2>METHODOLOGY</h2>
<br>
<ol>The necessary libraries are imported and installed.</ol><ol>The dataset has only 100 images in total which is very less to create a robust model.To increasethe robustness and to increase the data samples,images are augmented using Augmentor by flipping,rotating,skewing,zooming,resizing the images and creating 500 samples for each label that is in total 1000 image samples are created by augmenting them from 100 samples of both ascending and descending images.An array of these 1000 samples concatenated with label(Ascending and Descending) is formed into a dataset which will be used for training and testing of the model.</ol><ol>The dataset is split into training and testing using train_test_split function of sklearn.The train size is kept 0.7 for all the models.</ol><ol>Label Encoder is used to encode the labels into 0 and 1</ol><ol>Normalization is done to normzalise the pixel values between 0 and 1</ol>
<ol>Four Transfer Learning models namely MobileNetV2,VGG16,XCeption,InceptionV3 are used for the training purpose.Sequential models are created of baseline transfer learning models along with convoluted layer,dense layers.Dropout layer is used to avoid overfitting of the model.</ol>
<ol>Loss Function used is Binary Crossentropy,optimizer is Adam,Metrics is Accuracy</ol>
<ol>Models are trained on number of epochs value ranging from 25 to 50.</ol>
<ol>To analyse the accuracy and loss Confusion Matrix,Classification Report,Accuracy Graph (Training Accuracy VS Validation Accuracy),Loss Graph(Training Accuracy VS Validation Accuracy) are generated.
</ol>
<ol>Some test samples are used to test on the trained models and predictions are made.
</ol>

<br>
<h1>MODELS USED</h1>
<br>

Transfer Learning Models pretrained on imagenet weights are used for training.Four Models namely MobileNetV2,VGG16,XCeption,InceptionV3 are used.These models are robust and have high learning rate as they are been already trained on similiar data that is imagenet.So they give better accuracy and training.
For each model different number of convolutional,dense and dropout layers are used as per their training accuracy.
Every model is different in its pursuit and are easy trainable.
<br>


<h1>LIBRARIES NEEDED</h1>

The following libraries are essential :-
<br>
<ol>Keras - open source python library which facilitates deep neural networks like convolutional ,recurrent and their combinations</ol>
<ol>Tensorflow - open source library which supports Machine Learning powered models and applications.It also works with Keras and is of high utility </ol>
<ol>Scikit-learn - Simple and efficient tools for data mining and data analysis. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means.
</ol>

<h1>VISUALIZATION</h1>

<h2>MOBILENETV2</h2><br>
<h2>ACCURACY CURVE<h2>
![Mobilenet_acc_curve](Mobilenet_acc_curve.png)
<img src="https://github.com/kanishkakataria/DL-Simplified/blob/main/Staircases%20Segmentation%20Using%20DL/Images/Mobilenet_acc_curve.jpg"></img>
<h2>LOSS CURVE<h2>
<br>
<img src="C:\Users\Dell\Desktop\Open Source\DL-Simplified\Staircases Segmentation Using DL\Images\Mobilenet_loss_Curve.jpg">
ACCURACIES

Add all the algorithms used with their accuracies and results

CONCLUSION

What's the conclusion derived from this project and also showcase the accuracy results if it's applicable. Be briefer. Use accuracy scores to find the best fitted model among all the developed models for the particular projects.

YOUR NAME

Add your name at the end of the file, along with social media handles if applicable!
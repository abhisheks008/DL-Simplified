<h1>PROJECT TITLE</h1>
<br>
<h3>
<u>Staircases Segmentation Using DL</u></h3>
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
There are two folders within the dataset ,one for images of ascending staircases and the other one for descending staircases.Each folder contains 50 images of ascending staircases and 50 images of descending staircases respectively. These images have been taken using mobile phone's camera. This dataset includes interior staircases and exterior staircases of various houses. This dataset can be helpful in detection and classification of ascending and descending staircases.<br>

<h1>DESCRIPTION</h1>

The project aims at classifying the images of the staircases as ascending and descending by using Transfer Learning Models which are pretrained on imagenet weights.<br>
<br>
<h2>METHODOLOGY</h2>
<br>
<ol>
<li>The necessary libraries are imported and installed.</li><li>The dataset has only 100 images in total which is very less to create a robust model.To increasethe robustness and to increase the data samples,images are augmented using Augmentor by flipping,rotating,skewing,zooming,resizing the images and creating 500 samples for each label that is in total 1000 image samples are created by augmenting them from 100 samples of both ascending and descending images.An array of these 1000 samples concatenated with label(Ascending and Descending) is formed into a dataset which will be used for training and testing of the model.</li><li>The dataset is split into training and testing using train_test_split function of sklearn.The train size is kept 0.7 for all the models.</li><li>Label Encoder is used to encode the labels into 0 and 1</li><li>Normalization is done to normzalise the pixel values between 0 and 1</li>
<li>Four Transfer Learning models namely MobileNetV2,VGG16,XCeption,InceptionV3 are used for the training purpose.Sequential models are created of baseline transfer learning models along with convoluted layer,dense layers.Dropout layer is used to avoid overfitting of the model.</li>
<li>Loss Function used is Binary Crossentropy,optimizer is Adam,Metrics is Accuracy</li>
<li>Models are trained on number of epochs value ranging from 25 to 50.</li>
<li>To analyse the accuracy and loss Confusion Matrix,Classification Report,Accuracy Graph (Training Accuracy VS Validation Accuracy),Loss Graph(Training Accuracy VS Validation Accuracy) are generated.
</li>
<li>Some test samples are used to test on the trained models and predictions are made.
</li>
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
<ol>
<li>Keras - open source python library which facilitates deep neural networks like convolutional ,recurrent and their combinations</li>
<li>Tensorflow - open source library which supports Machine Learning powered models and applications.It also works with Keras and is of high utility </li>
<li>Scikit-learn - Simple and efficient tools for data mining and data analysis. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means.
</li>

<h1>VISUALIZATION</h1>

<h2>ACCURACY CURVE<h2>

![Mobilenet_acc_curve ](https://github.com/kanishkakataria/Images/assets/85161519/40135c42-46df-40f4-9aba-1cfdc8d0be2d)
<br>
![Xception_acc_graph](https://github.com/kanishkakataria/Images/assets/85161519/379debcf-9739-477c-b8bd-40735f86ad46)
<br>
![InceptionV3_ACC graph](https://github.com/kanishkakataria/Images/assets/85161519/7d4ea849-13c7-4c70-bc9e-6f17942f3b0e)
<br>
![VGG16_acc_curve](https://github.com/kanishkakataria/Images/assets/85161519/483b35b1-f711-49b1-ba5a-e2ceb6776544)
<br>

<h2>LOSS CURVE<h2>

![Mobilenet_loss_Curve](https://github.com/kanishkakataria/Images/assets/85161519/ee7c40f1-e7a2-4b1e-881d-c5767a1087ef)
<br>
![Xception_loss_curve](https://github.com/kanishkakataria/Images/assets/85161519/ec725122-8a07-41f8-a74f-7e051f4263b0)
<br>

![InceptionV3_loss_graph](https://github.com/kanishkakataria/Images/assets/85161519/7352f92a-f79f-4502-8770-91762f97d86a)
<br>
![VGG16_loss_curve](https://github.com/kanishkakataria/Images/assets/85161519/0ce9b5c3-78e2-4da3-9bf4-be3d98ebf7b6)
<br>

<h1>ACCURACIES</h1>
<ol>
<li>MOBILENETV2 - 99.9%</li>
<li>VGG16 - 99.5%</li>
<li>INCEPTIONV3 - 99%</li>
<li>XCEPTION - 99.8%</li>

</ol>

<h1>CONCLUSION</h1>

The models are trained well with validation accuracies close to 99.9% in MobilenetV2,Inception,Xception and 99.5% in VGG16
To avoid overfitting augmentation,dropout layers was used.The number of layers,train test split and batch size was changed to peform trial and testing for better accuracies.

VGG16 model is said to be the best as it is not overfitting and generalises the data well comparatively.This is clearily shown in the predictions made through test samples on the trained model.

<h1>CONTRIBUTOR</h1>

NAME - KANISHKA KATARIA
<br>
GITHUB - https://github.com/kanishkakataria
<br>
LINKEDIN - https://kanishkakataria.vercel.app/
<br>
PORTFOLIO -https://kanishkakataria.vercel.app/

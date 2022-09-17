# Google Recaptcha Image Classification

GOAL: To make a CNN to classify different images.

DATASET: [Google Recaptcha Image Dataset](https://www.kaggle.com/datasets/mikhailma/test-dataset)

DESCRIPTION: The dataset has near to 12000 RGB images of dimentions 120x120 pixels. They are scattered across 12 categories namely - 
1. Bicycle (780 images)
![](../Images/bicycle.png)
2. Bridge (533 images)
![](../Images/bridge.png)
3. Bus (1209 images)
![](../Images/bus.png)
4. Car (3558 images)
![](../Images/car.png)
5. Chimney (124 images)
![](../Images/chimney.png)
6. Crosswalk (1240 images)
![](../Images/crosswalk.png)
7. Hydrant (952 images)
![](../Images/hydrant.png)
8. Motorcycle (81 images)
![](../Images/motorcycle.png)
9. Other (1340 images)
![](../Images/other.png)
10. Palm (911 images)
![](../Images/palm.png)
11. Stair (211 images)
![](../Images/stairs.png)
12. Traffic Light (719 images)

As you can see that the dataset is highly imbalanced as for example the category Car has 3558 images where as Motorcycle only 81. The data is balanced using Augmentator library, which is explained below. 

<br>
#### METHODOLOGY 
Augmentor library is used to produce augmented images to make the dataset balanced. Using Augmentator we are applying augmentations to data such as rotation, skew, horizontal mirroring, changing brightness and contrast until there are a total of 2000 images in a perticular category (this number can be changed while running).
All of the images are stored in a different folder named "balanced_images".

The tensorflow input pipeline is given this directory (balanced_images) to take images from. Training and validation datasets are created with a 70-30 split.
Augmentation is again added to the pipeline in order to overcome any changes of overfitting. Images are resized, fliped and rotated and scaled in this layer. We don't convert the data to greyscale as it may benifit to take color in to consideration while classifying certain categories. For example, the model benifits from identifying the color red of a fire hydrant or green from palm trees.

To use the hardware effectively we optimize the pipeline by caching and prefetching the dataset. 

Model - 
![Model Shape](../Images/HyperparameterTestModel.png)

To reduce overfitting Batch Normalization is performed on the outputs before applying an activation function. Leaky ReLU is used as the activation function as it gives better performance than ReLU. 
The main reason behind using Batch Normalization is that it gives better results when the data is overfitting. Given that the dataset is such that it doesn't want bots to easily classify between the categories (purpose of captcha). This technique helps the weights to be tuned more effectively so that the validation metrics match with the training metrics and thus prevent overfitting.
This architecture was just to get the best combination of different hyperparameters.

<br>
#### Results


[Tensorboard](https://tensorboard.dev/experiment/sW4rl4fnSmK0CN5LBMuEyQ/#scalars)

From the results we can see that <b>RMSProp(Root Mean Squared Propagation)</b> as the optimizer with <b>Sparse Categorical Crossentropy</b> as the loss function and <b>Leky ReLU</b> as the activation function gave the best performance out of all. The graph would go up even more if trained for more epochs.

[Hyperparameter Combinations](https://tensorboard.dev/experiment/6EDBd1dqRBO97cmuGN8MbQ/#scalars)
The above link shows how different combinations of layers and number of neurons in them affect the accuracy and loss (both training and validation).
But because of computational limitations all combinations are not present.

<b>c2DLayers</b> - Number of 2D convolutional layers.
<b>c2DFilters</b> - Number of filters in a convolutional layer.
<b>denseLayers</b> - Number of dense layers.
<b>denseNeurons</b> - Number of neurons in a dense layer.

On the basis of the computed (as only the subset of the combinations were trained) results the lowest validation accuracy is of 2.28 and highest validation accuracy is 0.45.

On the above basis we can assume that, because of the dataset where images were choosen specifically so that a bot cannot calssify them, we result with a overfitted data.

One thing to note is that metrics may vary if the model is allowed to train for more epochs.

<br>
#### Libraries Needed
1. Augmentor
2. Tensorflow
3. Numpy
4. Matplotlib
5. PIL
6. Random
7. Datetime
8. Shutil
# Google Recaptcha Image Classification

**GOAL**<br>
To make a CNN to classify different images.

**DATASET**<br>
[Google Recaptcha Image Dataset](https://www.kaggle.com/datasets/mikhailma/test-dataset)

**DESCRIPTION**<br>
The dataset has near to 12000 RGB images of dimentions 120x120 pixels. They are scattered across 12 categories that are - 
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
<br><br>

**METHODOLOGY**<br><br>
Augmentor library is used to produce augmented images to make the dataset balanced. Using Augmentator we are applying augmentations to data such as rotation, skew, horizontal mirroring, changing brightness and contrast until there are a total of 2000 images in a perticular category (this number can be changed while running).
All of the images are stored in a different folder named "balanced_images".

The tensorflow input pipeline is given this directory (balanced_images) to take images from. Training and validation datasets are created with a 70-30 split.
Augmentation is again added to the pipeline in order to overcome any changes of overfitting. Images are resized, fliped and rotated and scaled in this layer. We don't convert the data to greyscale as it may benifit to take color in to consideration while classifying certain categories. For example, the model benifits from identifying the color red of a fire hydrant or green from palm trees.

To use the hardware effectively we optimize the pipeline by caching and prefetching the dataset. 

**Model** - <br>
![Model Shape](../Images/HyperparameterTestModel.png)

To reduce overfitting Batch Normalization is performed on the outputs before applying an activation function. Leaky ReLU is used as the activation function as it gives better performance than ReLU. 
The main reason behind using Batch Normalization is that it gives better results when the data is overfitting. Given that the dataset is such that it doesn't want bots to easily classify between the categories (purpose of captcha). This technique helps the weights to be tuned more effectively so that the validation metrics match with the training metrics and thus prevent overfitting.
This architecture was just to get the best combination of different hyperparameters.
<br><br>

**RESULTS**<br>

[Hyperparameter Combination Performance](https://tensorboard.dev/experiment/sW4rl4fnSmK0CN5LBMuEyQ/#scalars) <br>

**Validation Accuracy**

![Validation Accuracy](../Images/hyperparameterTestingValidationAccuracy.svg) <br>

**Validation Loss**

![Validation Accuracy](../Images/hyperparameterTestingValidationLoss.svg)

(You can check what each color means from the link above)

From the results we can see that <b>RMSProp(Root Mean Squared Propagation)</b> as the optimizer with <b>Sparse Categorical Crossentropy</b> as the loss function and <b>Leky ReLU</b> as the activation function gave the best performance out of all. The graph would go up even more if trained for more epochs.

<br>

[Layer|Neuron Combination Performance](https://tensorboard.dev/experiment/6EDBd1dqRBO97cmuGN8MbQ/#scalars) <br>
The above link shows how different combinations of layers and number of neurons in them affect the accuracy and loss (both training and validation).

<b>c2DLayers</b> - Number of 2D convolutional layers. <br>
<b>c2DFilters</b> - Number of filters in a convolutional layer. <br>
<b>denseLayers</b> - Number of dense layers. <br>
<b>denseNeurons</b> - Number of neurons in a dense layer. <br>

**NOTE** -> Output of the second last cell is abruptly terminated in between as its goal is to train the create and train the model iteratively with different number of layers and neurons in them. And because of the computational limitations all combinations are not present.

<br>

**If you are running this cell then you should also consider stopping it in between**

That said even if it runs for half or 1/4 of the total iterations, you should get a good enough idea of how the curve will look like from the above (tensorboard) results.
<br><br>

**CONCLUSION**<br>

On the basis of the computed results (as only the subset of the combinations were trained) the lowest validation accuracy is of 2.28 and highest validation accuracy is 0.45.

On the above basis we can assume that, because of the dataset where images were choosen specifically so that a bot cannot calssify them, we result with a overfitted data.

**One thing to note is that metrics may vary if the model is allowed to train for more epochs.**
<br>

**Libraries Needed**<br>
1. Augmentor <br>
2. Tensorflow <br>
3. Numpy <br>
4. Matplotlib <br>
5. PIL <br>
6. Random <br>
7. Datetime <br>
8. Shutil <br>
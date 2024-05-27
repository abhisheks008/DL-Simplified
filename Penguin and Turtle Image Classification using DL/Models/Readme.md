**PROJECT TITLE**: Penguin and Turtle Image Classification using DL

**GOAL**: To detect penguin and turtle images and classify them

**DATASET**: https://www.kaggle.com/datasets/abbymorgan/penguins-vs-turtles

**DESCRIPTION**:

The task relies on use of Baseline CNN model and ResNet 50 to detect if the given images are of penguins or turtles. ResNet (Residual Networks) and EfficientNet are popular deep learning architectures. ResNet introduces skip connections to mitigate vanishing gradient issues. EfficientNet optimizes model efficiency by balancing depth, width, and resolution. ResNet is well-established, while EfficientNet achieves competitive accuracy with fewer parameters, making it computationally efficient for resource-constrained environments.

**TASKS PERFORMED**:
1. Dataset created from the set of images and tagged as 1 and 0
2. Resizing, padding and augmentation tasks were done to properly extract features necessary for classification tasks
3. The Resnet50 model is used from keras_Cv to classify images, with box_loss and classification_loss as parameters used to compare the efficiency.
4. On the other hand, we prepare an EffecientNet model, with accuracy and loss as metrics used to reflect the performance of the model
5. Lastly confusion matrices help determine the misclassifications and correct classification for each type.

**MODELS USED**:
EfficientNet
ResNet


**LIBRARIES NEEDED**:

1. Numpy
2. Pandas
3. Matplotlib
4. Scikit-learn
5. Tensorflow
6. Keras

**VISUALIZATION**

![Alt text](<../Images/Screenshot (338).png>) ![Alt text](<../Images/Screenshot (335).png>)

The graphs compare loss of data for ResNet vs Effecient Net effectively
**ACCURACIES**: 
Loss ranges around 0.10 to 9.20 for ResNet, while at averages at about 1 for EfficientNet architecture.  ResNet exhibits a lower classification loss than EfficientNet on this dataset, which may suggest that ResNet is more effective in capturing the specific features and patterns present in the given images, which is essential while classifying animal images

**CONCLUSION**:
ResNet and EfficientNet are popular convolutional neural network architectures used for image classification tasks, including the detection of turtle and penguin images. ResNet employs residual learning, addressing the vanishing gradient problem by introducing skip connections, making it deeper and more effective. This helps capture intricate features in the images, crucial for identifying unique characteristics of turtles and penguins.

EfficientNet, on the other hand, optimizes model efficiency by balancing model depth, width, and resolution through a compound scaling method. It achieves high accuracy with fewer parameters, making it computationally efficient for detecting distinct patterns in turtle and penguin images.

Both ResNet and EfficientNet can be fine-tuned on the dataset containing annotated turtle and penguin images to create models which are highly accurate with upwards of 95% accuracy


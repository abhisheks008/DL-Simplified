# SEA ANIMAL DETECTION USING DEEP LEARNING
Full name : Aindree Chatterjee

GitHub Profile Link : https://github.com/aindree-2005

Email ID : aindree2005@gmail.com

Program : CodePeak

Approach for this Project :

**Description**
Using CNNS to handle image data and identify sea animals from a diverse set

**Model Used**
Input Layers:
Type: Conv2D
Parameters:
64 filters
Kernel size of (5, 5)
Activation function: ReLU
Padding: 'valid'
Input shape: (224, 224, 3)
This layer is responsible for detecting 64 different features using 5x5 convolutional filters on the input image.
Max Pooling Layer:

Type: MaxPooling2D
Parameters:
Pool size of (2, 2)
This layer performs max pooling, reducing the spatial dimensions of the representation.
Dropout Layer:

Type: Dropout
Parameters:
Dropout rate: 0.2
Dropout layers are used to prevent overfitting by randomly setting a fraction of input units to 0 at each update during training.
Batch Normalization Layer:

Type: BatchNormalization
Batch normalization normalizes the activations of the network, which can help improve training stability and speed.
Repeat of Convolutional, Pooling, Dropout, and Batch Normalization Blocks:

Similar blocks are repeated three more times with different filter sizes and configurations:
128 filters, (5,5) kernel, ReLU activation, MaxPooling, Dropout, and BatchNormalization.
256 filters, (3,3) kernel, ReLU activation, MaxPooling, Dropout, and BatchNormalization.
512 filters, (3,3) kernel, ReLU activation, MaxPooling, Dropout, and BatchNormalization.
1024 filters, (3,3) kernel, ReLU activation, MaxPooling.
Flatten Layer:

Type: Flatten
This layer flattens the input to a one-dimensional array, preparing it for the fully connected layers.
Dense Layer (Fully Connected):

Type: Dense
Parameters:
512 units/neurons
Activation function: ReLU
This layer connects every neuron in the previous layer to every neuron in this layer.
Dense Output Layer:

Type: Dense
Parameters:
Number of units: equal to the number of labels/classes
Activation function: Softmax
This is the output layer responsible for producing the final classification probabilities for each class.
**Visualisation**
Visualisation plots have been added in notebook for showing class distribution, accuracy and loss in data while training

**Accuracies**
90.19% using CNN

**My Conclusion**
Convolutional Neural Networks (CNNs) are ideal for sea animal detection due to their ability to automatically learn hierarchical features from image data. The hierarchical nature of CNNs allows them to capture spatial patterns and features crucial for identifying sea animals in underwater images. With their capacity to recognize complex patterns, CNNs excel at image classification tasks, making them well-suited for accurately detecting and classifying diverse sea creatures in marine environments.

**YOUR NAME**
Aindree Chatterjee

This project is using the MNIST digit classification dataset whose link has been given in the dataset folder.

Model 1:
Artificial neural network have been used to classify the handwritten digits into 10 classes. After feauture scaling, the 28x28 image was flattened and fed to the neural network. The input layer consists of 784 neurons followed by a single hidden layer with 100 neurons and 10 output neurons. The output layer uses the 'softmax' function and the optimiser used here is 'adam'. The model was trained for 10 epochs.

Model 2:
Convolutional neural network have been used to classify the handwritten digits into 10 classes. After feauture scaling, the 28x28 image was passed through 2 pairs of convolution layers and maxpooling layers.Then it was flattened and fed to the neural network with 128 units. After that a dropout layer was added to avoid overfitting. It was again passed through dense layer to finally classify the image. This model was also trained for 10 epochs and the optimiser used was adam.
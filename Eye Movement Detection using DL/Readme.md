# Eye Movement Detection using DL

## PROJECT TITLE

Eye Movement Detection using Deep Learning

## GOAL

The goal of this project is to develop a Deep Learning model capable of identifying the movements of the eyeballs.

## DATASET

The dataset used for this project can be found here: https://www.kaggle.com/datasets/priyankraval/eyet4empathy-eye-movement-and-empathy-dataset

## DESCRIPTION

This project focuses on leveraging Deep Learning techniques to detect and analyze eye movements.

## WHAT I HAD DONE

Data collection: Utilized the provided dataset to extract eye movement information.
Data preprocessing: Prepared the data for model training and testing.
Model selection: Implemented four different models - CNN, RNN, CapsNet, and GoogLeNet.
Comparative analysis: Evaluated and compared the performance of each model.
Exploratory Data Analysis
Total Number of Samples: 4844304
Total Number of Classes: 25

## MODELS SUMMARY
Model 1: Convolutional Neural Network (CNN)
markdown
Copy code
Model: "cnn_model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 5349398, 96)    30222010 
_________________________________________________________________
...
_________________________________________________________________
dense (Dense)                (None, 96)             17568 
=================================================================
Total params: 30241931 (115.36 MB)
Trainable params: 30241931 (115.36 MB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
Model 2: Recurrent Neural Network (RNN)
markdown
Copy code
Model: "rnn_model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
simple_rnn (SimpleRNN)      (None, 5349398, 100)    166055 
_________________________________________________________________
...
_________________________________________________________________
dense (Dense)                (None, 10)             11200
=================================================================
Total params: 166056 (63.35 MB)
Trainable params: 166056 (63.35 MB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
Model 3: Capsule Network (CapsNet)
markdown
Copy code
Model: "capsnet_model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
capsule_layer (CapsuleLayer) (None, 4844304, 71)    3470325
_________________________________________________________________
...
_________________________________________________________________
dense (Dense)                (None, 9)              7032
=================================================================
Total params: 3477525 (178.89 MB)
Trainable params: 3477525 (178.89 MB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
Model 4: GoogLeNet
markdown
Copy code
Model: "googlenet_model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
inception_block (InceptionB) (None, 65522701, 50)    108908
_________________________________________________________________
...
_________________________________________________________________
dense (Dense)                (None, 10)             493
=================================================================
Total params: 502 (100.09 MB)
Trainable params: 502 (100.09 MB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________

## LIBRARIES NEEDED
The following libraries are required to run this project:

matplotlib
tensorflow
keras
numpy
pandas
glob
seaborn
gboost
sklearn

## EVALUATION METRICS
The evaluation metrics used to assess the models:
Accuracy
Loss

## CONCLUSION
Based on the results, the Model 1: CNN outperforms the other models in terms of accuracy and loss. Further optimizations and fine-tuning can be explored for better performance.
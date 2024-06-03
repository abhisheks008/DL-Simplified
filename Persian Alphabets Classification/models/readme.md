## Work flow

1. Data Collection:

- Download the dataset from [Kaggle](https://www.kaggle.com/datasets/mostafamohammadi1/persian-alphabets-and-numbers)
- Curate and organize the dataset into appropriate folders.

2. Data Preprocessing:

- Load the dataset and preprocess the images.
- Resize the images to a uniform size.
- Split the dataset into training and testing sets.
- Convert images to numerical arrays for model input.

3. Model Architecture Design:

- Design a hybrid architecture combining CNN and LSTM layers.
- Define the number of layers, filter sizes, and activation functions.
- Compile the model with appropriate loss function and optimizer.

4. Model Training:

- Feed the preprocessed data into the model for training.
- Iterate over multiple epochs to allow the model to learn the patterns in the data.
- Adjust the model parameters based on training performance.

5. Model Evaluation:

- Evaluate the trained model on the test dataset.
- Calculate performance metrics such as accuracy, loss, and classification reports.
- Visualize the training and validation metrics to assess model performance.

## Evaluation Metrics

<p align="center">

<img src="https://github.com/abhisheks008/DL-Simplified/assets/103712713/5ab41544-11bc-4439-80ea-c146901dc553" />
</p>

## Findings

1. Standalone CNN Model: The standalone CNN model achieved a classification accuracy of 95.1% on the test dataset. This indicates that the CNN model was effective in extracting relevant features from the input images of Persian alphabet characters and making accurate predictions.

2. Standalone LSTM Model: The standalone LSTM model reported a classification accuracy of 94.9% on the test dataset. This suggests that the LSTM model was successful in capturing sequential patterns in the input data and performing well in classifying Persian alphabet characters.

3. Hybrid Model: Surprisingly, the hybrid CNN-LSTM model yielded a slightly lower classification accuracy of 94.2% compared to the standalone models. This suggests that the combination of CNN and LSTM layers did not provide significant improvement over using either model alone for Persian alphabet classification.

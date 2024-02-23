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

🎯 AIM

The aim of this project is to create neural networks that can be used to predict weather a person will get loan or not based on some information like `qualification` `number of dependents` `annual income` `asset values` etc.

🧵 Dataset

The Bank dataset is taken from Kaggle and can be found https://www.kaggle.com/datasets/architsharma01/loan-approval-prediction-dataset/data. The dataset for this project consists of labeled data. The target column is called `loan_status` which is used to predict whether a customer gets approved for loan or not.

🧾 Description

For training the model, lot of experiments have been done and 8 model's are trained few major hilights are:

6 different sequential dense networks with different layers 
2 models by running `Hyperparameter tuning` experiment with different `optimizers`, `loss functions` and `max_trails`

🧾 Data Preprocessing

These are the observations which are made on dataset.
   1. There is no null value and duplicated value in this dataset.
   2. no_of_dependents, education, self_employed and loan_status are categorical columns.
   3. here are a total 4269 rows in this dataset, with 13 columns (features).
   4. here are 2656 data with an approved loan_status, which is about 62.2% compared to the "rejected" group. The dataset is slightly imbalanced but it is acceptable and we don't need to rebalance it.
   5. `education`, `self_employed` and `loan_status` i.e. 3 are categorical columns Other columns are numerical.

🚀 Models Implemented

Three deep learning algorithms are implemented which given test accuracy of almost 95%. These models are described as follows:



For the first 1-6 models:
Layers:
The layers are dense layers with different number of neurons and uses `ReLU` activation function expect for the output layer which uses `sigmoid` activation.
The loss functions have been changed from model to model and uses between `Adam` or `SGD`.
The layers of these model are variable and changes from model to model.

The next 2 model's (Model 6&7 which are obtained by hyper parameter tuning):

The model 7:
- For finding this model `10 trails` have been made during the hyperparameter training.

- Trails on different `no.of layers`, `no.of neurons` in each layer and different `learning_rate` have been made.
- EarlyStopping Callback is also used to prevent model from overfitting.
- This model have validation accuracy of 94.9% and test accuracy of 94.8%

  
  <img width="387" alt="Screenshot 2024-05-24 at 8 22 36 PM" src="https://github.com/kumar8074/Bank-loan-approval-prediction/assets/99739282/4e56abec-849f-4ada-ab03-e9871f8542bd">



  <img width="740" alt="Screenshot 2024-05-24 at 8 24 59 PM" src="https://github.com/kumar8074/Bank-loan-approval-prediction/assets/99739282/02f0c81e-422b-44dd-aaf2-0b0ae3024dfe">




  Model 8:
  - For finding this model `20 trails` have been made during the hyperparameter training.
  - Trails on different `no.of layers`, `no.of neurons` in each layer `learning_rate` different `activation functions` and different `optimizers` have been made.
  - activation functions are ['relu', 'leaky_relu', 'elu', 'swish', 'linear']
  - optimizers are ['adam', 'rmsprop', 'nadam', 'adagrad', 'adadelta', 'sgd']
  - EarlyStopping Callback is also used to prevent model from overfitting.
  - This model have validation accuracy of 94.8% and test accuracy of 95.5%
 
    
    <img width="390" alt="Screenshot 2024-05-24 at 8 32 36 PM" src="https://github.com/kumar8074/Bank-loan-approval-prediction/assets/99739282/56cd20e6-4f40-46a7-890e-5d9e03f64b25">






    <img width="735" alt="Screenshot 2024-05-24 at 8 33 51 PM" src="https://github.com/kumar8074/Bank-loan-approval-prediction/assets/99739282/edbfb984-53a8-427a-b146-e5b4a6a0eda1">



However the model 1 has the best accuracy of 96.25%.
- It is a simple model with 3 dense layers
- The layer 1&2 uses `100 neurons` each and have `ReLU` activation
- The output layer uses `1 neuron` since it is a binary classification and uses `sigmoid` activation.
- The loss function is `binary_crossentropy` and optimizer is `Adam`.
  <img width="743" alt="Screenshot 2024-05-24 at 8 40 10 PM" src="https://github.com/kumar8074/Bank-loan-approval-prediction/assets/99739282/06510ebd-e8f3-431f-8d99-0d7937306cb1">


  <img width="579" alt="classification-report" src="https://github.com/kumar8074/Bank-loan-approval-prediction/assets/99739282/0d353f29-dd06-4d56-b033-7b69f710fc19">



    

**PROJECT TITLE**
Store Sales Prediction using Deep Learning

**GOAL**
Store Sales Prediction using Deep Learning
**DATASET**
https://www.kaggle.com/competitions/store-sales-time-series-forecasting/overview

**DESCRIPTION**
The project uses RNN to make predictions for store sales.Dataset is  updated daily and is dynamic. The project also aims to compare performance of Lasso, Ridge and Decision Tree regression models with respect to the use of Regression models
**WHAT I HAD DONE**
1. Used EDA and correlation matrix to figure out needed features
2. Tested using basic ML models like Ridge, Lasso, Linear and Decision Tree Regression
3. Tested using RNNs. Used multilayer networks for time-series data
4. RNNs have proven to be far more useful and versatile

**MODELS USED**
Lasso Regression, Ridge Regression,Decision Tree Regression, RNN

**LIBRARIES NEEDED**
Pandas, Numpy, Keras,TensorFlow, ScikitLearn, Seaborn, Matplotlib

**VISUALIZATION**
 We use correlation matrix to visualize required features.
 Line Charts are used to visualize day/month/store wise sales 

**ACCURACIES**
MAE is lowest for RNNs at 55 to 70.
The highest MAE is provided by Linear Regression at 1000+ and considerably better by Lasso Regression and Decision Tree at a little over 100.

**CONCLUSION**
Recurrent Neural Networks (RNNs) are employed for time series data due to their ability to capture temporal dependencies. RNNs maintain a memory of past information, enabling them to process sequential data with contextual awareness. This makes them well-suited for tasks such as stock price prediction or weather forecasting, where understanding patterns over time is crucial. The recurrent nature of RNNs facilitates the modeling of dynamic relationships within time series datasets, enhancing their effectiveness in capturing temporal dependencies.

**YOUR NAME**
Aindree Chatterjee
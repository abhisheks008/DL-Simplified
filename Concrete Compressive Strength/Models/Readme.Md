## **PROJECT TITLE**

Concrete Compressive Strength Prediction Using Deep Learning

### 🎯 **Goal**

To find best option for Concrete Compressive Strength Prediction by comparing across various models

### 🧵 **Dataset**

https://www.kaggle.com/datasets/elikplim/concrete-compressive-strength-data-set/data

### 🧾 **Description**

The project compares maximum absolute error as parameter to find the best option for Concrete Compressive Strength Prediction . Models used are XGBoostRegressor, RandomForest Regressor, LGBRegressor and Sequential Keras Model amongst others.Concrete is the most important material in civil engineering. The concrete compressive strength is a highly nonlinear function of age andingredients. These ingredients include cement, blast furnace slag, fly ash,water, superplasticizer, coarse aggregate, and fine aggregate.

### 🧮 **What I had done!**
- Used correlation matrix as EDA tool for visualizing correlation between columns
- Used Normalizer on the columns and then performance of  various regression models like LGBMRegressor,DecisionTreeRegressor,KNeighborsRegressor and so on were compared in a table, based on RMSE, MSE, MAE,R2 SCORE
- The hyperparameters were tuned for the most effective model to get 91.39% accuracy and 3.1 MAE
- Now, we used Normalizer and Keras Sequential model with Dense Layers and RelU to get 3.9 MAE. Thus it's performance is comparable to LGBRegressor

### 🚀 **Models Implemented**

**Algorithms Used**:

- GradientBoostingRegressor
- LGBMRegressor
- XGBRFRegressor
- DecisionTreeRegressor
- LinearRegression
- KNeighborsRegressor
- RandomForestRegressor
- BaggingRegressor (ExtraTreeRegressor with random_state=42)
- GaussianProcessRegressor

The above algorithms were used and a function was written to compare the MAE, and accuracy

Then a Keras Sequential model with  Dense Layers was used to compare performance of MAE, the most accurate error metric in such tasks.

### 📚 **Libraries Needed**

Pandas, Numpy, Keras,TensorFlow, ScikitLearn, Seaborn, Matplotlib

### 📊 **Exploratory Data Analysis Results**

![](https://github.com/abhisheks008/DL-Simplified/blob/main/Concrete%20Compressive%20Strength/Images/Screenshot%20(243).png)
![](https://github.com/abhisheks008/DL-Simplified/blob/main/Concrete%20Compressive%20Strength/Images/Screenshot%20(244).png)

### 📈 **Performance of the Models based on the Accuracy Scores**

Add all the algorithms used with their accuracies and results

### 📢 **Conclusion**

**Gradient Boosting Algorithm:**

LightGBM is a gradient boosting framework, which is an ensemble learning technique. It builds a predictive model in the form of an ensemble of weak learners (usually decision trees), and it combines their predictions to create a stronger overall model.
Gradient boosting algorithms, in general, are powerful for regression tasks, as they iteratively improve the model by focusing on the errors made in the previous iterations.

**LightGBM's Advantages:**
- Lightweight and Fast: LightGBM is designed to be efficient and fast. It is especially useful when dealing with large datasets or datasets with a large number of features.

- Leaf-Wise Growth: LightGBM grows trees leaf-wise rather than level-wise, which can lead to a more efficient and accurate model.

- Handling Non-Linear Relationships:Concrete compressive strength prediction has non-linear relationships between the input features and the target variable. Gradient boosting algorithms, including LightGBM, are well-suited for capturing complex, non-linear patterns in the data.

Neural Networks also similar level of accuracy to LGBMRegressor.RandomForest Regressor had 2nd highest accuracy Level.The Keras Sequential model is designed for building simple feedforward neural networks. Since the data can be effectively modeled as a series of layers where information flows in one direction (from input to output), a Sequential model is a natural and straightforward choice. The level of accuracy is at part with LightGBM

Lowest Absolute Error is shown for LGBRegressor and Keras Sequential Models at 3.1 and 3.9 respectively, making them the most suitable

### ✒️ **Your Signature**

Shravya pamu 

Comparison between LGBMRegressor, and Neural Network

**Gradient Boosting Algorithm:**
LightGBM is a gradient boosting framework, which is an ensemble learning technique. It builds a predictive model in the form of an ensemble of weak learners (usually decision trees), and it combines their predictions to create a stronger overall model.
Gradient boosting algorithms, in general, are powerful for regression tasks, as they iteratively improve the model by focusing on the errors made in the previous iterations.
**LightGBM's Advantages:**
-Lightweight and Fast: LightGBM is designed to be efficient and fast. It is especially useful when dealing with large datasets or datasets with a large number of features.
-Leaf-Wise Growth: LightGBM grows trees leaf-wise rather than level-wise, which can lead to a more efficient and accurate model.
Handling Non-Linear Relationships:
-Concrete compressive strength prediction has non-linear relationships between the input features and the target variable. Gradient boosting algorithms, including LightGBM, are well-suited for capturing complex, non-linear patterns in the data.

Neural Networks also similar level of accuracy to LGBMRegressor.RandomForest Regressor had 2nd highest accuracy Level.The Keras Sequential model is designed for building simple feedforward neural networks. Since the data can be effectively modeled as a series of layers where information flows in one direction (from input to output), a Sequential model is a natural and straightforward choice. The level of accuracy is at part with LightGBM

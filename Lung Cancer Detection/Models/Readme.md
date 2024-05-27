## Lung Cancer Detection Using Ten Models
# Goal
The goal is to compare performance of standard machine learning models to Keras Sequential Model, which is in total 10 models
## Dataset
The dataset is : https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer/data
## Description
The effectiveness of cancer prediction system helps the people to know their cancer risk with low cost and it also helps the people to take the appropriate decision based on their cancer risk status. The data is collected from the website online lung cancer prediction system .

## What I have done
1.  Data cleaning and removal of duplicates.
2. EDA to see dependance of parameters and data distribution
3. SMOTE to balance classes for imbalanced data
4. Using 9 models (std. ML) for checking performance and classification
5. Designing a Keras Sequential Model for Lung Cancer Detection 

## Libraries used
1. numpy
2. pandas
3. matplotlib
4. seaborn
5. tensorflow
6. keras
7. sklearn 

## Visualization
![Alt text](<../Images/Screenshot (379).png>)
![Alt text](<../Images/Screenshot (381).png>)
![Alt text](<../Images/Screenshot (384).png>)

## Models Used
1. Logistic Regression
2. KNN
3. SVC
4. DecisionTree Classifier
5. Random Forest Classifier
6. Catboost Classifier
7. XGBoost Classifier
8. LGBM Classifier
9. Keras Sequential Models
## Accuracy
1. Logistic Regression - 0.95
2. KNN - 0.94
3. SVC - 0.95
4. DecisionTree Classifier -0.94
5. Random Forest Classifier - 0.95 
6. Catboost Classifier - 0.96
7. XGBoost Classifier - 0.95
8. LGBM Classifier - 0.95
9. Gradient Boosting Classifier -0.95 
9. Keras Sequential Model - 0.98
## Conclusion
Successfully able to develop a Machine Learning Model that can Analyse or Predict Lung Cancer.
Keras Sequential Model is most useful at 98%, with Catboost coming in at close second (96%). SMOTE is needed to balance classes. The sequential model is effective for lung cancer detection because it enables the construction of a step-by-step neural network, allowing the model to learn hierarchical representations. This is crucial for capturing intricate patterns in medical data. Additionally, CatBoost, a gradient boosting algorithm, complements the sequential model by enhancing its predictive power. CatBoost handles categorical features adeptly, vital in medical datasets, and mitigates overfitting. The combination of a sequential model and CatBoost leverages their respective strengths, resulting in a robust and accurate system for lung cancer detection.

## Aindree Chatterjee

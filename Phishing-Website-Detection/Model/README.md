**PROJECT TITLE**: Phishing Website Detection

**GOAL**: To determine if a website is safe/dangerous using optimized features extracted from the website.

**DATASET**: [Phishing Website Dataset - Kaggle](https://www.kaggle.com/datasets/akashkr/phishing-website-dataset)

**DESCRIPTION**:

We have 30 optimized features extracted from a website, e.g. URL length, SSL final state, Port, Redirect, etc.  
The features are all categorical, most of which are binary. The target variable is also binary, safe (1) vs dangerous (-1).  
Our objective is to train a deep learning model to learn a representation which can accurately classify future websites as 
safe or dangerous based on the features extracted from them.

**TASKS PERFORMED**:

1. Data cleaning by fixing column names and encoding target variable. Feature selection using Correlation matrices,
Chi-squared test of independence and Mutual Information score. Used information from the analysis to create two reduced 
datasets with 23 and 9 features i.e. 77% and 30% of the original data respectively.

2. Used simple ML models to create a framework for model evaluation and setting a baseline accuracy. Improved understanding 
of which factors are affecting model performance.

3. Focused on neural networks to beat the baseline score. A deep neural network was able to do so by a significant margin
even without tuning. Used a grid search method to tune the deep neural network and improve the accuracy further.

**MODELS USED**:

1. Logistic Regression and Principal Component Analysis + Logistic Regression for a linear baseline.
2. Random Forest for a non-linear baseline.
3. Multi-layer Perceptron (fully-connected feed-forward neural network) with shallow as well as deep
configuration to beat the baselines.
4. Halving Grid-search for hyperparameter tuning of the neural networks
(All scikit-learn implementations)

**LIBRARIES NEEDED**:

1. Numpy
2. Pandas
3. Matplotlib
4. Scikit-learn

**VISUALIZATION**

1. [Feature selection](https://github.com/stiwari-ds/DL-Simplified-SWOC-S3/tree/phishing-website-detection/Phishing-Website-Detection/Images/00-eda_and_preprocessing) ([Notebook 00](https://github.com/stiwari-ds/DL-Simplified-SWOC-S3/tree/phishing-website-detection/Phishing-Website-Detection/Model/00_eda_and_preprocessing.ipynb))
2. [Baseline results](https://github.com/stiwari-ds/DL-Simplified-SWOC-S3/tree/phishing-website-detection/Phishing-Website-Detection/Images/01-ml_baseline) ([Notebook 01](https://github.com/stiwari-ds/DL-Simplified-SWOC-S3/tree/phishing-website-detection/Phishing-Website-Detection/Model/01_ml_baseline.ipynb))
3. [Deep neural network results](https://github.com/stiwari-ds/DL-Simplified-SWOC-S3/tree/phishing-website-detection/Phishing-Website-Detection/Images/02-sklearn_mlp) ([Notebook 02](https://github.com/stiwari-ds/DL-Simplified-SWOC-S3/tree/phishing-website-detection/Phishing-Website-Detection/Model/02_sklearn_mlp.ipynb)) 

**ACCURACIES**: (%)

| **Feature set ->**            | **Top (9 features)** | **Reduced (23 features)** | **All (30 features)** |
|:-----------------------------:|:--------------------:|:-------------------------:|:---------------------:|
| **Models**                    |                      |                           |                       |
| **Logistic Regression**       | 92.05                | 92.51                     | 92.81                 |
| **PCA + Logistic Regression** | 92.12                | 92.38                     | 92.45                 |
| **Random Forest**             | 93.63                | 93.85                     | 93.84                 |
| **Shallow MLP (basic)**       | 93.28                | 94.87                     | 95.59                 |
| **Deep MLP (basic)**          | 93.82                | 95.57                     | 96.22                 |
| **Deep MLP (tuned)**          | -                    | -                         | **96.73**                 |


**CONCLUSION**:

We used extracted and optimized features to detect cases of phishing websites. While simple ML models were able to classify  
with an accuracy upto 93.8%, training and tuning deep neural networks had even better performance. The best model was a deep  
multi-layer perceptron tuned using halving grid-search, with final metrics: **Accuracy = 96.73% and ROC-AUC = 0.9956**.

**AUTHOR**:
Siddhant Tiwari  
([Github](https://www.github.com/stiwari-ds) - [Kaggle](https://www.kaggle.com/stiwarids) - [LinkedIn](https://www.linkedin.com/in/stiwari-ds/))

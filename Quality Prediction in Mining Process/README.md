# Quality Prediction in Mining Process

(dataset image)

# Introduction

Here we create a model which will predict the purity of an ore using the various lab result values, done on a sample of that ore..

# Dataset

The dataset used in this project is take from the Kaggle website.
<br>
<b>Dataset Link:- https://www.kaggle.com/datasets/edumagalhaes/quality-prediction-in-a-mining-process </b>
<br>
In this dataset there is a table which contains 24 columns and around 735000 rows.
<br>
<b>Some of the columns are:</b>% Iron Feed, % Silica Feed, Starch Flow, Ore Pulp Flow, Floatation columns and so on.

# Aim

The main aim is to build a model using various approaches that will be able to predict an ore's purity and impurity using the different column values as input.

# Approach

We will try to build the models using different algorithms of ML and DL and compare their accuracy. In this notebook we will be building models using Linear Regression, Decision Trees, Random Forest and Artificial Neural Networks.

## Exploratory Data Analysis
(image - 2)
(image - 3)


## 1. Linear Regression

Linear regression analysis is used to predict the value of a variable based on the value of another variable. The variable you want to predict is called the dependent variable. The variable you are using to predict the other variable's value is called the independent variable.

## 2. Decision Tree 

Decision trees are a type of model used for both classification and regression. Trees answer sequential questions which send us down a certain route of the tree given the answer. The model behaves with “if this than that” conditions ultimately yielding a specific result.

## 3. Random Forest

A random forest is simply a collection of decision trees whose results are aggregated into one final result. Their ability to limit overfitting without substantially increasing error due to bias is why they are such powerful models.

## 4. Artificial Neural Network

Artificial neural networks, usually simply called neural networks or neural nets, are computing systems inspired by the biological neural networks that constitute animal brains. An ANN is based on a collection of connected units or nodes called artificial neurons, which loosely model the neurons in a biological brain.

## Observation

We have observed that:<br>
<i>Test Accuracy for Linear Regression model = <b>0.67646</b> <br>
Test Accuracy for Decision Tree model = <b>0.99407</b> <br>
Test Accuracy for Random Forest model = <b>0.88713</b> <br>
Test Accuracy for ANN model = <b>0.0037</b> <br>

### Key Notes:

<b>Loss can be seen as a distance between the true values of the problem and the values predicted by the model. Greater the loss is, more huge is the errors you made on the data.

<b>Accuracy can be seen as the number of error you made on the data.

That means:<br>
a low accuracy and huge loss means you made huge errors on a lot of data<br>
a low accuracy but low loss means you made little errors on a lot of data<br>
a great accuracy with low loss means you made low errors on a few data (best case)<br>
a great accuracy but a huge loss, means you made huge errors on a few data.

# Conclusion

We have solved the problem using four different approaches. The differences in the accuracies may be because of the model's architecture, optimizers used, loss functions used and so on. You can try changing these and observe how the model performs on your system.
<br>
The Decision Tree model seemed to have the highest accuracy in our case but Decision Tree's are also prone to Overfitting.

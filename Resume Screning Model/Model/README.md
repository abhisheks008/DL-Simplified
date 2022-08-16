# RESUME SCREENING AND CLASSIFICATION MODEL

**AIM**

Develop a model for predicting the class/category of role based on the person's resume.

**DATASET**

https://www.kaggle.com/datasets/dhainjeamita/updatedresumedataset?resource=download

**CONTENT**

Data for the case is available in CSV format having 963 rows and 2 columns.

**STEPS TAKEN**

All the required libraries and packages were imported and then the required dataset for the project was loaded.EDA was carried out to visualize various parameters and the most corelated unigrams and bigrams. Data was cleaned also known as Text Preprocessing. Text Preprocessing was done using the re function of python and the nltk library which is used for NLP based models. Model building was then implemented using different algorithms. 9 different models were used to train and valuate the results. 5 of the used models gave a very high accuracy whereas Dummy Classifier gave the least accuracy of less than 0.1.

**MODELS USED**

The classification models used are:

1. K Nearest Neighbor
2. Dummy Classifier
3. Linear Support Vector Classifier
4. Stochastic Gradient Descent
5. Random Forest
6. Decision Tree
7. Multinomial Naive Bayes Classifier
8. Gradient Boost
9. AdaBoost

**LIBRARIES NEEDED**

* Pandas - for data analysis
* Numpy - for data analysis
* matplotlib - for data visualization
* seaborn - for data visualization
* scikit-learn - for data analysis

**VISUALIZATION**

### Dataset Head snapshot
![data sample](https://user-images.githubusercontent.com/86421205/184983563-e11e69ab-266b-45ca-949c-68992b0a8dd5.png)

### Accuracy Comparison of Different models
![acuracy_comp(two)](https://user-images.githubusercontent.com/86421205/184983218-d01dba0d-98c0-4679-b08f-f2d65759df63.png)

### Confusion matrix for Stochastic Gradient Descent Algorithm
![confusion_matrix_SGD](https://user-images.githubusercontent.com/86421205/184983825-5244289e-1583-4ac6-908d-fe0eb37bd7c9.png)

By viewing Confusion Matrix it is easily deduced that RFC model is the best model for this project.


**ACCURACIES**

| Model         | Architecture                      | Accuracy in % (on testing data) |
| ------------- |:---------------------------------:|:-------------:|
| Model 1       | K Nearest Neighbor Model          |97.92          |
| Model 2       | Dummy Classifier Model            |9.84           |
| Model 3       | Linear Support Vector Model       |100.00         |
| Model 4       | Stochastic Gradient Descent Model |100.00         |
| Model 5       | Random Forest Classifier Model    |100.00         |
| Model 6       | Decision Tree Classifier Model    |100.00         |
| Model 7       | Multinomial Naive Bayes Model     |96.37          |
| Model 8       | Gradient Boost Classifier Model   |100.00         |
| Model 9       | AdaBoost Model                    |30.05          |

**CONCLUSION**

The mostsuccesful model was found to be Stochastic Gradient Descent Classifier for Role classification basedon their resume.

# Prajwal Uday

Connect with me on Linkedin: https://www.linkedin.com/in/prajwal-uday-1b9678229/

Check out my Github profile: https://github.com/prajwal-144

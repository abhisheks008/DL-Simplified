# RESUME SCREENING AND CLASSIFICATION MODEL

**GOAL**

Develop a model classify resumes into predefined categories.
Note: Text classification is an example of supervised machine learning since we train the model with labelled data.

**DATASET**

https://www.kaggle.com/datasets/dhainjeamita/updatedresumedataset?resource=download

**CONTENT**

Data for the case is available in CSV format having 963 rows and 2 columns.

**STEPS TAKEN**

All the required libraries and packages were imported and then the required dataset for the project was loaded. 

*EDA* was carried out to visualize various parameters and the most corelated unigrams and bigrams. 

Data was cleaned also known as *Text Preprocessing*. Text Preprocessing was done using the re function of python and the nltk library which is used for NLP based models. 

Model building was then implemented using different algorithms. 9 different models were used to train and valuate the results. 5 of the used models gave a very high accuracy whereas Dummy Classifier gave the least accuracy of less than 0.1.

![category_distribution](https://user-images.githubusercontent.com/86421205/184989201-89102de2-33d1-4472-85d1-8245280952ef.png)

**TEXT PREPROCESSING**

The text needs to be transformed to vectors so as the algorithms will be able make predictions. In this case, the **Term Frequency – Inverse Document Frequency (TFIDF)** weight will be used to evaluate how important a word is to a document in a collection of documents.

After removing punctuation and lower casing the words, importance of a word is determined in terms of its frequency.

TF-IDF is a measure of originality of a word.

**TF** is the number of times a term appears in a particular document.

**IDF** is a measure of how common or rare a term is across the entire corpus of documents.

![res](https://user-images.githubusercontent.com/86421205/184990238-7664e734-0e60-46a7-a778-f3fd79ebc2d5.png)

**MODELS USED**

The classification models used are:

1. *K Nearest Neighbor*
2. *Dummy Classifier*
3. *Linear Support Vector Classifier*
4. *Stochastic Gradient Descent*
5. *Random Forest*
6. *Decision Tree*
7. *Multinomial Naive Bayes Classifier*
8. *Gradient Boost*
9. *AdaBoost*

**LIBRARIES REQUIRED**

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

### Evaluating SGD on different classes
![sgd](https://user-images.githubusercontent.com/86421205/184990143-e525fd7f-530c-4629-9f49-e5cb70668e17.png)

### Confusion matrix for Stochastic Gradient Descent Algorithm
![confusion_matrix_SGD](https://user-images.githubusercontent.com/86421205/184983825-5244289e-1583-4ac6-908d-fe0eb37bd7c9.png)

By viewing Confusion Matrix it is easily deduced that SGD model is the best model for this project.


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

The most succesful model was found to be Stochastic Gradient Descent Classifier for Role classification based on their resume.

# Prajwal Uday

Connect with me on Linkedin: https://www.linkedin.com/in/prajwal-uday-1b9678229/

Check out my Github profile: https://github.com/prajwal-144

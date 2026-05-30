## Dataset

The dataset used in this project includes customer information from a bank and is meant for predicting customer churn. The goal is to find out if a customer is likely to leave the bank based on their demographic, financial, and account-related details.

### Dataset Features

| Feature         | Description                                                    |
| --------------- | -------------------------------------------------------------- |
| CreditScore     | The credit score of the customer                              |
| Geography       | The customer's geographical region                             |
| Gender          | The gender of the customer                                    |
| Age             | The age of the customer                                       |
| Tenure          | The number of years the customer has been with the bank      |
| Balance         | The current account balance                                    |
| NumOfProducts   | The number of banking products the customer uses              |
| HasCrCard       | Whether the customer has a credit card                        |
| IsActiveMember  | Whether the customer is an active member                     |
| EstimatedSalary | The customer's estimated annual salary                        |

### Target Variable

| Variable | Description                                                    |
| -------- | -------------------------------------------------------------- |
| Exited   | Shows whether the customer left the bank (1 = Yes, 0 = No)   |

### Data Characteristics

* The dataset has both numerical and categorical features.
* It includes customer demographics, financial status, and engagement metrics.
* The target variable is binary, resulting in a supervised binary classification problem.
* Some classes may be unbalanced, so careful evaluation is needed using metrics like Precision, Recall, F1-Score, and ROC-AUC.

### Feature Engineering

To capture more customer behavior patterns, the following derived features were created:

* **Balance-Salary Ratio**: The relationship between account balance and estimated salary.
* **Products Per Year**: The number of products adjusted by customer tenure.
* **Active Balance**: A combination of customer activity status and account balance.

These new features help the models find more meaningful relationships in the data and improve churn prediction accuracy.

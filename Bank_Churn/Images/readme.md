Exploratory data analysis

The data comprises 10000 bank customers of which roughly 20 percent are no longer customers with the remaining 80 percent still active customers of the bank. Hence it's a moderately imbalanced classification problem. From the geographical analysis it is observed that German customers leave the bank far more than French and Spanish customers. Females seem to be more likely to leave the bank than males. Age and account balance were observed to have a positive correlation and are highly related to customer churn, unlike active customers where active members leave less often than inactive ones. From the feature distribution we again see that churned customers are generally older with higher balance than those active ones, however the estimated salary of the customers does not seem to affect the churn.

Model performance

Out of the four models used for prediction namely ANN, TabNet, FT-Transformer and Autoencoder+Classifier, FT-Transformer is the best as it has a ROC-AUC value of 0.8519. However, in terms of accuracy TabNet is the best with 82.1%, ANN is also performing well. Autoencoder based model is performing relatively worse than the rest. ROC curves and Confusion Matrices reflect a better balance between correct prediction of churned customers and error in predicting non churned as churned for FT-Transformer and ANN.

Feature importance

SHAP values determined that The Number of Products, Customer Age, Active Members status, Geography and account balance were the most influential features for predicting whether or not a customer will leave the bank.

Conclusion

From the above we see that the features determining churn behavior are the account balance of the customers, number of products they use and their activity in the bank, geography of the customers and their age. Among the models used FT-Transformer gave the best overall results.
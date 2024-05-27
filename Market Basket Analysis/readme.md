### Market Basket Analysis for Retail Store: A Deep Learning Approach
<hr/>

### GOAL

The main goal of this project is to perform Market Basket Analysis on a given dataset containing transactional data from a retail store. The purpose is to discover item associations and generate insights that can be used to improve cross-selling opportunities, optimize product placements, and enhance overall sales strategies.

### DATASET
The dataset used in this project is available in the file basket_analysis.csv. It contains transactional data with boolean values indicating whether specific products were bought by the customer in each shopping session.

### DESCRIPTION
Market Basket Analysis is a widely used technique in retail and e-commerce industries to gain insights into customer buying patterns and discover potential relationships between products. By analyzing the transaction data, we aim to find frequent itemsets and association rules that can guide the store's sales and marketing strategies.

### WHAT I HAD DONE

Data Preprocessing: Cleaned the transactional data and handled missing values, converting it into a suitable format for analysis.
Transaction Encoding: Transformed the transaction data into a binary format to prepare it for association rule mining.
Association Rule Mining: Employed the Apriori and FP Growth algorithms to mine frequent itemsets and discover association rules.
Rule Evaluation: Evaluated the generated association rules based on support, confidence, and lift to identify significant rules.
Insight Generation: Interpreted the results to identify meaningful item associations and provide actionable insights for the retail store.

### MODELS USED

Apriori Algorithm: Used for frequent itemset mining and rule generation based on transaction data.
FP Growth Algorithm: Employed as an alternative frequent itemset mining technique for comparison.
Neural Collaborative Filtering (NCF) Model: A deep learning-based approach used for personalized product recommendations.

### LIBRARIES NEEDED

pandas
numpy
scikit-learn
mlxtend
matplotlib
TensorFlow
Keras

### VISUALIZATION
<img src = "https://github.com/vaishnavi-3969/DL-Simplified/assets/80088403/37aa53ab-da2a-44cd-835c-0f8035b244a9"/>


### CONCLUSION
The Market Basket Analysis provided valuable insights into customer buying patterns and item associations. Both traditional Apriori and FP Growth algorithms proved effective in mining frequent itemsets and generating association rules. Additionally, the NCF model successfully delivered personalized product recommendations based on user-item interactions. The incorporation of deep learning techniques enhanced the accuracy and personalization of recommendations, allowing the retail store to optimize cross-selling opportunities and improve customer satisfaction.

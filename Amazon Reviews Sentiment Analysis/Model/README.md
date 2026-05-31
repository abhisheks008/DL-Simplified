# Amazon Reviews Sentiment Analysis

### Goal
Analyze the sentiments from the given dataset of Amazon

### Dataset
The dataset is collected from the following link, https://www.kaggle.com/datasets/tarkkaanko/amazon

### Description
One of the most important problems in e-commerce is the correct calculation of the points given to after-sales products. The solution to this problem
is to provide greater customer satisfaction for the e-commerce site, product prominence for sellers, and a seamless shopping experience for buyers.
Another problem is the correct ordering of the comments given to the products. The prominence of misleading comments will cause both financial losses
and customer losses. In solving these 2 basic problems, e-commerce site and sellers will increase their sales, while customers will complete their
purchasing journey without any problems.

This dataset consists of ranking product ratings and reviews on Amazon.


### What I have done
1. Imported the required libraries
2. Imported the dataset
3. Cleaned the data from null values
4. Categorical variable analysis
5. Splitting ratings from 1-5 into positive, neutral, and negative
6. Processing the the review text and transform it into format usable by Machine learning models
7. Converting a collection of raw documents to a matrix of TF-IDF (Term Frequency Inverse Documnet Frequency) features.
8. Getting accuracy score of Naive Bayes Model



### Libraries used
1. `ntlk`
2. `sklearn`
3. `textblob`
4. `wordcloud`
5. `plotly`
6. `numpy`
7. `pandas`
8. `matplotlib`


# Models Used #
1. Naive Bayes Model

### Visualization ###

### Categorical variable summary ###
![image](https://github.com/SHAY2407/DL-Simplified/blob/main/Amazon%20Reviews%20Sentiment%20Analysis/Images/newplot.png)

### Result ###
![image](https://github.com/SHAY2407/DL-Simplified/blob/main/Amazon%20Reviews%20Sentiment%20Analysis/Images/result.png)

### Accuracy ###

| Sentiment                                   | Overall       |
|:-------------------------------------------:|:-------------:|
| Negative                                    |3.968051       |
| Positive                                    |4.737439       |
| Neutral                                     |4.687500       |

### Conclusion ###
Successfully able to develop a Deep Learning Model that can analyze the sentiments from the given data of Amazon reviews

**Yashwardhan Khanna**

Connect with me on Linkedin: https://www.linkedin.com/in/yashwardhan-khanna-7596871a5/
Check out my Github profile: https://github.com/SHAY2407

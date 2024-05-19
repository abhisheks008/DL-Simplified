## **PROJECT TITLE**

### 🎯 **Goal**
To predict the number of covid cases for every month.

### 🧵 **Dataset**
https://www.kaggle.com/datasets/imdevskp/corona-virus-report/data

### 🧾 **Description**
The project focuses on exploring the data on the COVID-19 pandemic and forecast the number of confirmed cases in steps of 30 days(1 month).

### 🧮 **What I had done!**

- Load the dataset
- Initial inspection of data
- Preprocessing
- Exploratory Data Analysis
- Model training and evaluation

### 🚀 **Models Implemented**

Since this is a time series dataset, I have chosen to proceed with time series models like ARIMA, SARIMAX, LSTM, BiLSTM.

### 📚 **Libraries Needed**
- numpy
- pandas
- matplotlib
- seaborn
- plotly
- sklearn
- statsmodels
- tensorflow
- keras


### 📊 **Exploratory Data Analysis Results**
1. Which country has the highest number of confirmed, active, recovered cases and deaths?
![](images/EDA1.png)
![](images/EDA2.png)
![](images/EDA3.png)
![](images/EDA4.png)

2. How rapidly is the virus spreading?
![](images/EDA5.png)

3. Analysis of US
![](images/EDA6.png)

4. Spread of the virus globally
![](images/newplot.png)



### 📈 **Performance of the Models based on the Accuracy Scores**

![](images/ARIMA.png)
![](images/SARIMAX.png)
![](images/LSTM.png)


|                    |   MAPE    |
|--------------------|---------------|
|      ARIMA        |     14%       |  
|     SARIMAX       |     11%       |
|    LSTM    |     57%       |
|    BiLSTM    |     58%       |   


### 📢 **Conclusion**
BiLSTM model performs better comparative to other models used on the above dataset.



### ✒️ Abirami Gurushanker

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/A-b-i-r-a-m-i-G-S)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abirami-gurushanker-b549a725a)


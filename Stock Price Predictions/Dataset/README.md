## Dataset link: https://finance.yahoo.com/quote/TTM/history?p=TTM
<i> This dataset contains all the previous record of stock price of Tata Motors Company. </i>
## To use the dataset in the code you can use this command
<code> 
import yfinance as yf
import datetime as dt
df = yf.download('TTM', dt.datetime(2012,1,1) , dt.datetime(2023,1,7)) </code>



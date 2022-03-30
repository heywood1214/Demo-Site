#Description: this is a stock market dashboard to show charts and data

#import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from pandas_datareader import data as web
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


today = datetime.today().strftime('%Y-%m-%d')
stockStartDate ='2013-01-01'

st.header('Welcome to my project on analyzing ETFs and visualizing your stock portfolio')
st.subheader('Creator: Heywood Lau')


image = Image.open("Linkedln Profile.jfif")
st.image(image,use_column_width=150)

#Create a sidebar header
st.sidebar.header('User Input')

#Create a function to get users input
def get_input():
    start_date = st.sidebar.text_input("Start Date","2013-01-01")
    end_date = st.sidebar.text_input("End Date","2020-01-01")    
    stock_symbol = st.sidebar.text_input("Stock Symbol","TSLA")
    second_ETF = st.sidebar.text_input("ETF comparison","XEI.TO")
    return start_date,end_date, stock_symbol,second_ETF

#Create a function to get the proper company data and the proper timeframe from the user start date to the users end date
def get_data(symbol,start_time, end_time):

    #Get date range
    start_time = pd.to_datetime(start_time)
    end_time = pd.to_datetime(end_time)

    #Load the data
    df=web.DataReader(symbol.upper(),'yahoo',start=start_time, end=end_time)
    
    #set the start end index rows both to 0
    start_row = 0
    end_row = 0
    df.reset_index(inplace=True,drop=False)


#set the date from the top of the data 
    for i in range(0, len(df)):
        if start_time <= pd.to_datetime(df['Date'][i]):
            start_row = i 
            break

    #Start from the bottom of the dataset and go up 
    for j in range(0,len(df)):
        if end_time>= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df)-1-j
            break

#set the index to the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row: end_row+1,:]


#combine 
def combine_ETF_graph(df, df_2):
    data = [df['Adj Close'],df_2['Adj Close']]
    headers=["First ETF","Second ETF"]
    df_3 = pd.concat(data, axis = 1, keys = headers)
    return df_3

# daily simple return
def daily_return(df,df_2):
    data = [df['Adj Close'],df_2['Adj Close']]
    headers=["First ETF","Second ETF"]
    df_3 = pd.concat(data, axis = 1, keys = headers)
    #df_3.reset_index(inplace=True,drop=False)
    df_3.index = df_3.index.strftime('%Y-%m-%d')
    daily_simple_return = df_3[['First ETF','Second ETF']].pct_change(1)

    return daily_simple_return


#Get the users input
start_time,end_time,symbol,second_ETF = get_input()

#Get the data
df= get_data(symbol,start_time,end_time)
df_2 = get_data(second_ETF, start_time,end_time)


st.line_chart(combine_ETF_graph(df,df_2))

st.write(daily_return(df,df_2))

#fig, ax = plt.subplots()
#sns.heatmap(df_col.corr(), ax=ax)
#st.write(fig)

#plt.subplots(figsize=(11,11))
fig, ax = plt.subplots()
sns.heatmap(daily_return(df,df_2).corr(),annot=True,fmt='.2%', ax = ax)
ax.set_title('ETFs HeatMap Correlation')
st.write(fig)


#show the co-variance matrix, can tell how they move together
st.subheader("Covariance Matrix")
st.write((daily_return(df,df_2)).cov())

st.subheader("Volatility")
st.write((daily_return(df,df_2)).var())

#volatility matrix
volatility=np.sqrt((daily_return(df,df_2)))*100
st.write((daily_return(df,df_2)).std()*100)
st.subheader("Volatility by Standard Deviation")
st.write((volatility))

#show the mean or average daily simple return
daily_average_return = (daily_return(df,df_2)).mean()*100
st.write("Daily average return: "+str(round((daily_average_return),2)))

#show the average monthly return 
monthly_average_return = daily_average_return*20
st.header("Monthly Average Return")
st.write(monthly_average_return)

#annualized returns
annualized_returns = (daily_return(df,df_2)).mean()*100*252
st.write(annualized_returns)

#Display the close price
st.header(symbol+" Close Price\n")


#Display the Volume
st.header(symbol+" Volume\n")
st.line_chart(df['Volume'])

#Get statistics on data
st.header('Data Statstics')
st.write(df.describe())

#Thoughts on what else to include
""" 
1. Prediction, ARIMA model, using time series data
2. Exponential Smoothing -> how much it could smooth out
3. Compare dividend ETFs vs S&P 500 
4. What happened when there was a correction
5. Metal Prices when there was a correction


"""

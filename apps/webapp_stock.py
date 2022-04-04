
#import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from pandas_datareader import data as web
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt

def app():
    st.title ("Market and ETF Analysis")

    plt.style.use('fivethirtyeight')


    today = datetime.today().strftime('%Y-%m-%d')
    stockStartDate ='2013-01-01'

    st.header('Welcome to my project on analyzing ETFs and visualizing your stock portfolio')
    st.subheader('Creator: Heywood Lau')


    #image = Image.open("./images/Linkedln Profile.png")
    #st.image(image,use_column_width=150)

    #Create a sidebar header
    st.sidebar.header('User Input')

    #Create a function to get users input
    def get_input():
        start_date = st.sidebar.text_input("Start Date","2013-01-01")
        end_date = st.sidebar.text_input("End Date","2022-03-30")    
        stock_symbol = st.sidebar.text_input("First ETF/Stock","TSLA")
        second_ETF = st.sidebar.text_input("Second ETF/Stock","XEI.TO")
        st.sidebar.text('ETFs listed in TSX needs\n to add ".TO" behind ticker symbol\n (i.e. "VSP.TO")')
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
        headers=[symbol,second_ETF]
        df_3 = pd.concat(data, axis = 1, keys = headers)
        return df_3

    # daily simple return
    def daily_return(df,df_2):
        data = [df['Adj Close'],df_2['Adj Close']]
        headers=[symbol,second_ETF]
        df_3 = pd.concat(data, axis = 1, keys = headers)
        #return df_3
        #df_3.reset_index(inplace=True,drop=False)
        df_3.index = df_3.index.strftime('%Y-%m-%d')

        daily_simple_return = df_3.pct_change(axis="rows", periods=-1)

        return daily_simple_return


    #Get the users input
    start_time,end_time,symbol,second_ETF = get_input()

    #Get the data
    df= get_data(symbol,start_time,end_time)
    df_2 = get_data(second_ETF, start_time,end_time)

    st.subheader("Here is historical adjusted close prices for the two ETFs/Stocks")
    st.line_chart(combine_ETF_graph(df,df_2))

 
    st.subheader("Here is the daily return of the two ETFs/Stocks")
    colT1,colT2 = st.columns([2,8])
    with colT2:
        st.write(daily_return(df,df_2))


    df_3 = daily_return(df,df_2)
    #df_4 = df
    #df_4.reset_index(inplace=True,drop=False)
    #st.write(df_4['Adj Close'])

    #X = np.stack((df['Adj Close'], df_2['Adj Close']),axis=0)
    #st.write(X)


    st.header("")
    fig, ax = plt.subplots()
    sns.heatmap(daily_return(df,df_2).corr(),annot=True,fmt='.2%', ax = ax)
    ax.set_title('ETFs HeatMap Correlation')
    st.write(fig)


    #show the co-variance matrix, can tell how they move together
    st.subheader("Covariance Matrix")
    st.write("measure of the direction of the linear relationship of the two ETFs,however, there is no indication of strength")
    cov_matrix = df_3.cov()
    st.write(cov_matrix.iloc[0,0])

    st.subheader("Volatility")
    st.write("Volatility is calculated based on the standard deviation/variance around the mean price. This provides investor an idea of how far the price might deviate from its average")

    #volatility matrix
    st.write("The below volatility is computed using daily % price change difference. Therefore, you could expect x% of variation per day using the date range you inputted")
    st.write((daily_return(df,df_2)).std()*100)
    
    volatility=np.sqrt(((daily_return(df,df_2))**2))*100
    st.subheader("Volatility by Standard Deviation")
    st.write((volatility))

    #show the mean or average daily simple return
    daily_average_return = (daily_return(df,df_2)).mean()*100

    #st.write(daily_average_return[daily_average_return.index.duplicated()])
    #st.write(type(daily_return(df,df_2)))



    st.subheader("Average " + symbol + " Daily % Change from start date to end date")
    st.write(((df['Adj Close'].iloc[-1])-(df['Adj Close'].iloc[0])/(df['Adj Close'].iloc[0]))/len((df['Adj Close'])) )

    first_ETF_daily_change = ((df['Adj Close'].iloc[-1])-(df['Adj Close'].iloc[0])/(df['Adj Close'].iloc[0]))/len((df['Adj Close'])) 

    st.subheader("Average " + second_ETF + " Daily % Change from start date to end date")
    st.write(((df_2['Adj Close'].iloc[-1])-(df_2['Adj Close'].iloc[0])/(df_2['Adj Close'].iloc[0]))/len((df_2['Adj Close'])))
    second_ETF_daily_change = ((df_2['Adj Close'].iloc[-1])-(df_2['Adj Close'].iloc[0])/(df_2['Adj Close'].iloc[0]))/len((df_2['Adj Close']))




    st.write("Daily average return is "+ ((((daily_average_return).round(2)).apply(str))) + "%")

    #show the average monthly return 
    first_ETF_monthly_average_return = first_ETF_daily_change*22
    second_ETF_monthly_average_return = second_ETF_daily_change*22
    st.header("Monthly Average Return")
    st.subheader(symbol)
    st.write(first_ETF_monthly_average_return)
    st.subheader(second_ETF)
    st.write(second_ETF_monthly_average_return)



    monthly_returns = [first_ETF_monthly_average_return,second_ETF_monthly_average_return]
    #st.write(pd.DataFrame(monthly_returns))

    #annualized returns
    st.header("Annuallaized Returns")
    first_ETF_annualized_returns = first_ETF_daily_change*252
    second_ETF_annualized_returns = second_ETF_daily_change*252
    st.subheader(symbol)
    st.write(first_ETF_annualized_returns)
    st.subheader(second_ETF)
    st.write(second_ETF_annualized_returns)
    #st.write( "The annualized returns of " + symbol + "is" + first_ETF_annualized_returns)
    #st.write( "The annualized returns of " + second_ETF + "is"  + second_ETF_annualized_returns)



    #Display the close price
    st.header(symbol+" Close Price\n")


    #Display the Volume
    st.header(symbol + " &" + second_ETF +" Volume\n")

    data = [df['Volume'],df_2['Volume']]
    headers=[symbol,second_ETF]
    df_3 = pd.concat(data, axis = 1, keys = headers)
    st.line_chart(df_3)


    #Get statistics on data
    st.header('Data Statstics for ' + symbol)
    st.write(df.describe())

    st.header("Data Statistics for " + second_ETF)
    st.write(df_2.describe())

    #Thoughts on what else to include
    """ 
    1. Prediction, ARIMA model, using time series data
    2. Exponential Smoothing -> how much it could smooth out
    3. Compare dividend ETFs vs S&P 500 
    4. What happened when there was a correction
    5. Metal Prices when there was a correction
    """

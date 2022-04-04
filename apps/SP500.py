#Predict future price of any ETF/stock

#from statistics import linear_regression


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as web
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from datetime import datetime
import plotly.express as px


plt.style.use('fivethirtyeight')

def app():
    st.title ("Retirement Forecast based on Dividends/Capital Gain")

    plt.style.use('fivethirtyeight')



    st.sidebar.header("Stock/ETF for prediction")
    st.title ("S&P 500/ETFs Linear Regression Prediction ")



    today = datetime.today().strftime('%Y-%m-%d')
    stockStartDate ='2013-01-01'

    st.header('Welcome to using simple regression for preciting Stock Prices')
    st.subheader('Creator: Heywood Lau')


    #image = Image.open("./images/Linkedln Profile.png")
    #st.image(image,use_column_width=150)

    #Create a sidebar header
    st.sidebar.header('User Input')

    #Create a function to get users input
    def get_input():
        start_date = st.sidebar.text_input("Start Date","2013-01-01")
        end_date = st.sidebar.text_input("End Date","2022-03-30")    
        stock_symbol = st.sidebar.text_input("First ETF/Stock","VSP.TO")
        st.sidebar.text('ETFs listed in TSX needs\n to add ".TO" behind ticker symbol\n (i.e. "VSP.TO")')
        return start_date,end_date, stock_symbol

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

        df.index = df.index.strftime('%Y-%m-%d')
        df = df.iloc[:,1:]


        return df.iloc[start_row: end_row+1,:]


    #Get the users input
    start_time,end_time,symbol= get_input()

    #Get the data
    df= get_data(symbol,start_time,end_time)

    #Clean Data
    st.write(df)

    #Create numbers column 

    df_copy = df.copy()
    df_copy ['Numbers'] = list(range(0,len(df)))

    X = np.array(df_copy[['Numbers']])
    y = df['Close'].values

    #Create and train the model
    simple_regression = LinearRegression().fit(X,y)

    st.write("Intercept:", simple_regression.intercept_)
    st.write("Slope", simple_regression.coef_)

    #Visualization
    #straight line equation


    predicted_y = simple_regression.coef_ * X + simple_regression.intercept_

    def combine_predict_actual(df_copy,df):
        data = [df_copy['Predicted'],df['Close']]
        #headers=['Predicted','Actual']
        df_3 = pd.concat(data, axis = 1)
        return df_3

    #new column to store prediction
    df_copy['Predicted'] = predicted_y
    st.write(df_copy['Predicted'])


    st.write(combine_predict_actual(df_copy,df))


    prediction_dataframe = combine_predict_actual(df_copy,df)




    #st.write(cross_tab)

    fig = px.line(prediction_dataframe)

    st.write(fig)




    #Goodness of fit
    st.subheader("R-squared - how much variation the model is being able to capture/goodness of fit")
    st.write(r2_score(df_copy['Close'],df_copy['Predicted']))

    #Predicted Price the day of the end day
    st.subheader("Next day after End Date Price of your selected ETFs using linear regression")
    st.write(simple_regression.coef_ * len(df_copy)+1 +simple_regression.intercept_)


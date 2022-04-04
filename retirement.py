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
    st.title ("Retirement Forecast based on Dividends/Capital Gain")

    plt.style.use('fivethirtyeight')


    #saving rate
    saving_rate = st.number_input("What is your saving rate", value = 0.3)

    #income
    annual_income = st.number_input("What is your annual after tax income", value = 39500)

    #Monthly Income
    st.subheader("Monthly After Tax Income: " + annual_income/12)

    #yearly expense
    annual_expense = st.number_input("What is your annual expense", value = 24000)

    #interest rate/dividends
    dividend_rate = st.number_input("What is your interest/dividend rate of your investments?", value = 0.02)

    #amount you could invest into the portfolio or assets
    annual_investment_amount = annual_income - annual_expense

    #calculate expected annual return

    annual_return = int(round((annual_investment_amount * dividend_rate)))

    #current year
    current_year = (st.number_input ("What is the current year", value = 2020))

    #withdrawl rate
    withdrawl_rate = st.number_input("What is your desired withdrawl rate" , value = 0.04,min_value = 0.00)

    #video: investment = income-expenses
    total_invested_amount = round(annual_investment_amount,2)

    #Empty list of years
    year_list = []
    annual_income_list = []
    annual_expense_list = []
    annual_investment_amount_list=[]
    total_invested_amount_list = []
    annual_returns_list=[]

    #get the data to the lists
    year_list.append(current_year)
    annual_income_list.append(annual_income)
    annual_expense_list.append(annual_expense)
    annual_investment_amount_list.append(round(annual_investment_amount,2))
    total_invested_amount_list.append(annual_investment_amount)
    annual_returns_list.append(annual_return)


    #a variable to store the maount of years investor desired
    number_of_years_invested = st.number_input("Number of years invested", value = 30)

    for i in range(0, number_of_years_invested -1):
        total_invested_amount = (annual_income - annual_expense) + annual_return + total_invested_amount
        annual_return = total_invested_amount * (dividend_rate)
        year_list.append(current_year+1+i)
        annual_income_list.append(annual_income)
        annual_expense_list.append(annual_expense)
        annual_investment_amount_list.append(annual_investment_amount)
        total_invested_amount_list.append(total_invested_amount)
        annual_returns_list.append(annual_return)

    #create the data set
    df=pd.DataFrame()
    df['Year']= year_list
    df['Annual Income']=annual_income_list
    df['Annual Expenses']=annual_expense_list
    df['Annual Investment Amount']=(annual_investment_amount_list)
    df['Total Invested Amount'] = total_invested_amount_list
    df['Annual Returns'] = annual_returns_list

    annual_withdrawl_amount = np.array(total_invested_amount_list)*withdrawl_rate
    df['Annual Withdrawl Amount']=annual_withdrawl_amount

    st.write(df)


    plt.figure(figsize = (12,4))
    plt.plot(df['Year'],df['Annual Expenses'], label = "Annual Expenses")
    plt.plot(df['Year'],df['Annual Withdrawl Amount'],label = "Annual Withdrawl Amount")
    plt.title("How many years until retirement")
    plt.xlabel("Years")
    plt.ylabel("CAD")
    plt.xticks(df['Year'],rotation = 45)
    plt.legend()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()

    #Index where you could live off your returns
    st.write(df[df['Annual Expenses']<=df['Annual Withdrawl Amount']].head(1))
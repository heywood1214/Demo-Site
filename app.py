import streamlit as st
from multipage import MultiApp
from apps import webapp_stock,home,retirement,SP500,portfolio_opt

app = MultiApp()

st.subheader(""" 
Welcome to the Heywood Lau's portfolio site. 
This multi-page app can be used for personal finance and data analytics purposes. 
""")

#Add application here 
app.add_app("Homepage", home.app)
app.add_app("Retirement Calculation", retirement.app)
app.add_app("Market and ETF Analysis", webapp_stock.app)
app.add_app("Retirement Calculation", retirement.app)
app.add_app("S&P 500/ETFs Linear Regression Prediction",SP500.app)
app.add_app("Portfolio Optimization - Build any portfolio from the Russell 2000 Index",portfolio_opt.app)


app.run()

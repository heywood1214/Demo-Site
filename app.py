import streamlit as st
from multipage import MultiApp
from apps import webapp_stock,home

app = MultiApp()

st.markdown(""" 

#Multi-Page App

This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).


""")

#Add application here 

app.add_app("home", home.app)
app.add_app("Stock", webapp_stock.app)


app.run()
import streamlit as st
from multipage import MultiApp
from apps import webapp_stock,home

app = MultiApp()

st.markdown(""" 

#Welcome to the Heywood Lau's portfolio site. 

This multi-page app can be used for personal finance and data analytics purposes. 


""")

#Add application here 

app.add_app("home", home.app)
app.add_app("Stock", webapp_stock.app)


app.run()

import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

MongoClient(st.secrets["MONGODB_URI"], server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
def ping():
    try:
        client.admin.command('ping')
        "Pinged your deployment. You successfully connected to MongoDB!"
    except Exception as e:
        e

# Initialize CookieController
controller = CookieController()

text = st.text_area("Write your portfolio")
def writetext():
    portfolios.portfolio_submit("egemam", text)
def readtext():
    st.write(portfolios.portfolio_read("egemam"))
# Function to read CSV and check login
st.button("Write", on_click=writetext)
st.button("Read", on_click=readtext)
st.button("Ping", on_click=ping)
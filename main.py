import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

cluster = MongoClient(st.secrets["MONGODB_URI"], server_api=ServerApi('1'))
db = cluster["wojoco"]
collection = db["userlist"]

def insert():
    collection.insert_one({"_id": "egemam", "password": "3131", "token": "ZWdlbWFt.MzEzMQ=="})

# Send a ping to confirm a successful connection
def ping():
    try:
        cluster.admin.command('ping')
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
def find(name):
    st.write(collection.find_one({"_id": name}))
# Function to read CSV and check login
st.button("Write", on_click=writetext)
st.button("Read", on_click=readtext)
st.button("Ping", on_click=ping)
st.button("Insert", on_click=insert)
name = st.text_input("Username (CaSeSeNsItIvE)", placeholder="JohnDoe")
st.button("Find", on_click=find(name))
import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

cluster = MongoClient(st.secrets["MONGODB_URI"], server_api=ServerApi('1'))
db = cluster["wojoco"]
userlist = db["userlist"]

controller = CookieController()

def is_logged_in():
    return userlist.find_one({"token": controller.get('token')})
    
def get_username():
    return userlist.find_one({"token": controller.get('token')})["_id"]

with st.sidebar:
    if is_logged_in():
        name = get_username()
        st.write(f"Welcome {name}!")
        st.button("Logout", on_click=logout)
    else:
        st.write("Please log in.")
# Initialize CookieController
controller = CookieController()
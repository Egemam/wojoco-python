import streamlit as st
from streamlit_cookies_controller import CookieController
import base64
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

cluster = MongoClient(st.secrets["MONGODB_URI"], server_api=ServerApi('1'))
db = cluster["wojoco"]
userlist = db["userlist"]

controller = CookieController()

if controller.get('token'):
    st.switch_page("main.py")

def login(username, password):
    if userlist.find_one({"_id": username}):
        token = base64.b64encode(username.encode("ascii")).decode("ascii")+"."+base64.b64encode(password.encode("ascii")).decode("ascii")
        if userlist.find_one({"_id": username})["token"] == token:
            print("Login successful")
            controller.set('token', token)
            st.switch_page("main.py")
        else:
            st.warning("Your password is incorrect")
    else:
            st.warning("This user does not exist")

username = st.text_input("Username (CaSeSeNsItIvE)", placeholder="JohnDoe")
password = st.text_input("Password", placeholder="*******", type="password")
button = st.button("Login")
if button:
    login(username,password)
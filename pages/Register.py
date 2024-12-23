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

def register(username, password):
    if not userlist.find_one({"_id": username}):
        token = base64.b64encode(username.encode("ascii")).decode("ascii")+"."+base64.b64encode(password.encode("ascii")).decode("ascii")
        userlist.insert_one({"_id": username, "password": password, "token": token})
        controller.set('token', token)
        st.switch_page("main.py")
    else:
        st.warning("This username is already in use")

username = st.text_input("Username (CaSeSeNsItIvE)", placeholder="JohnDoe")
if len(username) < 3:
    st.warning("Username must be at least 3 characters long")
if not username.isalnum():
    st.warning("Username must be alphanumeric")
password = st.text_input("Password", placeholder="*******", type="password")
if len(password) < 8:
    st.warning("Password must be at least 8 characters long")
if " " in password:
    st.warning("Password cannot contain spaces")
if len(username) < 3 and len(password) < 8:
    button = st.button("Join Us!")
    if button:
        register(username,password)
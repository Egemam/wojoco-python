import streamlit as st
from streamlit_cookies_controller import CookieController
import base64
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

cluster = MongoClient(st.secrets["MONGODB_URI"], server_api=ServerApi('1'))
db = cluster["wojoco"]
collection = db["userlist"]

controller = CookieController()

def login(username, password):
    if not collection.find_one({"_id": username}):
        token = base64.b64encode(username.encode("ascii")).decode("ascii")+"."+base64.b64encode(password.encode("ascii")).decode("ascii")
        collection.insert_one({"_id": username, "password": password, "token": token})
        controller.set('token', token)
        st.switch_page("main.py")

username = st.text_input("Username (CaSeSeNsItIvE)", placeholder="JohnDoe")
password = st.text_input("Password", placeholder="*******", type="password")
button = st.button("Join Us!")
if button:
    login(username,password)
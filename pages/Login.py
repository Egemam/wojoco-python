import streamlit as st
from streamlit_cookies_controller import CookieController
import base64
import csv

controller = CookieController()

def login(username, password):
    if collection.find_one({"_id": username}):
        token = base64.b64encode(username.encode("ascii")).decode("ascii")+"."+base64.b64encode(password.encode("ascii")).decode("ascii")
        if collection.find_one({"_id": username})["token"] == token:
            print("Login successful")
            controller.set('token', token)
            st.switch_page("main.py")
        else:
            st.warning("Your password is incorrect")
    else:
            st.warning("This account does not exist")

username = st.text_input("Username (CaSeSeNsItIvE)", placeholder="JohnDoe")
password = st.text_input("Password", placeholder="*******", type="password")
button = st.button("Login")
if button:
    login(username,password)
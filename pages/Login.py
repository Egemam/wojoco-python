import streamlit as st
from streamlit_cookies_controller import CookieController
import base64
import csv

controller = CookieController()

def login(username, password):
    token = base64.b64encode(username.encode("ascii")).decode("ascii")+"."+base64.b64encode(password.encode("ascii")).decode("ascii")
    with open('userlist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if token in [row['token'] for row in reader]:
            print("Login successful")
            controller.set('token', token)
            st.switch_page("main.py")
        else:
            print("Login failed")
    print(controller.get('token'))

username = st.text_input("Username (CaSeSeNsItIvE)", placeholder="JohnDoe")
password = st.text_input("Password", placeholder="*******", type="password")
button = st.button("Login")
if button:
    login(username,password)
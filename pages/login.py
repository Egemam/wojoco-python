import streamlit as st
from streamlit_cookies_controller import CookieController
import base64

controller = CookieController()

st.title("Login")

def login(username, password):
    print("test")
    #print(controller.get('token'))
    #controller.set('token', base64.b64encode(username.encode("ascii"))+base64.b64encode(password.encode("ascii")))
    #print(controller.get('token'))

username = st.text_input("Username", placeholder="JohnDoe")
password = st.text_input("Password", placeholder="*******", type="password")
button = st.button("Login", on_click=login(username,password))
if button:
    print("test")
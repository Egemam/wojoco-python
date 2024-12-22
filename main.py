import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController

# Initialize CookieController
controller = CookieController()

text = st.text_area("Write your portfolio")
def writetext():
    portfolios.portfolio_submit("egemam", text)
def readtext():
    portfolios.portfolio_read("egemam")
# Function to read CSV and check login
st.button("Write", on_click=writetext)
st.button("Read", on_click=readtext)
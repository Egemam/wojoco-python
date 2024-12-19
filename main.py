import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController

from dotenv import load_dotenv

load_dotenv()


print(os.getenv('TOKEN')) #os.getenv('TOKEN') 

controller = CookieController()

#st.button("Login",on_click=st.switch_page("pages/login.py"))
with open('userlist.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    if controller.get('token') in [row['token'] for row in reader]:
        logout_button = st.button("Logout",on_click=controller.delete('token'))

review_button = st.button("review",on_click=reviews.compare_sum("egemam","maya"))

#print(controller.get('token'))
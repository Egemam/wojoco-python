import portfolios
import reviews
import streamlit as st
import csv
#from streamlit_cookies_controller import CookieController

#controller = CookieController()

#st.button("Login",on_click=st.switch_page("pages/login.py"))
'''with open('userlist.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    if controller.get('token') in [row['token'] for row in reader]:
        logout_button = st.button("Logout",on_click=controller.delete('token'))'''
def functionn():
    print("a")
    print(reviews.compare_sum("egemam","maya"))

review_button = st.button("review",on_click=functionn())

#print(controller.get('token'))
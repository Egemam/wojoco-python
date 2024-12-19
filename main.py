import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController

controller = CookieController()

def review_compare():
    print(reviews.compare_sum("egemam","maya"))

#st.button("Login",on_click=st.switch_page("pages/login.py"))
with open('userlist.csv', newline='') as csvfile:
    print("e")
    reader = csv.DictReader(csvfile)
    print("e")
    if controller.get('token') in [row['token'] for row in reader]:
        print("e")
        logout_button = st.button("Logout",on_click=controller.delete('token'))

review_button = st.button("review",on_click=review_compare)

'''if action == "1":
    user = input("Enter your name: ")
    text = input("Enter your portfolio: ")
    portfolios.portfolio_submit(user, text)
elif action == "2":
    user = input("Enter your name: ")
    place = input("Enter the place: ")
    text = input("Enter your review: ")
    reviews.review_submit(user, place, text)
elif action == "3":
    user = input("Enter your name: ")
    place = input("Enter the place: ")    
    print(reviews.compare_sum(user,place))
elif action == "4":
    print("Goodbye!")
else:
    print("Invalid action")'''

#print(controller.get('token'))
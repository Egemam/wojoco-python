import portfolios
import reviews
import streamlit as st
from streamlit_cookies_controller import CookieController

controller = CookieController()

st.title('WoJoCo')

action = input("Choose your action:\n1. Edit portfolio\n2. Leave a review\n3. Compare your portfolio with a company\n4. Exit\n")

if action == "1":
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
    print("Invalid action")

print(controller.get('token'))
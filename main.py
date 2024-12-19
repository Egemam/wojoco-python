import portfolios
import reviews
import streamlit as st
#from streamlit_cookies_controller import CookieController

#controller = CookieController()

#st.button("Login",on_click=st.switch_page("pages/login.py"))
with open('userlist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if token in [row['token'] for row in reader]:
            st.button("Logout",on_click=controller.delete('token'))

review_button = st.button("review")
if review_button:
    print(reviews.compare_sum("egemam","maya"))

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

#print(controller.get('token'))
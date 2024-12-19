import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController

#st.button("Login",on_click=st.switch_page("pages/login.py"))
with open('userlist.csv', newline='') as csvfile:
    controller = CookieController()
    print(controller.get('token'))
    reader = csv.DictReader(csvfile)
    if controller.get('token') in [row['token'] for row in reader]:
        logout_button = st.button("Logout",on_click=controller.delete('token'))
def show_comparison():
    while 1:
        try:
            text = eval(reviews.compare_sum("egemam","maya"))
            result_icon = st.image(f"images/{text[0]}.png")
            break
        except:
            continue
    st.write(
        
    )

review_button = st.button("review",on_click=show_comparison())

print(controller.get('token'))
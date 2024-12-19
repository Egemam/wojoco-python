import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController

controller = CookieController()

#st.button("Login",on_click=st.switch_page("pages/login.py"))
'''with open('userlist.csv', newline='') as csvfile:
    print(controller.get('token'))
    reader = csv.DictReader(csvfile)
    if controller.get('token') in [row['token'] for row in reader]:
        logout_button = st.button("Logout",on_click=controller.set('token',""))'''
st.write("You are logged in as " + controller.get('token'))

def show_comparison():
    while 1:
        with open('userlist.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            "e"
            if controller.get('token') in [row['token'] for row in reader]:
                for row in reader:
                    "e"
                    if controller.get('token') == row['token']:
                        try:
                            text = eval(reviews.compare_sum(row['username'],"maya"))
                            result_icon = st.image(f"images/{text[0]}.png")
                            for positive in text[1]:
                                st.write(
                                    positive
                                )
                            break
                        except:
                            continue

st.button("review",on_click=show_comparison())
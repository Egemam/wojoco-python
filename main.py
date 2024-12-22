import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController

controller = CookieController()

def show_comparison():
    with open('userlist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        """check = (controller.get('token') in [row['token'] for row in reader])
        if not check:
            st.write("Please log in to access this page.")
            return 0"""
        while 1:
            try:
                name = "".join(row['username'] for row in reader)
                st.write(name)
                text = eval(reviews.compare_sum(name,"maya"))
                result_icon = st.image(f"images/{text[0]}.png")
                st.write("Pros:")
                st.write(
                    "\n".join(text[1])
                )
                st.write("Cons:")
                st.write(
                    "\n".join(text[2])
                )
                break
            except: 
                continue

def logout():
    controller.set('token',"")

"""with st.sidebar:
    with open('userlist.csv', newline='') as csvfile:
        print(controller.get('token'))
        reader = csv.DictReader(csvfile)
        if controller.get('token') in [row['token'] for row in reader]:
            name = "".join(row['username'] for row in reader if row['token'] == controller.get('token'))
            st.write(f"Welcome {name}!")
            logout_button = st.button("Logout",on_click=logout)"""

st.button("review",on_click=show_comparison)
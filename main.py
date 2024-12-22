import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController

controller = CookieController()

#st.button("Login",on_click=st.switch_page("pages/login.py"))
with open('userlist.csv', newline='') as csvfile:
    print(controller.get('token'))
    reader = csv.DictReader(csvfile)
    if controller.get('token') in [row['token'] for row in reader]:
        logout_button = st.button("Logout",on_click=controller.set('token',""))

def show_comparison():
    with open('userlist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not (controller.get('token') in [row['token'] for row in reader]):
            st.switch_page("pages\Login.py")
            return 0
        name = "".join(row['username'] for row in reader if row['token'] == controller.get('token'))
        while 1:
            try:
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

st.button("review",on_click=show_comparison)
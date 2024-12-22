import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController

controller = CookieController()

#st.button("Login",on_click=st.switch_page("pages/login.py"))
#with open('userlist.csv', newline='') as csvfile:
#    print(controller.get('token'))
#    reader = csv.DictReader(csvfile)
#    if controller.get('token') in [row['token'] for row in reader]:
#        logout_button = st.button("Logout",on_click=controller.set('token',""))

def show_comparison():
    
    controller.get('token')
    with open('userlist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        st.write(controller.get('token'))
        name = "".join(row['username'] for row in reader if row['token'] == controller.get('token'))
        st.write(name)
        while 1:
            try:
                text = eval(reviews.compare_sum(name,"maya"))
                st.write(text)
                result_icon = st.image(f"images/{text[0]}.png")
                for positive in text[1]:
                    st.write(
                        positive
                    )
                break
            except:
                continue

st.button("review",on_click=show_comparison)
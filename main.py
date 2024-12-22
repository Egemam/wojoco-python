import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController

controller = CookieController()

def load_user_data():
    with open('userlist.csv', newline='') as csvfile:
        return list(csv.DictReader(csvfile))

def show_comparison():
    user_data = load_user_data()
    check = (controller.get('token') in [row['token'] for row in user_data])
    if not check:
        st.write("Please log in to access this page.")
        return 0
    name = next((row['username'] for row in user_data if row['token'] == controller.get('token')), None)
    while 1:
        try:
            print("name=" + name)
            text = eval(reviews.compare_sum(name,"maya"))
            print(text[0] + text[1] + text[2])
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

with st.sidebar:
    print(controller.get('token'))
    user_data = load_user_data()
    if controller.get('token') in [row['token'] for row in user_data]:
        name = "".join(row['username'] for row in user_data if row['token'] == controller.get('token'))
        st.write(f"Welcome {name}!")
        logout_button = st.button("Logout",on_click=logout)

st.button("review",on_click=show_comparison)
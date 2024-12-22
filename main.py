import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController

# Initialize CookieController
controller = CookieController()

# Load CSV data
@st.cache_data
def load_user_data():
    with open('userlist.csv', newline='') as csvfile:
        return list(csv.DictReader(csvfile))

# Validate login
def is_logged_in(token, user_data):
    return any(row['token'] == token for row in user_data)

# Get username
def get_username(token, user_data):
    return next((row['username'] for row in user_data if row['token'] == token), None)

# Logout logic
def logout():
    controller.set('token', "")

# Show comparison
def show_comparison():
    user_data = load_user_data()
    token = controller.get('token')
    if not is_logged_in(token, user_data):
        st.warning("Please log in to access this page.")
        return
    
    name = get_username(token, user_data)
    if not name:
        st.error("Unable to fetch user data.")
        return
    while 1:
        try:
            # Ensure reviews.compare_sum returns structured data
            text = reviews.compare_sum(name, "maya")  # Expect a list [icon, pros, cons]
            if len(text) != 3:
                st.error("Invalid data format from reviews.compare_sum.")
                return

            st.image(f"images/{text[0]}.png")
            st.write("Pros:")
            st.write("\n".join(text[1]))
            st.write("Cons:")
            st.write("\n".join(text[2]))
            break
        except: continue

# Sidebar
with st.sidebar:
    user_data = load_user_data()
    token = controller.get('token')
    if is_logged_in(token, user_data):
        name = get_username(token, user_data)
        st.write(f"Welcome {name}!")
        st.button("Logout", on_click=logout)
    else:
        st.write("Please log in.")

# Main button
st.button("Review", on_click=show_comparison)

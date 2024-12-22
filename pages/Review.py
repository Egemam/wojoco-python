import portfolios
import reviews
import streamlit as st
from streamlit_cookies_controller import CookieController
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

cluster = MongoClient(st.secrets["MONGODB_URI"], server_api=ServerApi('1'))
db = cluster["wojoco"]
userlist = db["userlist"]
businesslist = db["businesses"]

# Initialize CookieController
controller = CookieController()

# Function to read CSV and check login
def is_logged_in():
    return userlist.find_one({"token": controller.get('token')})

# Get the username
def get_username():
    return userlist.find_one({"token": controller.get('token')})["_id"]

# Logout logic
def logout():
    controller.set('token', "")

# Sidebar with user information and logout
with st.sidebar:
    if is_logged_in():
        name = get_username()
        st.write(f"Welcome {name}!")
        st.button("Logout", on_click=logout)
    else:
        st.write("Please log in.")

# Writes portfolio
def write_review(user,place,text):
    if not is_logged_in():
        st.warning("Please log in to access this page.")
        return
    reviews.review_submit(get_username(), place, text)
    st.warning('You have successfuly updated your portfolio', icon="✅")

# Main text area
if not is_logged_in():
        st.warning("Please log in to access this page.")
else:
    option = st.selectbox(
        "What place do you want to leave review on?",
        [col[_id] for col in businesslist.find_many({})]
    )
    if option:
        review = st.text_area("Write your review",value=reviews.review_read(get_username(), option))
        if st.button("Write"):
            write_review(review)

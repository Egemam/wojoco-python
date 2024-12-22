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
def writetext(text):
    if not is_logged_in():
        st.warning("Please log in to access this page.")
        return
    portfolios.portfolio_submit(userlist.find_one({"token": controller.get('token')})["_id"], text)
    st.warning('You have successfuly updated your portfolio', icon="✅")

# Main text area
if not is_logged_in():
        st.warning("Please log in to access this page.")
else:
    portfolio_text_area = st.text_area("Write your portfolio",value=portfolios.portfolio_read(get_username()))
    # Main button for showing the comparison
    if st.button("Write"):
        writetext(portfolio_text_area)

st.write("\n\n\n\n")

# Show comparison logic
def show_comparison(user,place):
    # Verify user login
    if not is_logged_in():
        st.warning("Please log in to access this page.")
        return
    while 1:  # Infinite loop with try-except
        try:
            text = eval(reviews.compare_sum(name, place))  # Ensure `reviews.compare_sum` returns eval-safe data
            print(str(text[0]) + str(text[1]) + str(text[2]))  # Debug print
            result_icon = st.image(f"images/{str(text[0])}.png")
            st.write("Pros:")
            st.write("\n".join(text[1]))
            st.write("Cons:")
            st.write("\n".join(text[2]))
            break  # Exit loop after successful execution
        except Exception as e:
            print("Error occurred: {e}\n")
            continue  # Retry indefinitely

if not is_logged_in():
        st.warning("Please log in to access this page.")
else:
    option = st.selectbox(
        "What place do you want to leave review on?",
        [col["_id"] for col in businesslist.find({})]
    )
    if option:
        if st.button("Review"):
            show_comparison(get_username(), option)

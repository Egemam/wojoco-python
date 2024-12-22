import portfolios
import reviews
import streamlit as st
import csv
from streamlit_cookies_controller import CookieController

# Initialize CookieController
controller = CookieController()

# Function to read CSV and check login
def is_logged_in():
    with open('userlist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return controller.get('token') in [row['token'] for row in reader]

# Get the username
def get_username():
    with open('userlist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return "".join(row['username'] for row in reader if row['token'] == controller.get('token'))

# Show comparison logic
def show_comparison():
    # Verify user login
    if not is_logged_in():
        st.warning("Please log in to access this page.")
        return
    
    name = get_username()
    while 1:  # Infinite loop with try-except
        try:
            print("name=" + name)
            text = eval(reviews.compare_sum(name, "maya"))  # Ensure `reviews.compare_sum` returns eval-safe data
            print(text[0] + text[1] + text[2])  # Debug print
            result_icon = st.image(f"images/{text[0]}.png")
            st.write("Pros:")
            st.write("\n".join(text[1]))
            st.write("Cons:")
            st.write("\n".join(text[2]))
            break  # Exit loop after successful execution
        except Exception as e:
            print(f"Error occurred: {e}")
            continue  # Retry indefinitely

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

# Main button for showing the comparison
st.button("Review", on_click=show_comparison)

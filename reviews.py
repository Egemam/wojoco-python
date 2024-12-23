import os
from groq import Groq
import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st
import portfolios

cluster = MongoClient(st.secrets["MONGODB_URI"], server_api=ServerApi('1'))
db = cluster["wojoco"]
userlist = db["userlist"]
businesslist = db["businesses"]

client = Groq(
    api_key=st.secrets["GROQ_TOKEN"]
)

def compare_sum(user,place):
    if not portfolios.portfolio_read(user):
        st.warning("You should first write a porfolio")
    else:
        portfolio = portfolios.portfolio_read(user)
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                "content": f"Analyze the following content and decide if the place is matching with the person's portfolio. Adress to the person as you. Give your response with this format:\n[2, 1 or 0 for yes, maybe or no],[reasons for yes with \"\"s seperated by commas],[resons for no with \"\"s seperated by commas]]\nfor example: \n[1, [\"This place is suitable for you because you don't like staying late\", \"This place is suitable for you because you like the breaks\"], [\"This place is not suitable for you because you don't like low wages\", \"This place is not suitable for you because the temperatures are too cold for you\"]]\n\n Try to keep the amount of reasons for yes or no around the 2-5 range. DO NOT ADD ANYTHING ELSE BECAUSE THIS IS THE FORMAT AND GETTING OUT OF THE FORMAT WILL BREAK THE CODE\n\n I am repeating the format once again this is crucial for you to not break:\n[2 1 or 0 for yes maybe or no,[reasons for yes with \"\"s seperated by commas],[resons for no with \"\"s seperated by commas]]\nANOTHER EXAMPLE:\n[1,[\"The place is great for you because you don't like staying late\"], [\"The place is not great for you because you don't like low wages\"]]\n\nPlace: {place}\n\nPortfolio:\n\n{portfolio}\n\n{review_sum(place)}\n\n\n\nDO NOT FORGET NEVER BREAK THE FORMAT IT IS THERE FOR YOU TO OBEY. DO NOT FORGET THE QUOTATION MARKS"
                }
            ],
            model="llama-3.1-8b-instant",  # Use the model within token limits
            stream=False,)
        return(response.choices[0].message.content)  

def review_sum(place):
    text = ""
    print(businesslist.find({"_id": place}))
    text = "\n".join([review for review in businesslist.find({"_id": place})])
    print(text)
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Analyze the following comments and create a list with pros and cons:\n\n{text}"
            }
        ],
        model="llama-3.1-8b-instant",  # Use the model within token limits
        stream=False,)
    return(response.choices[0].message.content)
    


def review_submit(user, place, text):
    if not businesslist.find_one({"_id": place}):
        businesslist.insert_one({"_id": place})
    businesslist.update_one({"_id": place}, {"$set": {user: text}})

def review_read(user,place):
    try:
        return businesslist.find_one({"_id": place})[user]
    except:
        return ""
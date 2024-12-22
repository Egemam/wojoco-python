from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st

cluster = MongoClient(st.secrets["MONGODB_URI"], server_api=ServerApi('1'))
db = cluster["wojoco"]
collection = db["userlist"]

def portfolio_submit(user, text):
    collection.update_one({"_id": user}, {"$set": {"portfolio": text}})

def portfolio_read(user):
    if collection.find_one({"_id": user}):
        return collection.find_one({"_id": user})["portfolio"]
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st

cluster = MongoClient(st.secrets["MONGODB_URI"], server_api=ServerApi('1'))
db = cluster["wojoco"]
collection = db["userlist"]

def portfolio_submit(user, text):
    collection.update_one({"_id": user}, {"$set": {"portfolio": text}})()

def portfolio_read(user):
    path = f'portfolio/{user}.txt'
    with open(path, 'r') as fp:
        return fp.read()
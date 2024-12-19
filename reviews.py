import os
from groq import Groq
import streamlit as st

client = Groq(
    api_key=st.secrets["GROQ_TOKEN"]
)

def compare_sum(user,place):
    path = f'portfolio/{user}.txt'
    print(path)
    if not os.path.exists(path):
        print("This portfolio does not exist in the database")
    elif not os.path.exists(path):
        print("This place does not exist in the database")
    else:
        with open(path, 'r') as fp:
            text = fp.read()
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                "content": f"Analyze the following content and decide if the place is matching with the person's portfolio. Adress to the person as you. Give your response with this format\n[answer,[reasons for yes],[resons for no]: Yes, No or Maybe. a list of reasons for yes and a list of reasons for no. DO NOT GIVE ANY OTHER RESPONSE OTHER THAN MENTIONED THINGS. Try to be optimistic:\n\n{text}\n\n{review_sum(place)}"
                }
            ],
            model="llama-3.1-8b-instant",  # Use the model within token limits
            stream=False,)
        return(response.choices[0].message.content)  

def review_sum(place):
    text = ""
    path = f'reviews/{place}'
    file_list = os.listdir(path)
    for file in file_list:
        with open(f'{path}/{file}', 'r') as fp:
            text += fp.read() + "\n\n"
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
    if not os.path.exists(f'reviews/{place}'):
        os.makedirs(f'reviews/{place}')
    path = f'reviews/{place}/{user}.txt'
    with open(path, 'w') as fp:
        fp.write(text)
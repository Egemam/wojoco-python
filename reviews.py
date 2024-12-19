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
                "content": f"Analyze the following content and decide if the place is matching with the person's portfolio. Adress to the person as you. Give your response with this format:\n[2, 1 or 0 for yes, maybe or no],[reasons for yes with \"\"s seperated by commas],[resons for no with \"\"s seperated by commas]]\nfor example: \n[1, [\"This place is suitable for you because you don't like staying late\", \"This place is suitable for you because you like the breaks\"], [\"This place is not suitable for you because you don't like low wages\", \"This place is not suitable for you because the temperatures are too cold for you\"]]\n\n Try to keep the amount of reasons for yes or no around the 2-5 range. DO NOT ADD ANYTHING ELSE BECAUSE THIS IS THE FORMAT AND GETTING OUT OF THE FORMAT WILL BREAK THE CODE\n\n I am repeating the format once again this is crucial for you to not break:\n[2, 1 or 0 for yes, maybe or no],[reasons for yes with \"\"s seperated by commas],[resons for no with \"\"s seperated by commas]]\n\nPlace: {place}\n\nPortfolio:\n\n{text}\n\n{review_sum(place)}"
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
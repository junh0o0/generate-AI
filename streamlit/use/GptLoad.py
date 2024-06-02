#GPTLoad.py
import os
import streamlit as st
from openai import OpenAI
import sqlite3
import reviews
import UpdatePreference

api_key = st.secrets["api_key"]

def openapi(restaurant, cafe, attraction):
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "전주"+ str(restaurant)+  ", "+str(cafe)+ ", "+ str(attraction)+" 음식점에 대해 1줄로 영어로 알려주세요",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return (chat_completion.choices[0].message.content)

#사용자가 입력한 여행지의 특징의 가중치를 부여
def openapi2(prompt):
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":  str(prompt) + "This is a customer's requirement for the shop. There are 144 different requirements: " +
                            str(reviews.feature_eng_cafe) + ", " + str(reviews.feature_eng_attraction) + "," + str(reviews.feature_eng_restaurant) +
                            "You should pick all related requirements what customer wants. Only write prompt in requirements that I gave to you." 

            }
        ],
        model="gpt-3.5-turbo",
    )
    text = chat_completion.choices[0].message.content
    #text를 확인하고 text에 있는 관광지의 특성에 대해 추가 점수를 부여함.
    UpdatePreference.update_preference(text)
    return (text)

def openapi_restaurant(restaurant):
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "전주"+ str(restaurant) + "에 대해 총 세가지 1. The representative menu, 2. Opening hours, 3. Estimated price range를 영어로 알려줘",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return (chat_completion.choices[0].message.content)

def openapi_attraction(attraction):
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "전주"+ str(attraction) + "에 대해 총 세가지 1. The time required, 2. Admission Fees, 3. Opening hours 을 영어로 알려줘",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return (chat_completion.choices[0].message.content)

def openapi_cafe(cafe):
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "전주"+ str(cafe) + "에 대해 총 세가지 1. 아이스아메리카노 가격, 2. 카페라떼 가격, 3. 오픈시간 을 영어로 알려줘",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return (chat_completion.choices[0].message.content)
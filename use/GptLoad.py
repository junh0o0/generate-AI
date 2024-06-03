#GPTLoad.py
import os
import streamlit as st
from openai import OpenAI
import sqlite3
import reviews
import UpdatePreference
api_key = st.secrets['api_key']

def openapi(restaurant, cafe, attraction):
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "전주"+ str(restaurant)+  ", "+str(cafe)+ ", "+ str(attraction)+"의 이름을 영어로 알려줘. 출력은 'Let Me Introduce 한글이름(영어이름), 한글이름(영어이름),한글이름(영어이름)'로 해줘.",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return (chat_completion.choices[0].message.content)

#사용자가 입력한 여행지의 특징의 가중치를 부여
def openapi2(prompt):
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[                                  #관광지 리뷰데이터에 [사용자로부터 입력받은 요구사항 prompt]가 존재하는지 확인하고 겹치는 내용을 출력해주는 명령입니다.
            {
                "role": "user",
                "content": "Given the feature arrays" + str(reviews.feature_eng_cafe) + ", " + str(reviews.feature_eng_attraction) + "," + str(reviews.feature_eng_restaurant) + "which contain features of tourist attractions, and user requirements about these attractions specified in the next sentence" 
                "User: " + str(prompt) + "The task is to check if the features required by the user exist in these feature arrays. Output all the relevant features directly ONLY FOLLOW THE FORMAT . format: 'I'll recommend attractions highly rated for [print of].'"
            }
        ],
        model="gpt-4o",
    )
    text = chat_completion.choices[0].message.content
    UpdatePreference.update_preference(text)        #SurveyPage에서의 score업데이트는 component의 기여도를 곱해서 이뤄졌지만
    return (text)                                   #UpdatePreference에서는 사용자가 text로 입력한 특징이 관광지에 있는지 확인 후 각 관광지의 해당 특징의 비중을 곱하여 score를 업데이트 함.       




def openapi_restaurant(restaurant):                 #아래의 코드는 관광지의 정보를 출력해주도록 설정한 쿼리문입니다.
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Tell me about Jeonju "+ str(restaurant) + ". 1. The representative menu, 2. Opening hours, 3. Estimated fee in english.",
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
                "content": "Tell me about Jeonju "+ str(attraction) + ". 1. The time required, 2. Admission Fees, 3. Opening hours in english.",
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
                "content": "Tell me about Jeonju "+ str(cafe) + ". 1. The representative menu, 2. Estimated fee, 3. Opening hours in english",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return (chat_completion.choices[0].message.content)
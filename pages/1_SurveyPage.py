import sys
import os
import streamlit as st
import sqlite3
from streamlit_extras.stylable_container import stylable_container 
import numpy as np

path = os.path.dirname('__file__')
use = 'use'
use_path = os.path.join(path,use)
sys.path.append(use_path)

from GptLoad import openapi2
from UpdatePreference import update_preference
st.set_page_config(layout="wide")

st.markdown('<style>' + open('./style/side.css').read() + '</style>', unsafe_allow_html=True)
st.markdown(
    """<style>
    div[class*="stSlider"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 25px;
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown(
    """
    <style>
    textarea {
        font-size: 3rem !important;
    }
    input {
        font-size: 3rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
streamlit_style = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			html, body, [class*="css"]  {
			font-family: 'Roboto', sans-serif;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)
st.markdown("""
<style>
[data-testid="stFormSubmitButton"] {display: none;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.big-font {
    font-size:100px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Follow Me! 👋</p>', unsafe_allow_html=True)
st.markdown("* * *")
st.markdown("""
                ### We will listen to your opinions on cafes, restaurants, and tourist attractions and choose a more suitable place!""")
st.markdown("""<br><br>""", unsafe_allow_html=True)
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: ; #FFFFFF
    }
</style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
    .stForm {
        background-color: #1e83e7;
    }
    </style>
""", unsafe_allow_html=True)
def updateCafeScore(cafeSlider0, cafeSlider1, cafeSlider2, restaurantSlider0, restaurantSlider1,                #설문조사가 완료된 후 slider 값을 이용하여 각 장소마다의 점수를 계산합니다.
                            restaurantSlider2, attractionSlider0, attractionSlider1, attractionSlider2):
    conn = sqlite3.connect('./use/location.db')  
    cursor = conn.cursor()

    # 새로운 설문마다 이전 점수를 삭제하기 위한 코드                                                                
    cursor.execute('DROP TABLE IF EXISTS cafescore')
    cursor.execute('DROP TABLE IF EXISTS restaurantscore')
    cursor.execute('DROP TABLE IF EXISTS attractionscore')

    #테이블 생성
    cursor.execute('''
    CREATE TABLE cafescore (
        name TEXT,
        score REAL DEFAULT 0.0
    )
    ''')
    cursor.execute('''
    CREATE TABLE restaurantscore (
        name TEXT,
        score REAL DEFAULT 0.0
    )
    ''')
    cursor.execute('''
    CREATE TABLE attractionscore (
        name TEXT,
        score REAL DEFAULT 0.0
    )
    ''')

    #각 테이블에 장소 삽입
    cursor.execute('''
    INSERT INTO cafescore (name)
    SELECT DISTINCT name FROM cafe
    ''')
    cursor.execute('''
    INSERT INTO restaurantscore (name)
    SELECT DISTINCT name FROM restaurant
    ''')
    cursor.execute('''
    INSERT INTO attractionscore (name)
    SELECT DISTINCT name FROM attraction
    ''')

    #각 테이블에 점수 반영                                                                                      #각 관광지마다 DB테이블에서 feature, component0~2행은 주성분의 분산값을 저장했습니다.
    cursor.execute('''                                                                                          
    UPDATE cafescore
    SET score = (
        SELECT SUM(
            CASE WHEN cafe.feature = 'Component0' THEN cafe.value * ? 
                 WHEN cafe.feature = 'Component1' THEN cafe.value * ? 
                 WHEN cafe.feature = 'Component2' THEN cafe.value * ? 
            END
        )
        FROM cafe
        WHERE cafe.name = cafescore.name
    )
    ''', (cafeSlider0, cafeSlider1, cafeSlider2))
    cursor.execute('''
    UPDATE restaurantscore
    SET score = (
        SELECT SUM(
            CASE WHEN restaurant.feature = 'Component0' THEN restaurant.value * ? 
                 WHEN restaurant.feature = 'Component1' THEN restaurant.value * ? 
                 WHEN restaurant.feature = 'Component2' THEN restaurant.value * ? 
            END
        )
        FROM restaurant
        WHERE restaurant.name = restaurantscore.name
    )
    ''', (restaurantSlider0, restaurantSlider1, restaurantSlider2))
    cursor.execute('''
    UPDATE attractionscore
    SET score = (
        SELECT SUM(
            CASE WHEN attraction.feature = 'Component0' THEN attraction.value * ? 
                 WHEN attraction.feature = 'Component1' THEN attraction.value * ? 
                 WHEN attraction.feature = 'Component2' THEN attraction.value * ? 
            END
        )
        FROM attraction
        WHERE attraction.name = attractionscore.name
    )
    ''', (attractionSlider0, attractionSlider1, attractionSlider2))

    conn.commit()  
    conn.close()

css="""
<style>
    [data-testid="stForm"] {
        background: #EFFDF4;
    }
3</style>
"""

col1, col2, col3 = st.columns(3)                                                                    
st.write(css, unsafe_allow_html=True)
with col1:
    st.subheader(" Questions about the cafe ☕ ")
    cafeSlider0 = st.slider(
        label="How important is taste COFFEE to you?❓", 
        min_value=1,        
        max_value=100,    
    )
    cafeSlider1 = st.slider(
        label="How important is dessert taste to you❓", 
        min_value=1,        
        max_value=100,            
    )
    cafeSlider2 = st.slider(
        label="How about a UNIQUE cafe❓",
        min_value=1,
        max_value=100,
    )
    st.markdown("""* * *""")

with col2:    
    st.subheader('Questions about the restaurant 🍔')
    restaurantSlider0 = st.slider(
        label="How important is taste to you❓", 
        min_value=1,        
        max_value=100,            
    )
    restaurantSlider1 = st.slider(
        label="Do you like friendly employees❓", 
        min_value=1,        
        max_value=100,            
    )
    restaurantSlider2 = st.slider(
        label="How important is cost-effectiveness to you❓",  
        min_value=1,        
        max_value=100,            
    )
    st.markdown("""* * *""")
with col3: #
    st.subheader('Questions about the attraction 🎡')
    attractionSlider0 = st.slider(
        label="Do you enjoy taking photos❓", 
        min_value=1,        
        max_value=100,            
    )
    attractionSlider1 = st.slider(
        label="Do you want to have a lot of experience❓", 
        min_value=1,        
        max_value=100,            
    )
    attractionSlider2 = st.slider(
        label="Do you like having lots of things to look at❓",  
        min_value=1,        
        max_value=100,            
    )
    st.markdown("""* * *""")
with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                background-color: #EFFDF4;
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
    ):
        st.markdown(
                """
                <style>
                .large-font {
                    font-size: 35px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        st.markdown(
                """
                <h1 class="large-font"></strong>Please let me know what you want the destination to be.<br><strong> 
                ex) It should be cost-effective, I hope it's good for taking pictures</h1>
                """,
                unsafe_allow_html=True
            )
        preference = st.text_input("")
        if preference: #사용자가 버튼을 누르지 않고 UserPage로 넘어가는 경우에 대한 예외처리 부분입니다.
            updateCafeScore(cafeSlider0, cafeSlider1, cafeSlider2, restaurantSlider0, restaurantSlider1, 
                            restaurantSlider2, attractionSlider0, attractionSlider1, attractionSlider2)
            prompt = openapi2(preference)
            st.markdown(f"<div style='font-size:24px;'>{prompt}</div>", unsafe_allow_html=True)


if st.button("Finished? Go to User Page"): #설문조사가 완료된 뒤 버튼을 누르면 UserPage로 이동하고 location.db에 사용자의 설문조사 내용이 저장됩니다.
    updateCafeScore(cafeSlider0, cafeSlider1, cafeSlider2, restaurantSlider0, restaurantSlider1, 
                            restaurantSlider2, attractionSlider0, attractionSlider1, attractionSlider2)
    if preference:
        st.write(openapi2(preference))

        st.markdown(
        """
        <h1 class="large-font"><strong>Please let me know what you want the destination to be.</strong></h1>
        """,
        unsafe_allow_html=True
        )
        st.markdown(
        """
        <h1 class="large-font"><strong>ex) It should be cost-effective, I hope it's good for taking pictures</strong></h1>
        """,
        unsafe_allow_html=True
        )

    st.switch_page('./pages/2_UserPage.py')

  
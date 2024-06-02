import sys
import os
import streamlit as st
import sqlite3
from streamlit_extras.stylable_container import stylable_container 

path = os.path.dirname('__file__')
use = 'use'
use_path = os.path.join(path,use)
sys.path.append(use_path)

from GptLoad import openapi2

st.set_page_config(layout="wide") #streamlit은 가로 레이아웃 제한이 있어서 화면을 넓게 사용하기 위한 코드

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
        font-size: 2rem !important;
    }
    input {
        font-size: 1rem !important;
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
def updateCafeScore(cafeSlider0, cafeSlider1, cafeSlider2, restaurantSlider0, restaurantSlider1, 
                            restaurantSlider2, attractionSlider0, attractionSlider1, attractionSlider2):
    conn = sqlite3.connect('./use/location.db')  # Connect to SQLite Database
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

    #각 테이블에 점수 반영
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
</style>
"""

col1, col2, col3 = st.columns(3) #st.set_page_config(layout="wide")를 사용해서 왼쪽 정렬을 가운데 정렬로 바꿈
st.write(css, unsafe_allow_html=True)
with col1:
    with st.form(key='my_form1'):
        st.subheader(" Questions about the cafe ☕ ")
        cafeSlider0 = st.slider(
            label="Do you value the taste of coffee❓", 
            # label="Do you value the taste of coffee❓&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", 
            min_value=1,        
            max_value=10,            
            value=6               
        )
        cafeSlider1 = st.slider(
            label=" Do you value the taste of dessert❓", 
            min_value=1,        
            max_value=10,            
            value=6                    
        )
        cafeSlider2 = st.slider(
            label="How about a unique cafe❓",  
            min_value=1,        
            max_value=10,            
            value=6                 
        )
        st.markdown("""* * *""")
        submitted = st.form_submit_button("Submit")
        #if submitted:
            #st.write("slider", slider_val, "checkbox", checkbox_val)

with col2:    
    with st.form(key='my_form2'):
        st.subheader('Questions about the restaurant 🍔')
        restaurantSlider0 = st.slider(
            label="Do you think taste is important❓", 
            min_value=1,        
            max_value=10,            
            value=6         
        )
        restaurantSlider1 = st.slider(
            label=" Do you think it's important to be kind❓", 
            min_value=1,        
            max_value=10,            
            value=6               
        )
        restaurantSlider2 = st.slider(
            label="Do you value cost-effectiveness❓",  
            min_value=1,        
            max_value=10,            
            value=6                   
        )
        st.markdown("""* * *""")
        submitted = st.form_submit_button("Submit")
with col3:
    with st.form(key='my_form3'):
        st.subheader('Questions about the attraction 🎡')
        st.markdown("""<br>""",unsafe_allow_html=True)
        attractionSlider0 = st.slider(
            label="Do you do Instagram❓", 
            min_value=1,        
            max_value=10,            
            value=6             
        )
        attractionSlider1 = st.slider(
            label="Do you want to have a lot of experience❓", 
            min_value=1,        
            max_value=10,            
            value=6              
        )
        attractionSlider2 = st.slider(
            label="How about there's a lot to see❓",  
            min_value=1,        
            max_value=10,            
            value=6                
        )
        st.markdown("""* * *""")
        submitted = st.form_submit_button("Submit")
    
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
                    font-size: 24px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        st.markdown(
                """
                <p class="large-font"><strong>Please let me know what you want the destination to be. 
                ex) It should be cost-effective, I hope it's good for taking pictures</strong></p>
                """,
                unsafe_allow_html=True
            )
        preference = st.text_input("")
        if preference:
            updateCafeScore(cafeSlider0, cafeSlider1, cafeSlider2, restaurantSlider0, restaurantSlider1, 
                            restaurantSlider2, attractionSlider0, attractionSlider1, attractionSlider2)
            st.write(openapi2(preference))



if st.button("Go to User Page"):
    updateCafeScore(cafeSlider0, cafeSlider1, cafeSlider2, restaurantSlider0, restaurantSlider1, 
                    restaurantSlider2, attractionSlider0, attractionSlider1, attractionSlider2)
    #st.session_state['page'] = 'chat'
    #st.experimental_rerun()
    st.switch_page('./pages/2_UserPage.py')

  
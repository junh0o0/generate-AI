#user페이지는 설문조사를 마친뒤 접속하게되고 각 관광지마다 세부적인 score를 조절할 수 있습니다.

import sys
import os
import streamlit as st
import sqlite3

st.set_page_config(layout="wide")
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
<style>
[data-testid="stFormSubmitButton"] {display: none;}
</style>
""", unsafe_allow_html=True)

st.markdown('<style>' + open('./style/side.css').read() + '</style>', unsafe_allow_html=True)
dbFile = './use/location.db'

conn = None
conn = sqlite3.connect(dbFile)
st.markdown(
    """<style>
    div[class*="stSlider"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown(
"""
#### This page shows the predicted score of the user's satisfaction with the tourist attraction by the survey.
"""
)
st.markdown("""<br><br>""", unsafe_allow_html=True)
if conn is not None: #관광지, 카페, 레스토랑 중 선택
    st.markdown(""" ##### 🔻 Select the type of place you want to adjust 🔻""")
    placeName = st.selectbox(
        "",
        ["CAFE", "RESTAURANT", "ATTRACTION"],
        index=0  
    )

    # 선택된 카테고리에 해당하는 테이블 이름
    tableDict = {"ATTRACTION": "attractionscore", "CAFE": "cafescore", "RESTAURANT": "restaurantscore"}
    table = tableDict[placeName]

    st.subheader(f"If you see an interesting *{placeName}* give me a high score :sunglasses:")
    
    # 데이터베이스에서 현재 점수를 조회
    cur = conn.cursor()
    cur.execute(f"SELECT name, score FROM {table}")
    rows = cur.fetchall()

    # 각 장소에 대한 슬라이더 생성 및 점수 조절
    for name, score in rows:
        newScore = st.slider(f"{name}", 1, 100, int(score), 1, key=f"{table}_{name}")
        # 슬라이더 값이 변경되면 데이터베이스 업데이트
        if newScore != score:
            cur.execute(f"UPDATE {table} SET score = ? WHERE name = ?", (round(newScore, 1), name))
            conn.commit()

    conn.close()
    
st.markdown("""
            ##### If you've given me all the score for the place, please check the results❗
            """)


if st.button('Check Result❗'):
    st.switch_page("./pages/3_ChatPage.py")

import sys
import os
import streamlit as st
from streamlit_option_menu import option_menu
from st_on_hover_tabs import on_hover_tabs
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Follow Me!",
    page_icon="👋",
)
st.markdown("""
<style>
.big-font {
    font-size:60px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Welcome to Follow Me! 👋</p>', unsafe_allow_html=True)
st.markdown(""" * * * """)

st.markdown('<style>' + open('./style/side.css').read() + '</style>', unsafe_allow_html=True)
    



st.markdown(
"""
# Motivation
"""
)
st.markdown(
"""
* ### We thought that  travel comfortably abroad by using the recommended algorithm and generation ai Conversely, We made it with the idea of making foreigners who came to Korea comfortable
"""
)
st.markdown("""<br><br>""", unsafe_allow_html=True)
st.markdown(
"""
# What different Follow Me ? 
"""
)
st.markdown(
"""
* ### It's not just a recommendation, but a recommendation algorithm is used to receive user opinions and recommend it 
* ### It provides a lot of information about recommended places using generative AI 
"""
)


   

        

        


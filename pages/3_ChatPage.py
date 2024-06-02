import os
import sys
import streamlit as st
import folium
import sqlite3
from streamlit_folium import folium_static

path = os.path.dirname('__file__')
use = 'use'
use_path = os.path.join(path,use)
sys.path.append(use_path)

from GptLoad import openapi, openapi_attraction, openapi_cafe, openapi_restaurant
import googlemaps
import polyline
import time
st.set_page_config(layout="wide")
st.markdown('<style>' + open('./style/side.css').read() + '</style>', unsafe_allow_html=True)
st.markdown("""
<style>
.big-font {
    font-size:100px !important;
}
</style>
""", unsafe_allow_html=True)

def getRestaurant():
    conn = sqlite3.connect('./use/location.db')
    cur = conn.cursor()
    cur.execute("SELECT name FROM restaurantscore WHERE score = (SELECT MAX(score) FROM restaurantscore)")
    result = cur.fetchone() 
    conn.close()
    return result[0] if result else None

def getCafe():
    conn = sqlite3.connect('./use/location.db')
    cur = conn.cursor()
    cur.execute("SELECT name FROM cafescore WHERE score = (SELECT MAX(score) FROM cafescore)")
    result = cur.fetchone() 
    conn.close()
    return result[0] if result else None

def getAttraction():
    conn = sqlite3.connect('./use/location.db')
    cur = conn.cursor()
    cur.execute("SELECT name FROM attractionscore WHERE score = (SELECT MAX(score) FROM attractionscore)")
    result = cur.fetchone() 
    conn.close()
    return result[0] if result else None

def setScoreZero(name):
    conn = sqlite3.connect('./use/location.db')
    cur = conn.cursor()
    cur.execute("UPDATE restaurantscore SET score = 0 WHERE name = ?", (name,))
    conn.commit()  
    conn.close()

def getRestaurantLocation(name):
    conn = sqlite3.connect('./use/location.db')
    cur = conn.cursor()
    cur.execute("SELECT feature, value FROM restaurant WHERE name = ? AND feature = '위경도'", (name,))
    result = cur.fetchone()
    conn.close()
    latitude, longitude = map(float, result[1].split(','))
    return latitude, longitude

def getCafeLocation(name):
    conn = sqlite3.connect('./use/location.db')
    cur = conn.cursor()
    cur.execute("SELECT feature, value FROM cafe WHERE name = ? AND feature = '위경도'", (name,))
    result = cur.fetchone()
    conn.close()
    latitude, longitude = map(float, result[1].split(','))
    return latitude, longitude

def getAttractionLocation(name):
    conn = sqlite3.connect('./use/location.db')
    cur = conn.cursor()
    cur.execute("SELECT feature, value FROM attraction WHERE name = ? AND feature = '위경도'", (name,))
    result = cur.fetchone()
    conn.close()
    latitude, longitude = map(float, result[1].split(','))
    return latitude, longitude

def get_directions(origin, destination):
    gmaps = googlemaps.Client('AIzaSyACPl1nwMoOfOrLXl340zq7zrCWTXmVIcY')
    directions_result = gmaps.directions(origin, destination, 'transit')
    if directions_result:
        print(directions_result)
        print("direction found")
        return directions_result
    else:
        return print("dirction no found")

def add_directions_to_map_blue(m, polyline_str):
    route = polyline.decode(polyline_str)
    folium.PolyLine(route, color='blue').add_to(m)
    return route

def add_directions_to_map__red(m, polyline_str):
    route = polyline.decode(polyline_str)
    folium.PolyLine(route, color='red').add_to(m)
    return route

restaurant_name = getRestaurant()
cafe_name = getCafe()
attraction_name = getAttraction()

restaurant_location = getRestaurantLocation(restaurant_name)
cafe_location = getCafeLocation(cafe_name)
attraction_location = getAttractionLocation(attraction_name)
col1,col2 = st.columns(2)
with col1:
    with st.container():
        st.markdown('<p class="big-font">Follow Me! 👋</p>', unsafe_allow_html=True)
        st.markdown("* * *")
        # Folium 지도 생성
        m = folium.Map(location=[35.840544, 127.132029], zoom_start=13)

        # 마커 추가
        if restaurant_location:
            folium.Marker(restaurant_location, popup=f"{restaurant_name}", tooltip="식당 위치", icon=folium.DivIcon(html='<i class="fa-solid fa-utensils"style="font-size: 36px;"></i>')).add_to(m)
        if attraction_location:
            folium.Marker(attraction_location, popup=f"{attraction_name}", tooltip="관광지 위치", icon=folium.DivIcon(html='<i class="fa-solid fa-torii-gate"style="font-size: 36px;"></i>')).add_to(m)
        if cafe_location:
            folium.Marker(cafe_location, popup=f"{cafe_name}", tooltip="카페 위치", icon=folium.DivIcon(html='<i class="fa-solid fa-mug-saucer"style="font-size: 36px;"></i>')).add_to(m)

        # 음식점에서 관광지까지 경로 그리기
        directions_result = get_directions(restaurant_name, attraction_name)
        overview_polyline = directions_result[0]['overview_polyline']['points']
        add_directions_to_map_blue(m, overview_polyline)

        #관광지에서 카페까지 경로 그리기
        directions_result = get_directions(attraction_name, cafe_name)
        overview_polyline = directions_result[0]['overview_polyline']['points']
        add_directions_to_map__red(m, overview_polyline)


        folium_static(m) #지도 생성
#생성형 AI 정보 제공
with col2:
    with st.container():
        st.markdown("""<br><br><br><br><br><br><br>""", unsafe_allow_html=True)
        st.write(openapi(restaurant_name, cafe_name, attraction_name))
        st.write(openapi_restaurant(restaurant_name))
        st.write(openapi_attraction(attraction_name))
        st.write(openapi_cafe(cafe_name))


    


                
                                             
        




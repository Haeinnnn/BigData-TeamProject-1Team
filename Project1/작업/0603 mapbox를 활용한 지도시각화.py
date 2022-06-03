from mapboxgl.viz import *
import os
from mapboxgl.utils import create_color_stops
from mapboxgl.utils import create_numeric_stops

geo_data = 'C:/BigData/work/R_Project/ch011/Rpython/Seoul.geo.json'

# json 파일이라 파이썬 파일 읽기
import json
with open(geo_data, encoding='UTF-8') as f:
    data = json.loads(f.read())

# mapbox에서 Access tokens url 가져오기
token = 'pk.eyJ1IjoiZWVoZWFpbmVlIiwiYSI6ImNsM3RpZjFpczA5aXIzY3FwdHpyeHdvc2MifQ.k8l5ufgjLjeXxBmnyyC10A'

# 서울시 중심부의 경도, 위도 입니다. 
center = [126.986, 37.565]

# 시각화 할 값에 따른 색상의 범주를 지정해줍니다.
color_breaks = [0, 100, 200, 300]
color_stops = create_color_stops(color_breaks, colors='OrRd')


# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
viz = ChoroplethViz(
    access_token=token, # 자신의 mapbox 계정 api token
    data=data, # json 데이터
    color_property='Crime', # 데이터 내 속성에서 시각화 할 색의 기준이 될 속성
    color_stops=color_stops, # 시각화할 색상과 각 색상의 범주 값
    center=center, # 지도의 중심점
    zoom=10) # 지도의 줌 레벨

# 맵을 출력합니다.
viz.show()

# 출처 : https://kimdingko-world.tistory.com/187
# 출처 : https://80000coding.oopy.io/80236516-709b-46a0-8a51-e92357e1b66e
# 출처 : https://dailyheumsi.tistory.com/145

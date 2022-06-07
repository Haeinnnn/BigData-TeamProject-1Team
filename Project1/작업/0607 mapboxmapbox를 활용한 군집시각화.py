# -- 안전지수가 낮으면 red, 높으면 blue에 가깝게 나오게

from mapboxgl.viz import *
import os
from mapboxgl.utils import create_color_stops
from mapboxgl.utils import create_numeric_stops

geo_data = 'Result.geo.json'

# json 파일이라 파이썬 파일 읽기
import json
with open(geo_data, encoding='UTF-8') as f:
    data = json.loads(f.read())

# mapbox에서 Access tokens url 가져오기
token = 'pk.eyJ1IjoiZWVoZWFpbmVlIiwiYSI6ImNsM3RpZjFpczA5aXIzY3FwdHpyeHdvc2MifQ.k8l5ufgjLjeXxBmnyyC10A'

# 서울시 중심부의 경도, 위도 입니다. 
center = [126.986, 37.565]

# 시각화 할 값에 따른 색상의 범주를 지정해줍니다.
color_breaks = [-150, -120, -100, -50, 0]
color_stops = create_color_stops(color_breaks, colors='Spectral')
# 색 반전하는 기능이 없어서 반전 색 사용


# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
viz = ChoroplethViz(
    access_token=token, # 자신의 mapbox 계정 api token
    data=data, # json 데이터
    color_property='Safety_var', # 데이터 내 속성에서 시각화 할 색의 기준이 될 속성
    color_stops=color_stops, # 시각화할 색상과 각 색상의 범주 값
    center=center, # 지도의 중심점
    zoom=9.5, # 지도의 줌 레벨
    label_property='Rank') # 지도에 영문이름 출력

# 맵을 출력합니다.
viz.show()


# -- 안전지수가 가장 낮은곳 5곳을 red로
geo_data = 'Result.geo.json'

# json 파일이라 파이썬 파일 읽기
import json
with open(geo_data, encoding='UTF-8') as f:
    data = json.loads(f.read())

# mapbox에서 Access tokens url 가져오기
token = 'pk.eyJ1IjoiZWVoZWFpbmVlIiwiYSI6ImNsM3RpZjFpczA5aXIzY3FwdHpyeHdvc2MifQ.k8l5ufgjLjeXxBmnyyC10A'

# 서울시 중심부의 경도, 위도 입니다. 
center = [126.986, 37.565]

# 시각화 할 값에 따른 색상의 범주를 지정해줍니다.
match_color_stops = [
    ['동대문구', '#B73625'], 
    ['동작구', '#EA5330'], 
    ['관악구', '#EF9884'],
    ['중구', '#FAC0B1'],
    ['광진구', '#FFE1D7']]

# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
viz = ChoroplethViz(
    access_token=token, # 자신의 mapbox 계정 api token
    data=data, # json 데이터
    color_property='name', # 데이터 내 속성에서 시각화 할 색의 기준이 될 속성
    color_function_type='match',
    color_stops=match_color_stops, # 시각화할 색상과 각 색상의 범주 값
    color_default='rgba(52,73,94,1)',
    center=center, # 지도의 중심점
    zoom=9.5, # 지도의 줌 레벨
    label_property='name') # 지도에 영문이름 출력

# 맵을 출력합니다.
viz.show()


# -- 5곳을 제외한 나머지 곳을 green으로
geo_data = 'Result.geo.json'

# json 파일이라 파이썬 파일 읽기
import json
with open(geo_data, encoding='UTF-8') as f:
    data = json.loads(f.read())

# mapbox에서 Access tokens url 가져오기
token = 'pk.eyJ1IjoiZWVoZWFpbmVlIiwiYSI6ImNsM3RpZjFpczA5aXIzY3FwdHpyeHdvc2MifQ.k8l5ufgjLjeXxBmnyyC10A'

# 서울시 중심부의 경도, 위도 입니다. 
center = [126.986, 37.565]

# 시각화 할 값에 따른 색상의 범주를 지정해줍니다.
match_color_stops = [
    ['서초구', '#274E2C'],
    ['종로구', '#274E2C'],
    ['도봉구', '#274E2C'],
    ['노원구', '#274E2C'],
    ['강북구', '#20A844'],
    ['은평구', '#20A844'],
    ['용산구', '#20A844'],
    ['성동구', '#20A844'],
    ['성북구', '#44B390'],
    ['강서구', '#44B390'],
    ['강남구', '#44B390'],
    ['강동구', '#44B390'],
    ['양천구', '#40CF53'],
    ['송파구', '#40CF53'],
    ['구로구', '#40CF53'],
    ['서대문구', '#40CF53'],
    ['마포구', '#90D5A2'],
    ['영등포구', '#90D5A2'],
    ['중랑구', '#90D5A2'],
    ['금천구', '#90D5A2']] # 색 5개 4개씩


# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
viz = ChoroplethViz(
    access_token=token, # 자신의 mapbox 계정 api token
    data=data, # json 데이터
    color_property='name', # 데이터 내 속성에서 시각화 할 색의 기준이 될 속성
    color_function_type='match',
    color_stops=match_color_stops, # 시각화할 색상과 각 색상의 범주 값
    color_default='rgba(52,73,94,0)', # 아예 투명하게
    center=center, # 지도의 중심점
    zoom=9.5, # 지도의 줌 레벨
    label_property='name') # 지도에 영문이름 출력

# 맵을 출력합니다.
viz.show()

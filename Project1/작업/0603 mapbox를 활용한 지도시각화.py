from mapboxgl.viz import *
import os
from mapboxgl.utils import create_color_stops
from mapboxgl.utils import create_numeric_stops

# ------------------------------ Crime 파일
geo_data = 'Seoul_Crime.geo.json'

# json 파일이라 파이썬 파일 읽기
import json
with open(geo_data, encoding='UTF-8') as f:
    data = json.loads(f.read())

# mapbox에서 Access tokens url 가져오기
token = 'pk.eyJ1IjoiZWVoZWFpbmVlIiwiYSI6ImNsM3RpZjFpczA5aXIzY3FwdHpyeHdvc2MifQ.k8l5ufgjLjeXxBmnyyC10A'

# 서울시 중심부의 경도, 위도 입니다. 
center = [126.986, 37.565]

# 시각화 할 값에 따른 색상의 범주를 지정해줍니다.
color_breaks = [0, 50, 100, 150, 200, 250, 300]
color_stops = create_color_stops(color_breaks, colors='OrRd')


# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
viz = ChoroplethViz(
    access_token=token, # 자신의 mapbox 계정 api token
    data=data, # json 데이터
    color_property='Crime', # 데이터 내 속성에서 시각화 할 색의 기준이 될 속성
    color_stops=color_stops, # 시각화할 색상과 각 색상의 범주 값
    center=center, # 지도의 중심점
    zoom=10, # 지도의 줌 레벨
    below_layer='waterway-label', # 지도에 영문이름 출력
    label_property='Crime') # 지도에 Crime의 데이터값 표시

# 맵을 출력합니다.
viz.show()

# ---------------------------- Pub 파일
geo_data = 'Seoul_Pub.geo.json'

# json 파일이라 파이썬 파일 읽기
import json
with open(geo_data, encoding='UTF-8') as f:
    data = json.loads(f.read())

# mapbox에서 Access tokens url 가져오기
token = 'pk.eyJ1IjoiZWVoZWFpbmVlIiwiYSI6ImNsM3RpZjFpczA5aXIzY3FwdHpyeHdvc2MifQ.k8l5ufgjLjeXxBmnyyC10A'

# 서울시 중심부의 경도, 위도 입니다. 
center = [126.986, 37.565]

# 시각화 할 값에 따른 색상의 범주를 지정해줍니다.
color_breaks = [0, 3, 5, 7, 9]
color_stops = create_color_stops(color_breaks, colors='RdPu')


# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
viz = ChoroplethViz(
    access_token=token, # 자신의 mapbox 계정 api token
    data=data, # json 데이터
    color_property='Pub', # 데이터 내 속성에서 시각화 할 색의 기준이 될 속성
    color_stops=color_stops, # 시각화할 색상과 각 색상의 범주 값
    center=center, # 지도의 중심점
    zoom=10, # 지도의 줌 레벨
    below_layer='waterway-label') # 지도에 영문이름 출력

# 맵을 출력합니다.
viz.show()

# ---------------------------------- Oneperson 파일
geo_data = 'Seoul_Oneperson.geo.json'

# json 파일이라 파이썬 파일 읽기
import json
with open(geo_data, encoding='UTF-8') as f:
    data = json.loads(f.read())

# mapbox에서 Access tokens url 가져오기
token = 'pk.eyJ1IjoiZWVoZWFpbmVlIiwiYSI6ImNsM3RpZjFpczA5aXIzY3FwdHpyeHdvc2MifQ.k8l5ufgjLjeXxBmnyyC10A'

# 서울시 중심부의 경도, 위도 입니다. 
center = [126.986, 37.565]

# 시각화 할 값에 따른 색상의 범주를 지정해줍니다.
color_breaks = [0, 500, 1000, 1500, 2000]
color_stops = create_color_stops(color_breaks, colors='YlGn')


# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
viz = ChoroplethViz(
    access_token=token, # 자신의 mapbox 계정 api token
    data=data, # json 데이터
    color_property='Oneperson', # 데이터 내 속성에서 시각화 할 색의 기준이 될 속성
    color_stops=color_stops, # 시각화할 색상과 각 색상의 범주 값
    center=center, # 지도의 중심점
    zoom=10, # 지도의 줌 레벨
    below_layer='waterway-label') # 지도에 영문이름 출력

# 맵을 출력합니다.
viz.show()

from mapboxgl.viz import *
import os
from mapboxgl.utils import create_color_stops
from mapboxgl.utils import create_numeric_stops

# ----------------------------- CCTV 파일
geo_data = 'Seoul_CCTV.geo.json'

# json 파일이라 파이썬 파일 읽기
import json
with open(geo_data, encoding='UTF-8') as f:
    data = json.loads(f.read())

# mapbox에서 Access tokens url 가져오기
token = 'pk.eyJ1IjoiZWVoZWFpbmVlIiwiYSI6ImNsM3RpZjFpczA5aXIzY3FwdHpyeHdvc2MifQ.k8l5ufgjLjeXxBmnyyC10A'

# 서울시 중심부의 경도, 위도 입니다. 
center = [126.986, 37.565]

# 시각화 할 값에 따른 색상의 범주를 지정해줍니다.
color_breaks = [0, 50, 100, 150, 200]
color_stops = create_color_stops(color_breaks, colors='GnBu')


# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
viz = ChoroplethViz(
    access_token=token, # 자신의 mapbox 계정 api token
    data=data, # json 데이터
    color_property='CCTV', # 데이터 내 속성에서 시각화 할 색의 기준이 될 속성
    color_stops=color_stops, # 시각화할 색상과 각 색상의 범주 값
    center=center, # 지도의 중심점
    zoom=10, # 지도의 줌 레벨
    below_layer='waterway-label') # 지도에 영문이름 출력 # 이거 쓰면 안됨 데이터 일부 출력안됨 ㅡㅡ

# 맵을 출력합니다.
viz.show()

# 출처 : https://kimdingko-world.tistory.com/187
# 출처 : https://80000coding.oopy.io/80236516-709b-46a0-8a51-e92357e1b66e
# 출처 : https://dailyheumsi.tistory.com/145

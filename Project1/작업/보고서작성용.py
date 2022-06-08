from mapboxgl.viz import *
import os
from mapboxgl.utils import create_color_stops
from mapboxgl.utils import create_numeric_stops
#----------------------------------------------------------------------------
# 지도시각화
# geojson 에서 지도 파일 및 필요데이터 입력해서 준비하기
#----------------------------------------------------------------------------
geo_data = 'Result.geo.json'

#----------------------------------------------------------------------------
# json 파일이라 파이썬 파일 읽기
#----------------------------------------------------------------------------
import json
with open(geo_data, encoding='UTF-8') as f:
    data = json.loads(f.read())

#----------------------------------------------------------------------------
# mapbox에서 Access tokens url 가져오기
#----------------------------------------------------------------------------
token = 'pk.eyJ1IjoiZWVoZWFpbmVlIiwiYSI6ImNsM3RpZjFpczA5aXIzY3FwdHpyeHdvc2MifQ.k8l5ufgjLjeXxBmnyyC10A'

#----------------------------------------------------------------------------
# 서울시 중심부의 경도, 위도 입력
#----------------------------------------------------------------------------
center = [126.986, 37.565]

#----------------------------------------------------------------------------
# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
#----------------------------------------------------------------------------
# 시각화 할 값에 따른 색상의 범주를 지정해줍니다.
color_breaks = [-150, -120, -100, -50, 0]
color_stops = create_color_stops(color_breaks, colors='Spectral')

viz = ChoroplethViz(
    access_token=token, # 자신의 mapbox 계정 api token
    data=data, # json 데이터
    color_property='Safety_var', # 데이터 내 속성에서 시각화 할 색의 기준이 될 속성
    color_stops=color_stops, # 시각화할 색상과 각 색상의 범주 값
    center=center, # 지도의 중심점
    zoom=9.8, # 지도의 줌 레벨
    label_property='Rank', # 지도에 Rank 출력
    label_size=8.5, # 데이터값의 크기 조정
    label_halo_width=0.75, # 데이터값의 테두리 조정
    scale=True, # 얼마나 위에서 보고있는지 표기
    scale_position='bottom-left', # 스케일의 위치
    legend_header_fill='rgba(190,190,190,0.5)') # 범례 헤더 색상지정 

#----------------------------------------------------------------------------
# 맵을 출력합니다.
#----------------------------------------------------------------------------
viz.show()

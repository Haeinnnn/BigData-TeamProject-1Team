# ---------- k-means 1번 군집시각화

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
match_color_stops = [
    ['중구', '#720000'],
    ['강남구', '#2669b9'],
    ['관악구', '#2669b9'],
    ['광진구', '#2669b9'],
    ['구로구', '#2669b9'],
    ['금천구', '#2669b9'],
    ['동대문구', '#2669b9'],
    ['동작구', '#2669b9'],
    ['서대문구', '#2669b9'],
    ['성동구', '#2669b9'],
    ['성북구', '#2669b9'],
    ['양천구', '#2669b9'],
    ['영등포구', '#2669b9'],
    ['중랑구', '#2669b9'],
    ['강동구', '#69A65A'],
    ['강북구', '#69A65A'],
    ['강서구', '#69A65A'],
    ['노원구', '#69A65A'],
    ['도봉구', '#69A65A'],
    ['마포구', '#69A65A'],
    ['송파구', '#69A65A'],
    ['용산구', '#69A65A'],
    ['은평구', '#69A65A'],
    ['종로구', '#69A65A'],
    ['서초구', '#69A65A']
]

# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
viz = ChoroplethViz(
    access_token=token, # 자신의 mapbox 계정 api token
    data=data, # json 데이터
    color_property='name', # 데이터 내 속성에서 시각화 할 색의 기준이 될 속성
    color_function_type='match',
    color_stops=match_color_stops, # 시각화할 색상과 각 색상의 범주 값
    center=center, # 지도의 중심점
    zoom=9.8, # 지도의 줌 레벨
    label_property='name', # 지도에 영문이름 출력
    label_size=8.5, # 데이터값의 크기 조정
    label_halo_width=0.75, # 데이터값의 테두리 조정
    scale=True, # 얼마나 위에서 보고있는지 표기
    scale_position='bottom-left') # 스케일의 위치

# 맵을 출력합니다.
viz.show()

# ---------- k-means 2번 군집시각화

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
match_color_stops = [
    ['관악구', 'rgb(114,0,0)'],
    ['동대문구', 'rgb(114,0,0)'],
    ['동작구', 'rgb(114,0,0)'],
    ['강남구', '#A6BFDA'],
    ['금천구', '#A6BFDA'],
    ['영등포구', '#A6BFDA'],
    ['서대문구', '#6A97DD'],
    ['성북구', '#6A97DD'],
    ['광진구', '#1120C6'],
    ['구로구', '#1120C6'],
    ['성동구', '#1120C6'],
    ['양천구', '#1120C6'],
    ['중랑구', '#1120C6']]
# 색 반전하는 기능이 없어서 반전 색 사용


# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
viz = ChoroplethViz(
    access_token=token, # 자신의 mapbox 계정 api token
    data=data, # json 데이터
    color_property='name', # 데이터 내 속성에서 시각화 할 색의 기준이 될 속성
    color_function_type='match',
    color_stops=match_color_stops, # 시각화할 색상과 각 색상의 범주 값
    color_default='rgba(190,190,190,0.5)', # 선택되지 않은 지역의 디폴트색 지정
    center=center, # 지도의 중심점
    zoom=9.8, # 지도의 줌 레벨
    label_property='name', # 지도에 영문이름 출력
    label_size=8.5, # 데이터값의 크기 조정
    label_halo_width=0.75, # 데이터값의 테두리 조정
    scale=True, # 얼마나 위에서 보고있는지 표기
    scale_position='bottom-left', # 스케일의 위치
    legend_header_fill='rgba(190,190,190,0.5)') # 범례 헤더 색상지정 

# 맵을 출력합니다.
viz.show()

# ---------- 막대그래프

import matplotlib.font_manager as fm

font_path = r'C:\Users\user\NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=18)

data = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/data_comb.csv", encoding="euc-kr")
x=data['District'].to_list()		# 데이터 프레임의 지역을 리스트로 저장 
y=data['CCTV'].to_list()			# 테이터 프레임의 CCTV를 리스트로 저장

plt.figure(figsize=(20, 15))			# 그래프 크기 지정
plt.xlabel('서울시 구역별 CCTV현황 (2021년)') # 그래프 x축 이름(label) 지정
# plt.ylabel('CCTV 현황')				# 그래프 y축 이름(label) 지정

colors = ['#e8e8e4', '#e8e8e4', '#e8e8e4', '#e8e8e4', '#fcd5ce',
          '#e8e8e4', '#e8e8e4', '#e8e8e4', '#e8e8e4', '#e8e8e4',
          '#fcd5ce', '#fcd5ce', '#e8e8e4', '#e8e8e4', '#e8e8e4',
          '#e8e8e4', '#e8e8e4', '#e8e8e4', '#e8e8e4', '#e8e8e4',
          '#e8e8e4', '#e8e8e4', '#e8e8e4', '#e8e8e4', '#e8e8e4',]
plt.barh(x, y, color=colors)	# 리스트로 저장한 x와 y로 막대(bar) 그래프 플롯

# ---------- 선과 막대그래프를 같이

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

font_path = r'C:\Users\user\NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=18)
plt.rcParams['font.family'] = 'NanumGothic' # 글씨 깨짐 방지 나눔고딕폰트 설치해야함

data = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/cctv_years.csv", encoding="euc-kr")
district = data['district'].to_list()
min = data['min'].to_list()
y2021 = data['y2021'].to_list()
y2020 = data['y2020'].to_list()

fig = plt.figure(figsize=(20, 15)) ## Figure 생성 
fig.set_facecolor('white') ## Figure 배경색 지정
ax1 = fig.add_subplot() ## axes 생성

colors = '#fcd5ce' ## 바 차트 색
xtick_label_position = list(range(len(district))) ## x축 눈금 라벨이 표시될 x좌표
ax1.set_xticks(xtick_label_position) ## x축 눈금 
ax1.set_xticklabels(district) ## x축 눈금 라벨
ax1.bar(xtick_label_position, y2021, color=colors) ## 바차트 출력

colors = '#e8e8e4' ## 바 차트 색
ax3 = ax1.twinx()
xtick_label_position = list(range(len(district))) ## x축 눈금 라벨이 표시될 x좌표
ax3.set_xticks(xtick_label_position) ## x축 눈금 
ax3.set_xticklabels(district) ## x축 눈금 라벨
ax3.bar(xtick_label_position, y2020, color=colors) ## 바차트 출력
 
color = 'gray'
ax2 = ax1.twinx() ## 새로운 axis 생성
ax2.plot(xtick_label_position, min, color=color, linestyle='--', marker='o') ## 선 그래프 
ax2.tick_params(axis='y', labelcolor=color) ## 눈금 라벨 색상 지정

 
plt.title('서울시 구역별 CCTV현황 (2021년)')
plt.show()

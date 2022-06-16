from mapboxgl.viz import *
import os
from mapboxgl.utils import create_color_stops
from mapboxgl.utils import create_numeric_stops
#============================================================================
# 지도시각화
# geojson 에서 지도 파일 및 필요데이터 입력해서 준비하기
#============================================================================
geo_data = 'Result.geo.json'

#============================================================================
# json 파일이라 파이썬 파일 읽기
#============================================================================
import json
with open(geo_data, encoding='UTF-8') as f:
    data = json.loads(f.read())

#============================================================================
# mapbox에서 Access tokens url 가져오기
#============================================================================
token = '토큰url입력'

#============================================================================
# 서울시 중심부의 경도, 위도 입력
#============================================================================
center = [126.986, 37.565]

#============================================================================
# ChoroplethViz (지리적 영역 범위별 수치 데이터 값을 색(color)으로 표현) 그리기
#============================================================================
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

#============================================================================
# 맵을 출력합니다.
#============================================================================
viz.show()

# 보고서 작성용 출처!!!!!!
# 출처 : https://kimdingko-world.tistory.com/187
# 출처 : https://80000coding.oopy.io/80236516-709b-46a0-8a51-e92357e1b66e
# 출처 : https://dailyheumsi.tistory.com/145
# 출처 : https://m.blog.naver.com/kiddwannabe/221763497317
# 출처 : https://suy379.tistory.com/51
# 컬러팔레트 참고 : https://www.colorion.co/related/D3D3D3

# 전체적으로 색 바꾸기
# sns.set_palette(sns.color_palette(['#d9534f', '#5bc0de', '#5cb85c', '#428bca', '#fcd5ce']))

sns.lineplot(x = 'CCTV', y = 'Crime', hue="cluster", # line으로 시각화를 표현함
                     style='cluster', # cluster에 따라서 스타일을 다르게
                     markers= True, # 점을 다르게 찍어주는거
                     dashes=False, data = data_KK) # 점선같은거 다르게 찍어주는거

# sns.barplot # bar로 시각화를 표현함

# 필요한 그래프만 그릴 수 있게 한번에! 추출하기
# dis = ['종로구', '동작구', '동대문구', '관악구']
# new = data_KK[data_KK['district'].isin(dis)]

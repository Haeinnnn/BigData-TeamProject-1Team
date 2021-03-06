# ============================================================================================
# 선행 패키지 설치
# ============================================================================================
# !pip install pandas
# !pip install numpy
# !pip install matplotlib
# !pip install seaborn

# ============================================================================================
# 파이썬에서 패키지를 사용하도록 설정
# ============================================================================================
import pandas as pd # 분석용 파이썬 라이브러리 패키지
import numpy as np # 계산용 파이썬 라이브러리 패키지
import matplotlib.pyplot as plt # 시각화 파이썬 라이브러리 패키지
import seaborn as sns # 시각화 파이썬 라이브러리 패키지 as는 seaborn을 sns로 쓰겠다는 말
# 위에 패키지들이 없으면 !pip install pandas, numpy, matplotlib, seaborn 해주기

# ============================================================================================
# 데이터 셋 로딩하기 (csv 파일을 pandas의 데이터 프레임으로 불러오려면 pd.read_csv())
# ============================================================================================
data = pd.read_csv("data_comb.csv", encoding="euc-kr")
data.head() # 불러온 데이터 확인하기

# ============================================================================================
# matplotlib 으로 전체 데이터를 boxplot으로 그려줌
# ============================================================================================
plt.figure(figsize=(20, 5)) # 만들어질 그래프의 사이즈를 지정
data = plt.boxplot(data[['cctv', 'oneperson', 'pub', 'crime']]) # boxplot에 쓸 데이터
plt.xticks([1, 2, 3, 4, 5], ['cctv', 'oneperson', 'pub', 'crime']) # x축의 라벨 지정
plt.show() # 완성된 그래프를 보여줌

# ============================================================================================
# 다른 시각화 라이브러리인 seaborn 으로 boxplot
# ============================================================================================
boxplot= sns.boxplot(y='cctv', data=data) # CCTV만 보여줌
# boxplot= sns.boxplot(y='oneperson', data=data) # oneperson만 보여줌
# boxplot= sns.boxplot(y='pub', data=data) # pub만 보여줌
# boxplot= sns.boxplot(y='crime', data=data) # crime만 보여줌

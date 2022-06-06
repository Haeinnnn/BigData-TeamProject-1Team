# ============================================================================================
# 파이썬에서 패키지를 사용하도록 설정
# ============================================================================================
import pandas as pd # 분석용 파이썬 라이브러리 패키지
import numpy as np # 계산용 파이썬 라이브러리 패키지
import matplotlib.pyplot as plt # 시각화 파이썬 라이브러리 패키지
import seaborn as sns # 시각화 파이썬 라이브러리 패키지 as는 seaborn을 sns로 쓰겠다는 말
# 위에 패키지들이 없으면 !pip install pandas, numpy, matplotlib, seaborn 해주기
# ============================================================================================
# 데이터 셋 로딩하기
# ============================================================================================
data = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/data_comb.csv", encoding="euc-kr")
# ============================================================================================
# 불러온 데이터 확인하기
# ============================================================================================
data.head()
# ============================================================================================
# 파이썬에서 패키지를 사용하도록 설정
# ============================================================================================
# ============================================================================================
# matplotlib 으로 전체 데이터를 boxplot으로 그려줌
# ============================================================================================
plt.figure(figsize=(20, 5)) # 만들어질 그래프의 사이즈를 지정
data = plt.boxplot(data[['CCTV', 'Oneperson', 'Pub', 'Crime']]) # boxplot에 쓸 데이터
plt.xticks([1, 2, 3, 4, 5], ['CCTV', 'Oneperson', 'Pub', 'Crime']) # x축의 라벨 지정
plt.show() # 완성된 그래프를 보여줌
# ============================================================================================
# 다른 시각화 라이브러리인 seaborn 으로 boxplot
# ============================================================================================
boxplot= sns.boxplot(y='CCTV', data=data) # CCTV만 보여줌
# boxplot= sns.boxplot(y='Oneperson', data=data) # Oneperson만 보여줌
# boxplot= sns.boxplot(y='Pub', data=data) # Pub만 보여줌
# boxplot= sns.boxplot(y='Crime', data=data) # Crime만 보여줌

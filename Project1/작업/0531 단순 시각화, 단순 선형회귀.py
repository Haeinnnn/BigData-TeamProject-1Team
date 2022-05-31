import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/data_comb.csv", encoding="euc-kr")
data.head()

plt.rcParams['font.family'] = 'NanumGothic' # 글씨 깨짐 방지 나눔고딕폰트 설치해야함
plt.rcParams['font.size'] = 10 # 폰트 사이즈 조정
plt.rcParams['figure.figsize'] = (15, 10) # 시각화 사이즈 조정

sns.scatterplot(x="District", y="CCTV", hue="CCTV", palette="Reds", s=data["CCTV"]*10, data=data)
# hue CCTV 개수에 따라 색을 다르게
# S 점 사이즈

plt.rcParams['font.family'] = 'NanumGothic' # 글씨 깨짐 방지 나눔고딕폰트 설치해야함
plt.rcParams['font.size'] = 10 # 폰트 사이즈 조정
mpl.rcParams['axes.unicode_minus'] = False # - 깨지는 현상
plt.rcParams['figure.figsize'] = (15, 10)

line = sns.lineplot(x="District", y="Crime", data=data) # 단순선형회귀식

# 출처 : https://dsbook.tistory.com/52

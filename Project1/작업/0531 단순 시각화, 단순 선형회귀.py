import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/data_comb.csv", encoding="euc-kr")
data.head()

# -- 단순 시각화
plt.rcParams['font.family'] = 'NanumGothic' # 글씨 깨짐 방지 나눔고딕폰트 설치해야함
plt.rcParams['font.size'] = 10 # 폰트 사이즈 조정
plt.rcParams['figure.figsize'] = (15, 10) # 시각화 사이즈 조정

sns.scatterplot(x="District", y="CCTV", hue="CCTV", palette="Reds", s=data["CCTV"]*10, data=data)
# hue CCTV 개수에 따라 색을 다르게
# S 점 사이즈

# -- 단순 선형회귀식
plt.rcParams['font.family'] = 'NanumGothic' # 글씨 깨짐 방지 나눔고딕폰트 설치해야함
plt.rcParams['font.size'] = 10 # 폰트 사이즈 조정
mpl.rcParams['axes.unicode_minus'] = False # - 깨지는 현상
plt.rcParams['figure.figsize'] = (15, 10)

line = sns.lineplot(x="District", y="Crime", color='green', data=data) # 단순선형회귀식

# -- matplotlib 회귀식
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

X = data['District'].to_list()
Y = data['Crime'].to_list()

import matplotlib.pyplot as plt
plt.scatter(X, Y)
plt.plot(X, Y, color='red')
plt.title('y = {}*x + {}'.format(lr.coef_[0], lr.intercept_))
plt.show()

# 출처 : https://dsbook.tistory.com/52
# 출처 : https://ordo.tistory.com/103?category=732886

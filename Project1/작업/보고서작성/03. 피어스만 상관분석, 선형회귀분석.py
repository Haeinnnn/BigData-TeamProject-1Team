import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/data_comb.csv", encoding="euc-kr")

# -- 피어스만 상관분석
cor = data.corr() # 수치적 상관관계를 파악할때
cor

# -- 피어스만 상관분석의 시각화
mpl.rcParams['axes.unicode_minus'] = False # - 깨지는 현상 방지
fig, ax = plt.subplots( figsize=(12,12) ) # 시각화 크기

# 삼각형 마스크를 만든다(위 쪽 삼각형에 True, 아래 삼각형에 False)
mask = np.zeros_like(sea, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# 위에서 만들어진 히트맵을 그린다
sns.heatmap(sea, 
            cmap = 'RdYlBu_r', # 컬러맵에서 색을 뽑아냄
            annot = True,   # 실제 값을 표시한다
            mask=mask,      # 표시하지 않을 마스크 부분을 지정한다, 반으로 줄여줌
            linewidths=.5,  # 경계면 실선으로 구분하기
            cbar_kws={"shrink": .5}, # 옆면이 컬러바의 크기 설정 : 절반으로 줄이기
            vmin = -1, vmax = 1   # 컬러바 범위 -1 ~ 1
           )  
plt.show()

# -- 선형 회귀 분석
import statsmodels.formula.api as smf

res = smf.ols(formula='Crime ~ Police + CCTV + Oneperson + Pub', data=data).fit()
print(res.summary())

# 출처 : https://m.blog.naver.com/kiddwannabe/221763497317

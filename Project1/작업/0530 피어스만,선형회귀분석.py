data = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/data_comb.csv", encoding="euc-kr")

sea = data.corr() # 수치적 상관관계를 파악할때
sea
# 상관계수는 0.3 ~ 0.7 사이 뚜렷한 양적 선형관계
# 0.7과 1.0 사이는 강한 양적 선형관계, 상관계수는 -1~1 사이로 나옴.

# ---------- 상관분석 시각화

mpl.rcParams['axes.unicode_minus'] = False # - 깨지는 현상

fig, ax = plt.subplots( figsize=(12,12) )

# 삼각형 마스크를 만든다(위 쪽 삼각형에 True, 아래 삼각형에 False)
mask = np.zeros_like(sea, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# 히트맵을 그린다
sns.heatmap(sea, 
            cmap = 'RdYlBu_r', 
            annot = True,   # 실제 값을 표시한다
            mask=mask,      # 표시하지 않을 마스크 부분을 지정한다
            linewidths=.5,  # 경계면 실선으로 구분하기
            cbar_kws={"shrink": .5},# 컬러바 크기 절반으로 줄이기
            vmin = -1,vmax = 1   # 컬러바 범위 -1 ~ 1
           )  
plt.show()

# ------------------ 선형회귀분석
import statsmodels.formula.api as smf

res = smf.ols(formula='Crime ~ Police + CCTV + Oneperson + Pub', data=data).fit()
print(res.summary())

# 설명력을 가지는 R-squared 결정계수 # Adj. R-squared 수정된 결정계수
# 결정계수는 변수를 많이 쓰면 쓸 수록 커지니까 
# 변수를 많이 써서 식이 커지면 수정된 결정계수를 보기
# p-value 0.05보다 작아야함

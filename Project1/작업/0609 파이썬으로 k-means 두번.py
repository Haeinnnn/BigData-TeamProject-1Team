#========================================
# 불필요한 데이터 제거
#========================================

dataa = data.drop( "Police", axis=1)
dataa = dataa.drop("District", axis=1)
dataa = dataa.drop("Unnamed: 0", axis=1)
dataa


#========================================
# 데이터 표준화
#========================================
from sklearn.preprocessing import StandardScaler
# Standardization 평균 0 / 분산 1

scaler = StandardScaler()   
scaler = scaler.fit_transform(dataa)

scaler = pd.DataFrame(scaler)
scaler


#========================================
# 자동으로 k를 찾는 k-means 엘보우 기법
#========================================
from yellowbrick.cluster import KElbowVisualizer

model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(scaler)

# !pip install -U yellowbrick

# !pip uninstall scikit-learn -y 해결~^^ ㅠㅠ 
# !pip3 install scikit-learn 다시설치해줘야함


#========================================
#========================================

data_K=dataa
data_K

# dataa 가 District랑 index가 빠진값임
# 원본데이터취급, 잘못될까봐 뒤에_k 붙임


#========================================
# 스케일된 데이터를 넣어 클러스터링
#========================================

kmeans = KMeans(n_clusters=3, random_state=0) # k값은 아까 구한 값
clusters = kmeans.fit(scaler)

#클러스터링 변수인 clusters 값을 원본 데이터 내에 넣기 
data_K['cluster'] = clusters.labels_
data_K


#========================================
# cluster를 기준으로 데이터 개수 세기
#========================================

data_K.groupby('cluster').count() 


#========================================
# 그룹별 특징을 알아보기 (그룹별 평균값)
#========================================

data_K.groupby('cluster').mean()

# 0은 중구니까 제외하면 1이 위험지역!


#========================================
# 차원 축소를 통해 4개의 변수를 2개로 축소
#========================================

from sklearn.decomposition import PCA 
X = scaler.copy() # 표준화 변수를 copy한 새로운 변수 'X'를 만들어 PCA를 적용

#객체
pca = PCA(n_components=2) # 2개로 축소

#적용
pca.fit(X)
x_pca = pca.transform(X)
x_pca


# 5개의 변수를 2개의 변수로 줄이는 작업을 통해, 2차원 그래프로 나타내봅니다.
# 이것이 바로 '차원 축소'인데요,
# 대표적인 차원 축소 방법인 PCA(Principal Component Analysis)를 수행합니다.


#========================================
#x_pca를 보기 쉽게 데이터프레임으로 만들기
#========================================

pca_df = pd.DataFrame(x_pca)
pca_df['cluster'] = data_K['cluster'] 
pca_df.head()


#========================================
# 시각화하기
#========================================

axs = plt.subplots()
axs = sns.scatterplot(0, 1, hue='cluster', data=pca_df)
# x축은 0 , y축은 1, 묶는건 클러스터로 묶음


#========================================
# 군집분석 후에 나온 그룹1을 가지고 한번 더 클러스터
#========================================

data_KK = data_K[data_K['cluster']== 1]
data_KK # 변수명은 k는 한번 kk 두번이라


#========================================
# 그룹1로 데이터 표준화
#========================================

from sklearn.preprocessing import StandardScaler
# Standardization 평균 0 / 분산 1

scaler = StandardScaler()   
scaler_KK = scaler.fit_transform(data_KK)

scaler_KK = pd.DataFrame(scaler_KK)
scaler_KK

#========================================
# 자동으로 k를 찾는 k-means 엘보우 기법
#========================================

from yellowbrick.cluster import KElbowVisualizer

model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(scaler_KK)

# !pip install -U yellowbrick

# !pip uninstall scikit-learn -y 해결~^^ ㅠㅠ 
# !pip3 install scikit-learn 다시설치해줘야함


#========================================
# 스케일된 데이터를 넣어 클러스터링
#========================================

kmeans = KMeans(n_clusters=4, random_state=0) # k값은 아까 구한 값
clusters = kmeans.fit(scaler_KK)

#클러스터링 변수인 clusters 값을 원본 데이터 내에 넣기 
data_KK['cluster'] = clusters.labels_
data_KK


#========================================
# cluster를 기준으로 데이터 개수 세기
#========================================

data_KK.groupby('cluster').count()


#========================================
# 그룹별 특징을 알아보기 (그룹별 평균값)
#========================================

data_KK.groupby('cluster').mean()
# 군집 1과 2가 제일 위험함


#========================================
#========================================


# 5개의 변수를 2개의 변수로 줄이는 작업을 통해, 2차원 그래프로 나타내봅니다.
# 이것이 바로 '차원 축소'인데요,
# 대표적인 차원 축소 방법인 PCA(Principal Component Analysis)를 수행합니다.

from sklearn.decomposition import PCA 
X_KK = scaler_KK.copy() # 표준화 변수를 copy한 새로운 변수 'X'를 만들어 PCA를 적용

#객체
pca = PCA(n_components=2) # 2개로 축소

#적용
pca.fit(X_KK)
x_pca_KK = pca.transform(X_KK)
x_pca_KK


#========================================
#========================================


#x_pca를 보기 쉽게 데이터프레임으로 만들기
pca_df_KK = pd.DataFrame(x_pca_KK)
pca_df_KK['cluster'] = data_K['cluster'] 
pca_df_KK.head()


#========================================
#========================================


# 시각화하기

axs = plt.subplots()
axs = sns.scatterplot(0, 1, hue='cluster', data=pca_df_KK)

# 제대로 분류된걸 확인할 수 있었음!
# 너무 도움 많이 받았던 블로그 : https://suy379.tistory.com/51

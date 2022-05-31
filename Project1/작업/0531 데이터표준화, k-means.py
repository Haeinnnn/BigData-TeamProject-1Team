# 데이터 표준화

from sklearn.preprocessing import StandardScaler
# Standardization 평균 0 / 분산 1
scaler = StandardScaler()   
scaler = scaler.fit_transform(dataa)

scaler

# https://mizykk.tistory.com/101

from sklearn.cluster import KMeans
# 적절한 군집수 찾기
# Inertia(군집 내 거리제곱합의 합) number of clusters, k (적정 군집수)

# elbow method 방법

ks = range(1,10)
inertias = []

for k in ks:
    model = KMeans(n_clusters=k)
    model.fit(scaler)
    inertias.append(model.inertia_)

# Plot ks vs inertias
plt.figure(figsize=(4, 4))

plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('')
plt.xticks(ks)
plt.show()

# https://planharry.tistory.com/43

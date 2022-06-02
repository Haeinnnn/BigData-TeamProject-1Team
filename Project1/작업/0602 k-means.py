# 데이터 정규화 후 진행해야함
# 정규화 해야 하는 이유 : 변수별 단위가 다를 때는 비교가 어렵다는 것

# -- elbow method 방법으로 k 찾기
# 적절한 군집수를 찾는방법
# 목적 함수를 정의한다. 이를 왜곡 측정( distortion measure ) 함수라고 한다
# 각각의 점들로부터 그 클러스터의 평균과의 거리의 합을 제곱한 함수
# distortions (군집 내 거리제곱합의 합), number of clusters, k (적정 군집수)

from sklearn.cluster import KMeans

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

# 출처 : https://planharry.tistory.com/43 -- elbow method 이용
# 출처 : https://lucy-the-marketer.kr/ko/growth/k-means-clustering-python-customer-data-analysis/ -- 개념이해
# 출처 : https://predictivehacks.com/k-means-elbow-method-code-for-python/
# 출처 : https://aplab.tistory.com/182 -- 자동으로 k 찾아줌

# 자동으로 k를 찾는 k-means
from yellowbrick.cluster import KElbowVisualizer

model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(scaler)

# !pip install -U yellowbrick

# !pip uninstall scikit-learn -y 해결~^^ ㅠㅠ 
# !pip3 install scikit-learn 다시설치해줘야함

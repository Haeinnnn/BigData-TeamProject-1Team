# !pip install -U yellowbrick
# !pip uninstall scikit-learn -y
# !pip3 install scikit-learn

from yellowbrick.cluster import KElbowVisualizer

model = KMeans()
visualizer = KElbowVisualizer(model, n_clusters=(1,10))
# k에서 n_clusters로 바꾸면 결과가나옴
visualizer.fit(scaler)

# 'KMeans' object has no attribute 'k' 문구가 뜨지만 실행됨

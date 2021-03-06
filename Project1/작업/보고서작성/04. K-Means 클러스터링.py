# ============================================================================================
# 선행 패키지 설치
# ============================================================================================
# !pip install -U yellowbrick
# !pip uninstall scikit-learn -y # 위의 패키지가 제대로 설치가 안될시에 언인스톨을 진행한다
# !pip install scikit-learn

# ============================================================================================
# 파이썬에서 패키지를 사용하도록 설정
# ============================================================================================
from yellowbrick.cluster import KElbowVisualizer # Elbow Method를 이용

# ============================================================================================
# 자동으로 k 값을 찾아주는 수식
# ============================================================================================
model = KMeans()
visualizer = KElbowVisualizer(model, n_clusters=(1,10)) # k의 범위를 1부터 10까지
visualizer.fit(scaler) # 알맞은 k 값을 찾아준다

# 'KMeans' object has no attribute 'k' 문구가 뜨지만 실행됨

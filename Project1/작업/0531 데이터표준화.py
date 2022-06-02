# 데이터 표준화

from sklearn.preprocessing import StandardScaler
# Standardization 평균 0 / 분산 1
scaler = StandardScaler()   
scaler = scaler.fit_transform(dataa)

scaler

# 출처 : https://mizykk.tistory.com/101

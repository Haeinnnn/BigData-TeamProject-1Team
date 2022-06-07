# ============================================================================================
# 파이썬에서 패키지를 사용하도록 설정
# ============================================================================================
import pandas as pd # 분석용 파이썬 라이브러리 패키지
import numpy as np # 계산용 파이썬 라이브러리 패키지
# 위에 패키지들이 없으면 !pip install pandas, numpy 해주기

# ============================================================================================
# 데이터 셋 로딩하기 (csv 파일을 pandas의 데이터 프레임으로 불러오려면 pd.read_csv())
# ============================================================================================
crime = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/crime_seoul.csv", encoding="euc-kr")
oneperson = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/Oneperson.csv", encoding="euc-kr")
pub = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/pub_seoul.csv", encoding="euc-kr")
cctv = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/cctv_seoul.csv", encoding="euc-kr")
# ============================================================================================
# for문으로 merge(공통 데이터끼리 병합해줌)를 반복해서 합치기
# ============================================================================================
i = 0; # 반복을 알아보려고 넣은 변수
comb = crime # 안에 아무것도 없으면 이상한 내용으로 출력됨
datalist = [oneperson, pub, cctv] # 합칠 csv들
for idx in range(len(datalist)):  # 리스트의 길이만큼 반복한다
    comb = pd.merge(comb, datalist[i], left_on='District', right_on='District')
    # merge를 이용하여 합쳐줌 left right 둘다 district를 기준으로 합쳐준다
    i=i+1
    print(i, "번 반복") # 제대로 반복되었는지 확인

print(comb) # 제대로 병합되었는지 확인
# ============================================================================================
# 완성된 데이터 셋을 저장해줌
# ============================================================================================
comb.to_csv('datacomb.csv', index=False, encoding="euc-kr")

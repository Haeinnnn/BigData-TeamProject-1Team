import pandas as pd
import numpy as np

crime = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/crime_seoul.csv", encoding="euc-kr")
oneperson = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/Oneperson.csv", encoding="euc-kr")
cctv = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/pub_seoul.csv", encoding="euc-kr")

i = 0;
comb = crime # 안에 아무것도 없으면 이상한 내용으로 출력됨
datalist = [cctv, oneperson] # 합칠 csv들
for idx in range(len(datalist)):  # 리스트의 길이만큼 반복한다
    comb = pd.merge(comb, datalist[i], left_on='District', right_on='District') # merge를 이용하여 합쳐줌 left right 둘다 district를 기준으로
    i=i+1
    print(i, "번 반복") # 제대로 되었는지 확인

print(comb)
comb.to_csv('datacomb.csv', index=False, encoding="euc-kr")

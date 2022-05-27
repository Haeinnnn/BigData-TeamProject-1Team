# 머지로 파이썬 합치기
# 머지의 단점 = 2개밖에 안됨, for 문으로 돌리는거 생각해보기

# import pandas as pd
# import numpy as np
# import glob
# import os

# output = glob.glob('C:\BigData\work\R_Project\ch011\Rpython\*.csv')
# r로 시작하는 다른 방식이랑 차이가 없음
# 어떤 파일들이 들어있는지 확인
# print(output)

# forders = os.listdir('C:\BigData\work\R_Project\ch011\RPython')
# print(forders)

# groups = df_all.groupby('District') # 지역명으로 그룹을 만듦
# groups.size() # 각 지역명이 몇개나 되는지 확인

# forders = os.listdir('C:\BigData\work\R_Project\ch011\RPython')
# print(forders)

# df_all = pd.DataFrame()
# for i in range(0,len(forders)):
#     if forders[i].split('.')[1] == 'csv':
#         file = 'C:\BigData\work\R_Project\ch011\RPython/'+forders[i]
#         df= pd.read_csv(file,encoding='euc-kr') 
#         df_all = pd.concat([df_all, df])

# df_all
# 그룹별로 합치는 코드인데... 기준점을 정할 수 없었음 출처 : https://javapp.tistory.com/169

# ---- 원래 썼던 코드
# pd.merge(crime, cctv, left_on='District', right_on='District')

# ---- for문 연습
# sum = 0
# c = 1
# o = 2
# test = {c, o}
# for i in test:
#     print(i)
#     sum = i + sum
# print(sum)

# 본문 코드
# 밑이 진ㅉ

import pandas as pd
import numpy as np

crime = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/crime_seoul.csv", encoding="euc-kr")
oneperson = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/Oneperson.csv", encoding="euc-kr")
cctv = pd.read_csv("C:/BigData/work/R_Project/ch011/Rpython/pub_seoul.csv", encoding="euc-kr")


j = 0;
summ = crime # 안에 아무것도 없으면 이상한 내용으로 출력됨
ttest = [cctv, oneperson] # 합칠 csv들
for idx in range(len(ttest)):  # ttest 리스트의 길이만큼 반복한다
    summ = pd.merge(summ, ttest[j], left_on='District', right_on='District') # merge를 이용하여 합쳐줌 left right 둘다 district를 기준으로
    j=j+1
    print(j, "번 반복") # 제대로 되었는지 확인
    
# type(ttest) # ttest의 타입을 확인 = list

print(summ)
summ.to_csv('end.csv', index=False, encoding="euc-kr")

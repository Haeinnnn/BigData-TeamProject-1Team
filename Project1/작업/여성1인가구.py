# 21년 서울 열린데이터 광장 - 서울시 가구원수별 가구수 (동별) 통계 (2021) 참조시
# 3,982,290 가구 중 1인가구는 1,390,710 가구였음
# csv 파일은 서울 열린데이터 광장 - 서울시 1인가구(거처종류별) 통계 (2021)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

womandata = pd.read_csv("C:/BigData/work/R_Project/ch011/woman_households.csv", encoding="euc-kr")
womandata
# csv 파일을 pandas의 데이터 프레임으로 불러오려면 pd.read_csv()

womandata.notnull().sum()
# null 값 확인

womandata.rename(columns = {'주택(거처)의 종류.1':'단독주택', '주택(거처)의 종류.2':'아파트',
                            '주택(거처)의 종류.3':'연립주택', '주택(거처)의 종류.4':'다세대주택',
                            '주택(거처)의 종류.5':'비거주용 건물내 주택'
                            }, inplace=True) # 보기 힘드니까 열 이름들을 제대로 바꿔줌
                                             # 원래 제대로 나와 있는데 csv로 바꾸면서 틀어진거

womandata = womandata.loc[womandata["성별"]=="여자", ["자치구", "성별", "합계", "단독주택", "아파트", "연립주택",
                                      "다세대주택", "비거주용 건물내 주택", "주택이외의 거처"]]
# △ loc를 써서 필요한 행과 열만 추출, 행에선 여자인 행만 추출하고 열에선 필요한 열을 추출
womandata

# -- 면적당 여성 1인가구 수를 조사하기 위해서 면적을 추가 (단위 km2)
womandata.insert(9,'면적', [605.23, 23.91, 9.96, 21.87, 16.86, 17.06, 14.22,
                         18.5, 24.58, 23.6, 20.65, 35.44, 29.71, 17.63, 23.85, 17.41,
                         41.44, 20.12, 13.02, 24.55, 16.35, 29.57, 46.98, 39.5, 33.87, 24.59])
# 9번째 열에 면적 구당 데이터 추가하기
womandata

# womandata.info() # 타입확인
womandata.dtypes # 데이터프레임 타입확인 (둘다가능)

# test = womandata['합계'] / womandata['면적'] 같은 타입이 아니라 계산이 안됨

# -- 같은 타입으로 바꿔주기 위한 작업
womandata['합계']= womandata['합계'].str.replace(pat=r'[^\w]',repl=r'',regex=True)
womandata['합계'] # △ 특수문자 제거해주기

womandata = womandata.astype({'합계':'float64'}) # float 타입으로 타입 변환
womandata.info()

test = womandata['합계'] / womandata['면적']
# round(test,2) # 소수점 2자리까지만 출력
test = round(test)
test

test = test.astype('int') # .0을 없애기 위한 타입 변환
test.info

# test = test.split("")
# print(test[1])
# 문자열일때 쪼개는 함수. r의 cbind와 같은 역할
# float 때문에 .0 이 나오는 문제여서 전부 주석처리

# test.columns = ['면적당 1인 가구 수']
# test
# ★ 안되어서 직접 합치고 바꿈...
# test["C"] = np.nan # 새 열 추가하고 이름 바꾸려고 했으나 행이 추가됨 ㅠㅠ..

womandata = pd.concat([womandata, test], axis=1) # axis=1이 없으면 NaN 값으로 나옴
womandata

womandata = womandata.rename(columns = {0:'면적당 1인 가구 수'}) 
womandata

# -- 필요한 값만 추출해서 저장
end = womandata[["자치구", "면적당 1인 가구 수"]]
end

end.rename(columns = {'자치구':'District', '면적당 1인 가구 수':'Onepersonhouseholds',}, inplace=True)
# true 안붙이면 복사본이 생성됨
end

end = end.drop(index=[3]) # index 3인 합계를 지움
end

end = end.sort_values('District', ascending=True) # 지역이름인 ㄱㄴㄷ 순으로 정렬해줌
end

end.to_csv('Onepersonhouseholds.csv', index=False, encoding="euc-kr") # 변수이름 수정하기
# 앞에 숫자가 index인데 이걸 false로 하고 저장함, encoding euc-kr로 하면 깨지지 않음

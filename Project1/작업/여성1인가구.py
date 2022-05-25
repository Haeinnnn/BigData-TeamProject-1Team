# 21년 서울 열린데이터 광장 - 서울시 가구원수별 가구수 (동별) 통계 (2021) 참조시
# 3,982,290 가구 중 1인가구는 1,390,710 가구였음


# csv 파일은 서울 열린데이터 광장 - 서울시 1인가구(거처종류별) 통계 (2021)

womandata = pd.read_csv("C:/BigData/work/R_Project/ch011/woman_households.csv", encoding="euc-kr")
# csv 파일을 pandas의 데이터 프레임으로 불러오려면 pd.read_csv()
womandata

womandata.rename(columns = {'주택(거처)의 종류.1':'단독주택', '주택(거처)의 종류.2':'아파트',
                            '주택(거처)의 종류.3':'연립주택', '주택(거처)의 종류.4':'다세대주택',
                            '주택(거처)의 종류.5':'비거주용 건물내 주택'
                            }, inplace=True)
                            # 보기 힘드니까 열 이름들을 제대로 바꿔줌 (csv로 바꾸면서 틀어진거)
womandata

# womandata = womandata.drop([0, 1], axis = 0) # 1행을 지움 # 데이터프레임은 axis 1
# 여자만 추출하면 굳이 행을 지울 필요가 없음
# 합계를 지우고싶으면 # 제거하기

womandata = womandata.loc[womandata["성별"]=="여자", ["자치구", "성별", "합계", "단독주택", "아파트", "연립주택",
                                      "다세대주택", "비거주용 건물내 주택", "주택이외의 거처"]]
# loc를 써서 필요한 행과 열만 추출, 행에선 여자인 행만 추출하고 열에선 필요한 열을 추출함

womandata
womandata.to_csv('실습결과.csv', index=False, encoding="euc-kr")
# 앞에 숫자가 index인데 이걸 false로 하고 저장함, encoding euc-kr로 하면 깨지지 않음

import matplotlib.pyplot as plt
import os
currentPath=os.getcwd()
print(currentPath)

file=currentPath+"\Rpython\data_comb.csv"
data=pd.read_csv(file , encoding = "euc-kr")
data.drop(['Unnamed: 0'], axis=1, inplace=True) # 인덱스 열지움, 바로반영
data

------ 직선그래프

data.plot()

data.plot(y=['CCTV', 'Crime'])

---------- 막대그래프

import matplotlib.font_manager as fm

font_path = r'C:\Users\user\NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path, size=18)

xs=data['District'].to_list()		#dy_day(데이터 프레임)의 index(날짜, 시간)를 리스트로 저장 
ys=data['Crime'].to_list()			#dy_day(테이터 프레임)의 volume 필드를 리스트로 저장

plt.figure(figsize=(10, 6))			#그래프 크기 지정
plt.xlabel('District')				#그래프 x축 이름(label) 지정
plt.ylabel('Crime')				#그래프 y축 이름(label) 지정

plt.bar(xs, ys, width=0.6, color='grey')	#리스트로 저장한 xs와 ys로 막대(bar) 그래프 플롯
plt.rc('font', family='Malgun Gothic') 


------------ pairplot

import seaborn as sns

sns.pairplot(data, hue="District")
plt.show()

출처 : https://steadiness-193.tistory.com/198

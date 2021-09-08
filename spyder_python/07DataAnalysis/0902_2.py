# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:09:45 2021

@author: user9
"""
# WebCrolling(0809_5) + pairplot, heatmap, linearregression (0902_1)

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import urllib.request as ulib
from sklearn.linear_model import LinearRegression # 선형회귀 함수 사용
from sklearn.model_selection import train_test_split # 데이터 분리 (train/test)
from sklearn.metrics import mean_squared_error, r2_score # MSE /상관계수 사용 
import matplotlib.pyplot as plt
import seaborn as sns

# tools - preferences - Editor - Wrap lines 체크
# <URL> ?이전: 위치정보 / 이후: 매개변수.(속성명=value, &으로 구분)
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=82TgFxF3Ydt4K7%2FC9asScsLmWTp1K1c2qcWvQCEPFX36vNn4VSwuN38ftE2G63PGfVrvs9t3Dq3fwlmlg%2ByRWw%3D%3D&returnType=xml&numOfRows=1000&pageNo=1&stationName=%EC%A2%85%EB%A1%9C%EA%B5%AC&dataTerm=MONTH&ver=1.0'

res = ulib.urlopen(url) # 지정된 주소로부터 xmL(계층구조, 태그로 구성)을 반환

# XML Parser를 이용해 XML문서를 DOM(Document Object Model)구조로 변화한 후 데이터에 접근
air = BeautifulSoup(res,"html.parser") # xmL 파싱


df1 = [] #pm10
df2 = [] #pm25
df3 = [] #co
df4 = [] #no2
df5 = [] #so2
df6 = [] #o3
df7 = [] #time

for item in air.findAll("item") : 
# 반복되는 item 태그로부터 item 변수에 항목을 반환

    for pm10 in item.findAll("pm10value") :         
        df1.append(pm10.string)
    for pm25 in item.findAll("pm25value") :
        df2.append(pm25.string)
    for co in item.findAll("covalue") : # 모두 소문자로
        df3.append(co.string)        
    for no2 in item.findAll("no2value") :         
        df4.append(no2.string)       
    for so2 in item.findAll("so2value") :
        df5.append(so2.string)
    for o3 in item.findAll("o3value") : # 모두 소문자로
        df6.append(o3.string)
    for datatime in item.findAll("datatime") : # 모두 소문자로
        df7.append(datatime.string[11:13]) 
          
df = pd.DataFrame({'pm10':df1, 'pm25':df2, 'co':df3,'no2':df4, 'so2':df5, 'o3':df6, 'time':df7})

df = df[df['pm10'] != '-']
df = df[df['pm25'] != '-']

df = df.astype(float)

df.to_csv('C:/kyj/spyder_python/07DataAnalysis/airinfo.csv', encoding='euc-kr', index=False)

X = df.drop(['pm10'], axis=1, inplace=False)

Y = df['pm10']

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3)

lr = LinearRegression()
lr.fit(X_train, Y_train)

Y_predict = lr.predict(X_test)

mse = mean_squared_error(Y_test, Y_predict)
rmse = np.sqrt(mse)
print(mse,rmse)

# lr.coef_ : 각 변수에 대한 기울기(상관계수)/ lr.intercept_ : y 절편
print(lr.coef_, lr.intercept_)

# 기울기를 Series로 저장 / np.round(data,2) : 2자리수까지 data를 반올림. 
coef = pd.Series(data=np.round(lr.coef_,2), index=X.columns) 
print(coef)

'''
# Graph ()
fig, axs = plt.subplots(figsize=(16,16), nrows=2, ncols=3)
X_head = ['pm25', 'co','no2', 'so2', 'o3', 'time']
color=['r','g','b','y','k','r']

for i,head in enumerate(X_head):
    row = int(i/3)
    col = i%3
    sns.regplot(x=head, y='pm10', data = df, ax=axs[row][col], color=color[i])
'''

# 피어슨 상관계수 (correlation)
df_corr = df.corr(method='pearson')
print(df_corr)
# df_corr.to_csv('C:/kyj/spyder_python/07DataAnalysis/df_corr.csv')

# pairplot
#sns.pairplot(df, hue='pm10')
#plt.show()

# heatmap
heatmap_data = df[['pm10','pm25', 'co','no2', 'so2', 'o3', 'time']]
sns.heatmap(heatmap_data.astype(float).corr(), linewidths=0.1, annot=True)
plt.show()











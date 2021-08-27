# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:09:45 2021

@author: user9
"""

from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as ulib

# tools - preferences - Editor - Wrap lines 체크
# <URL> ?이전: 위치정보 / 이후: 매개변수.(속성명=value, &으로 구분)
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=82TgFxF3Ydt4K7%2FC9asScsLmWTp1K1c2qcWvQCEPFX36vNn4VSwuN38ftE2G63PGfVrvs9t3Dq3fwlmlg%2ByRWw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%B6%A9%EB%B6%81&ver=1.0'

res = ulib.urlopen(url) # 지정된 주소로부터 xmL(계층구조, 태그로 구성)을 반환

# XML Parser를 이용해 XML문서를 DOM(Document Object Model)구조로 변화한 후 데이터에 접근
air = BeautifulSoup(res,"html.parser") # xmL 파싱

# 충북지역의 측정소명과 pm10 값을 추출
df1 = []
df2 = []
df3 = []

for item in air.findAll("item") : 
# 반복되는 item 태그로부터 item 변수에 항목을 반환

    for station in item.findAll("stationname") : # 모두 소문자로
        #print(station.string)
        df1.append(station.string)

    for pm10 in item.findAll("pm10value") :
        #print(pm10)            
        df2.append(pm10.string)
        
    for pm25 in item.findAll("pm25value") :
        df3.append(pm25.string)

df = pd.DataFrame({'Station':df1, 'pm10':df2, 'pm25':df3})

#df.head()

print(df.head())

df.to_csv('test.csv', encoding='euc-kr')


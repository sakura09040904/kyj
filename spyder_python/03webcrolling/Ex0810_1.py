# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:51:46 2021

@author: user9
"""

# open API Data Crolling

from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as ulib

url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=82TgFxF3Ydt4K7%2FC9asScsLmWTp1K1c2qcWvQCEPFX36vNn4VSwuN38ftE2G63PGfVrvs9t3Dq3fwlmlg%2ByRWw%3D%3D&returnType=xml&numOfRows=5&pageNo=1&stationName=%EC%9A%A9%EB%8B%B4%EB%8F%99&dataTerm=DAILY&ver=1.0"

res = ulib.urlopen(url) # xmL 반환
air = BeautifulSoup(res,"html.parser") # xmL 파싱 (DOM객체로 반환)

df1 = []
df2 = []
df3 = []

for item in air.findAll("item"):
    for pm10 in item.findAll("pm10value"):
        df1.append(pm10.string)
        
    for pm25 in item.findAll("pm25value"):
        df2.append(pm25.string)
        
    for time in item.findAll("datatime"):
        df3.append(time.string)

df=pd.DataFrame({'PM10':df1, 'PM25':df2, 'TIME':df3})

df.to_csv("station.csv", encoding='euc-kr')        



# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 12:02:43 2021

@author: user9
"""

# 테이블만들기(0806_4) + open API data crolling(0810_1)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as ulib

class MyApp(QWidget) :
    def __init__(self) : 
        super().__init__() 
        
        url="http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=82TgFxF3Ydt4K7%2FC9asScsLmWTp1K1c2qcWvQCEPFX36vNn4VSwuN38ftE2G63PGfVrvs9t3Dq3fwlmlg%2ByRWw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0"
        res = ulib.urlopen(url)
        self.air=BeautifulSoup(res,"html.parser")

        
        self.initUI() 

    def initUI(self) : 
        cnt = len(self.air.findAll("item"))  # 행의 개수
        
        self.tbl = QTableWidget(cnt, 3, self)
        self.tbl.setGeometry(30, 30, 600, 400)
        self.col_head = ['station','pm10','pm25'] # 헤더 변수 선언
        self.tbl.setHorizontalHeaderLabels(self.col_head) # 헤더 변수를 테이블 헤더에 setting
        
        row = 0
        for item in self.air.findAll("item"):
            for station in item.findAll("stationname"):
                self.tbl.setItem(row, 0, QTableWidgetItem(station.string))
            for pm10 in item.findAll("pm10value"):
                self.tbl.setItem(row, 1, QTableWidgetItem(pm10.string)) 
            for pm25 in item.findAll("pm25value"):
                self.tbl.setItem(row, 2, QTableWidgetItem(pm25.string))     
            row += 1    
                
            
                
                
        
        self.show()
        
        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())
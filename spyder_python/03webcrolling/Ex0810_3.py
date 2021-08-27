# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 13:46:02 2021

@author: user9
"""

# 테이블만들기(0806_4) + open API data crolling(0810_1)

from bs4 import BeautifulSoup
import urllib.request as ulib
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=82TgFxF3Ydt4K7%2FC9asScsLmWTp1K1c2qcWvQCEPFX36vNn4VSwuN38ftE2G63PGfVrvs9t3Dq3fwlmlg%2ByRWw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
        
        res = ulib.urlopen(url)
        self.o3 = BeautifulSoup(res,'html.parser')
        
        self.initUI() 

    def initUI(self) : 
        cnt = len(self.o3.findAll("item"))
        
        self.tbl = QTableWidget(cnt, 2, self)
        self.tbl.setGeometry(30, 30, 300, 600)
        
        row=0
        for item in self.o3.findAll("item"):
            for station in item.findAll("stationname"):
                self.tbl.setItem(row, 0, QTableWidgetItem(station.string))
            for ozon in item.findAll("o3value"):
                self.tbl.setItem(row, 1, QTableWidgetItem(ozon.string))
            row += 1    
        self.show()
        


if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())
        

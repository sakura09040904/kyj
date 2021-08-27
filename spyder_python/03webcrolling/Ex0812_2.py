# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:12:38 2021

@author: user9
"""
# open API data crolling(0810_4) + Table에 Data 적용

from bs4 import BeautifulSoup
import urllib.request as ulib
import urllib.parse as parse
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
    
        self.initUI()        
        
    def initUI(self):       
        
        self.lbArea = QLabel("Station",self)
        self.lbArea.setGeometry(15, 30, 40, 30)
        self.leArea = QLineEdit(self)
        self.leArea.setGeometry(60, 30, 120, 30)
        
        self.btnFind = QPushButton("Search",self)
        self.btnFind.setGeometry(190, 30, 80, 30)
        self.btnFind.clicked.connect(self.btnFindEvent)
        
        self.tbl = QTableWidget(self)
        self.tbl.setGeometry(30, 80, 400, 300)
        self.tbl.setColumnCount(4)
        self.tbl_col = ['Date','pm10', 'pm25','Ozon']
        self.tbl.setHorizontalHeaderLabels(self.tbl_col)
        
# Window 영역            
        self.setWindowTitle('Graph Exam')
        self.setGeometry(50,50,600,400)
        self.show()        
        
# 메서드 영역        
# Event Handler        
    def btnFindEvent(self):
        
        station = self.leArea.text()        
        station = parse.quote_plus(station) # 입력한 문자열을 아스키값으로 변환
               
        self.url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=82TgFxF3Ydt4K7%2FC9asScsLmWTp1K1c2qcWvQCEPFX36vNn4VSwuN38ftE2G63PGfVrvs9t3Dq3fwlmlg%2ByRWw%3D%3D&returnType=xml&numOfRows=5&pageNo=1&stationName=" + station+ "&dataTerm=DAILY&ver=1.0"
        
        res = ulib.urlopen(self.url)
        self.data = BeautifulSoup(res,"html.parser")
        self.row = len(self.data.findAll("item"))
        
        self.tbl.setRowCount(5)
        row=0
        for item in self.data.findAll("item"):
            for date in item.findAll("datatime"):
                self.tbl.setItem(row, 0, QTableWidgetItem(date.string))
            for pm10 in item.findAll("pm10value"):
                self.tbl.setItem(row, 1, QTableWidgetItem(pm10.string))
            for pm25 in item.findAll("pm25value"):
                self.tbl.setItem(row, 2, QTableWidgetItem(pm25.string))
            for ozon in item.findAll("o3value"):
                self.tbl.setItem(row, 3, QTableWidgetItem(ozon.string))                
            row += 1                

        
# Main 영역        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 13:51:52 2021

@author: user9
"""

# Graph Drawing(0812_1) + open API data crolling(0812_2) + CB box

from bs4 import BeautifulSoup
import urllib.request as ulib
import urllib.parse as parse
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc
import pymysql


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
    
        self.initUI()        
        
    def initUI(self):       

# Widget영역
        
        self.lbArea = QLabel("Station",self)
        self.leArea = QLineEdit(self)
        
        self.strArea = ['종로구','용암동','용담동']
        self.cbArea = QComboBox(self)
        self.cbArea.addItems(self.strArea)
        
        self.cbArea.currentTextChanged.connect(self.cbChangeEvent) # CB Event 연결
        
        self.btnFind = QPushButton("Search",self)
        self.btnFind.clicked.connect(self.btnFindEvent) # Button Event 연결
        
        self.tbl = QTableWidget(self)
        self.tbl.setColumnCount(4)
        self.tbl_col = ['Date','pm10', 'pm25','Ozon']
        self.tbl.setHorizontalHeaderLabels(self.tbl_col)
        
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig) 


# Layout 영역

        layout1 = QHBoxLayout() # Vertical Box Layout1. 캔버스 영역
        layout1.addWidget(self.lbArea)
        layout1.addWidget(self.leArea)
        layout1.addWidget(self.cbArea)
        layout1.addWidget(self.btnFind)
                       
        layout2 = QVBoxLayout() # 2. Line Editor 영역
        layout2.addWidget(self.tbl)
        layout2.addWidget(self.canvas)

            
        layout = QVBoxLayout() # Horizontal Box Layout
        layout.addLayout(layout1)
        layout.addLayout(layout2)
            
        layout.setStretchFactor(layout1, 1) # 영역 크기 변경 가능여부 true
        layout.setStretchFactor(layout2, 1) 
            
        self.setLayout(layout)        
        
# Window 영역            
        self.setWindowTitle('Graph Exam')
        self.setGeometry(50,50,600,600)
        self.show()   
        
        self.initLoad()
        
        self.timer1 = QTimer(self) 
        self.timer1.start(5000) 
        self.timer1.timeout.connect(self.btnFindEvent) 
        
        
# 메서드 영역        
    def initLoad(self):
        self.leArea.setText('종로구')
        self.btnFindEvent()
        
# Event Handler        

# Combo box change
    def cbChangeEvent(self):
        self.leArea.setText(self.cbArea.currentText())  # CB의 현재 항목을 LE에 입력
        
# Search Button 
    def btnFindEvent(self):
                        
        self.listpm10 = []
        self.listpm25 = []
        self.listozon = []
        self.listdate = []

#URL 연결        
        station = self.leArea.text()        
        station = parse.quote_plus(station) # 입력한 문자열을 아스키값으로 변환
               
        self.url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?serviceKey=82TgFxF3Ydt4K7%2FC9asScsLmWTp1K1c2qcWvQCEPFX36vNn4VSwuN38ftE2G63PGfVrvs9t3Dq3fwlmlg%2ByRWw%3D%3D&returnType=xml&numOfRows=10&pageNo=1&stationName=" + station+ "&dataTerm=DAILY&ver=1.0"
        
        res = ulib.urlopen(self.url)
        self.data = BeautifulSoup(res,"html.parser")
        self.row = len(self.data.findAll("item"))

# tbl 작성
        self.tbl.setRowCount(self.row)
        
        row = self.row-1
        for item in self.data.findAll("item"):
            for date in item.findAll("datatime"):
                self.tbl.setItem(row, 0, QTableWidgetItem(date.string))
                self.listdate.append(date.string[11:16])
                
            for pm10 in item.findAll("pm10value"):
                self.tbl.setItem(row, 1, QTableWidgetItem(pm10.string))
                self.listpm10.append(int(pm10.string)) # 그래프 적용을 위한 형변환
                
            for pm25 in item.findAll("pm25value"):
                self.tbl.setItem(row, 2, QTableWidgetItem(pm25.string))
                self.listpm25.append(int(pm25.string)) # 그래프 적용을 위한 형변환
                
            for ozon in item.findAll("o3value"):
                self.tbl.setItem(row, 3, QTableWidgetItem(ozon.string))                
                self.listozon.append(float(ozon.string)) # 그래프 적용을 위한 형변환
            row -= 1         
        
        self.draw()                
 

# Draw   
           
    def draw(self):

        self.listdate.reverse()               
        self.listpm10.reverse()
        self.listpm25.reverse()
        self.listozon.reverse()

        ax1 = self.fig.add_subplot(211)
        ax1.clear()
        ax1.plot(self.listdate,self.listpm10, 'r--', label='pm10')
        ax1.plot(self.listdate,self.listpm25, 'b-', label='pm25')

        ax2 = self.fig.add_subplot(212)
        ax2.clear()
        ax2.plot(self.listdate,self.listozon, 'g-', label='ozon')

        self.canvas.draw() 

        print(self.listdate)
        print(self.listpm10)
        print(self.listpm25)
        print(self.listozon)


        
# Main 영역        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:56:13 2021

@author: user9
"""

# Graph Drawing(0812_1) + open API data crolling(0812_3) + CB box & Radio Button

from bs4 import BeautifulSoup
import urllib.request as ulib
import urllib.parse as parse
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
    
        self.initUI()        
        
    def initUI(self):       
        font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
        rc('font', family=font_name)
        
# Widget영역

        # Label & Combo Box  
        self.lb1 = QLabel("지역")
        self.lb2 = QLabel("측정소")
        self.lb1.setFixedSize(30, 30)
        self.lb2.setFixedSize(40, 30)
        
        self.listSido = ['-','서울','부산','대전','대구','충북','울산','인천','광주','대전','충남','전북','전남','경북','경남','강원','제주','세종','경기']
        self.listSido.sort()
        self.cbSido = QComboBox(self)    
        self.cbSido.addItems(self.listSido)
        self.cbSido.currentTextChanged.connect(self.cbChangeEvent1)
        
        self.cbStation = QComboBox(self)
        self.cbStation.currentTextChanged.connect(self.cbChangeEvent2)
        
        # Button
        self.btnFind = QPushButton('search', self)
        self.btnFind.clicked.connect(self.btnFindEvent)
        
        # Table
        self.tbl = QTableWidget(self)
        self.tbl.setColumnCount(4)
        self.tbl_col = ['Date','pm10', 'pm25','Ozon']
        self.tbl.setHorizontalHeaderLabels(self.tbl_col)
        
        # Radio button
        self.rbtn1 = QRadioButton("Graph type 1", self)
        self.rbtn2 = QRadioButton("Graph type 2", self)
        self.rbtn3 = QRadioButton("Graph type 3", self)
        self.rbtn1.clicked.connect(self.rbtnEvent)
        self.rbtn2.clicked.connect(self.rbtnEvent)
        self.rbtn3.clicked.connect(self.rbtnEvent)
        self.rbtn1.setChecked(True)
        
        # Graph
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig) 

        
# Layout 영역
        
        layout1 = QHBoxLayout() 
        layout1.addWidget(self.lb1)
        layout1.addWidget(self.cbSido)
        layout1.addWidget(self.lb2)
        layout1.addWidget(self.cbStation)
        layout1.addWidget(self.btnFind)
                       
        layout2 = QVBoxLayout() 
        layout2.addWidget(self.tbl)
        
        layout3 = QHBoxLayout()
        layout3.addWidget(self.rbtn1)
        layout3.addWidget(self.rbtn2)
        layout3.addWidget(self.rbtn3)
              
        layout4 = QVBoxLayout() 
        layout4.addWidget(self.canvas)
            
        layout = QVBoxLayout() 
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)
            
        layout.setStretchFactor(layout1, 1)
        layout.setStretchFactor(layout2, 1) 
        layout.setStretchFactor(layout3, 1) 
        layout.setStretchFactor(layout4, 1) 
            
        self.setLayout(layout)

# Window 영역            
        self.setWindowTitle('Graph Exam')
        self.setGeometry(50,50,600,650)
        self.show()        
        
        
# 메서드 영역

# CB Cahnge    

    def cbChangeEvent1(self):
        self.cbStation.clear()
        self.listStation = []       
        
        sidoname = self.cbSido.currentText()
        sidoname = parse.quote_plus(sidoname)
        
        url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=82TgFxF3Ydt4K7%2FC9asScsLmWTp1K1c2qcWvQCEPFX36vNn4VSwuN38ftE2G63PGfVrvs9t3Dq3fwlmlg%2ByRWw%3D%3D&returnType=xml&numOfRows=100&pageNo=1&sidoName="+sidoname+"&ver=1.0"
        
        res = ulib.urlopen(url)
        self.data = BeautifulSoup(res,"html.parser")
        num = len(self.data.findAll("item"))
        
        row=0
        for item in self.data.findAll("item"):
            for station in item.findAll("stationname"):
                self.listStation.append(station.string)
            row += 1              
                
        self.cbStation.addItems(self.listStation)
            
    def cbChangeEvent2(self):
        self.station = self.cbStation.currentText()
    
# Search Button 
    def btnFindEvent(self):
                        
        self.listpm10 = []
        self.listpm25 = []
        self.listozon = []
        self.listdate = []

        #URL 연결             
        station = parse.quote_plus(self.station) # 입력한 문자열을 아스키값으로 변환
               
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
                self.listpm10.append(int(pm10.string))
                
            for pm25 in item.findAll("pm25value"):
                self.tbl.setItem(row, 2, QTableWidgetItem(pm25.string))
                self.listpm25.append(int(pm25.string))
                
            for ozon in item.findAll("o3value"):
                self.tbl.setItem(row, 3, QTableWidgetItem(ozon.string))                
                self.listozon.append(float(ozon.string))
            row -= 1       
            
        self.listdate.reverse()               
        self.listpm10.reverse()
        self.listpm25.reverse()
        self.listozon.reverse()     
        
        self.fig.clear()
        self.draw1()
        self.canvas.draw()    
            

# Radio Button    

    def rbtnEvent(self):
        
        self.fig.clear()
        
        if self.rbtn1.isChecked() :
            self.draw1()
        elif self.rbtn2.isChecked() :
            self.draw2()
        elif self.rbtn3.isChecked() :
            self.draw3()    
            
        self.canvas.draw()                    

# Draw   
    # rbtn1       
    def draw1(self):
        
        ax1 = self.fig.add_subplot(111)
        ax1.clear()
        ax1.plot(self.listdate,self.listpm10, 'r-', label='pm10')
        ax1.plot(self.listdate,self.listpm25, 'g-', label='pm25')

        ax1.legend()

 
        
    # rbtn2    
    def draw2(self):       

        ax1 = self.fig.add_subplot(121)
        ax1.clear()
        ax1.plot(self.listdate,self.listpm10, 'r-', label='pm10')

        ax2 = self.fig.add_subplot(122)
        ax2.clear()
        ax2.plot(self.listdate,self.listpm25, 'g-', label='pm25')

        ax1.legend()
        ax2.legend()

        
    # rbtn3
    def draw3(self):
        
        ax1 = self.fig.add_subplot(131)
        ax1.clear()
        ax1.plot(self.listdate,self.listpm10, 'r-', label='pm10')

        ax2 = self.fig.add_subplot(132)
        ax2.clear()
        ax2.plot(self.listdate,self.listpm25, 'g-', label='pm25')
        
        ax3 = self.fig.add_subplot(133)
        ax3.clear()
        ax3.plot(self.listdate,self.listozon, 'b-', label='ozon')

        ax1.legend()
        ax2.legend()
        ax3.legend()

   
        
                  
        
        
                       
        
        
                
# Main 영역        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())
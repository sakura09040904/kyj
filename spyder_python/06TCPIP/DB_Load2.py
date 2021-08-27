# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:05:49 2021

@author: user9
"""

# 실시간으로 DB에 저장된 Data를 불러오기 (0811 + client)

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc
import pymysql


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()        
        
    def initUI(self):
        
        self.dbconn()
        
        font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
        rc('font', family=font_name)

# Widget영역

        # Table
        self.tbl = QTableWidget(20,11,self)
        self.tbl_col = ['Date','Temp1','Temp2','Temp3','Temp4','Temp5','Temp6','Temp7','Temp8','Temp9','Temp10']
        self.tbl.setHorizontalHeaderLabels(self.tbl_col)
                
        # Graph
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig) 
        
        # Line Edit
        self.le = QLineEdit(self)
        
        self.timer1 = QTimer(self) # 타이머 생성 (ms단위)
        self.timer1.start(10000) # 10초 간격으로
        self.timer1.timeout.connect(self.dbupdate) # 10초가 지난후 Event 연결
        




# Layout 영역
        layoutTbl = QVBoxLayout() 
        layoutTbl.addWidget(self.tbl)
        
        layoutGraph = QVBoxLayout() 
        layoutGraph.addWidget(self.le)
        layoutGraph.addWidget(self.canvas)
                
        layout = QVBoxLayout() 
        layout.addLayout(layoutTbl)
        layout.addLayout(layoutGraph)
            
        self.setLayout(layout)        
        

        
        
# Window 영역            
        self.setWindowTitle('Sensor Exam')
        self.setGeometry(50,50,1200,800)
        self.show()        
        

# 메서드 영역

# DB 연결
    def dbconn(self):
        conn = pymysql.connect(host='127.0.0.1', user='python', password='12345678', db='test', charset='utf8')        
        self.cursor = conn.cursor()

# DB Update        
    def dbupdate(self):            
        sql = "SELECT * FROM tblsensor ORDER BY ts_date DESC LIMIT 20;"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        
        i=0
        self.xdata = []
        self.ydata1 = []
        for item in self.result:
            for j in range(11):
                val = str(item[j])
                self.tbl.setItem(i, j, QTableWidgetItem(val))
            strtime = item[0]    
            self.xdata.append(strtime[11:])    
            self.ydata1.append(int(item[1]))
            i+=1  
            
        self.xdata.reverse()
        self.ydata1.reverse()                
        self.draw1()

# Draw   
    # rbtn1       
    def draw1(self):
        
        self.fig.clear()
        xdata = []

        plt.subplot(1,3,1)
        
        ax1 = self.fig.add_subplot(111)
        ax1.clear()
        
        ax1.bar(self.xdata,self.ydata1, label='Temp1')
        
        ax1.legend()        
        
        
        self.canvas.draw() 
        
        
# Main 영역        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())        
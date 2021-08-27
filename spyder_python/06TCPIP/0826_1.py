# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:05:49 2021

@author: user9
"""

# Server로부터 Data를 받아 DB에 저장한 후, DB에 있는 Data를 불러와서 표와 그래프로 표시(DBLoad2 + client) 

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc
import pymysql
import socket
import datetime


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()        
        
    def initUI(self):

        
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
        


# Server에 연결               
        HOST = '192.168.0.9'
        PORT = 9999 

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 객체 생성

        self.client_socket.connect((HOST,PORT)) # 서버에 접속
        
        self.timer1 = QTimer(self) 
        self.timer1.start(1000) 
        
        self.timer1.timeout.connect(self.dataload) 
        
        
        
        
        

# 메서드 영역

    def dataload(self):
        data = self.client_socket.recv(1024)
        now = datetime.datetime.today()
        nowstr = now.strftime('%Y-%m-%d %H:%M:%S') 
        # formating하여 str로 저장 (%Y:4자리year, %m:2자리month, %H:2자리hour,... )
        print(nowstr)
        rs = data.decode().split(sep=':') # ':'으로 문자열 split. List로 반환
        
        # graph
        i=1
        for i in range(10):
            rs[i] = int(rs[i])
        print(rs)
        
        self.fig.clear()
        
        ax1 = self.fig.add_subplot(111)
        ax1.clear()
        
        xdata = ['Temp1','Temp2','Temp3','Temp4','Temp5','Temp6','Temp7','Temp8','Temp9','Temp10']
        ydata = rs
        ax1.bar(xdata, ydata, label = nowstr)

        ax1.legend()        
                
        self.canvas.draw()        
        
        # table
        
        

# DB 연결

    def test(self):
        QMessageBox.about(self, 'title', 'text')
        
    def dbconn(self):
        conn = pymysql.connect(host='127.0.0.1', user='python', password='12345678', db='test', charset='utf8')        
        self.cursor = conn.cursor()
'''
# DB Update        
    def dbupdate(self):            

        self.xdata = []
        self.ydata1 = []
        for item in :
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
        
        ax1 = self.fig.add_subplot(111)
        ax1.clear()
        
        ax1.bar(self.xdata,self.ydata1, label='Temp1')
        
        ax1.legend()        
                
        self.canvas.draw() 
'''       
        
# Main 영역        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())        

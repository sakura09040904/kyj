# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:47:18 2021

@author: user9
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem

class MyApp(QWidget) :
    def __init__(self) : 
        super().__init__() 
        self.initUI() 

    def initUI(self) : 
        
        self.tbl = QTableWidget(10, 5, self)
        self.tbl.setGeometry(30, 30, 550, 350)        
                
        #self.tbl.setItem(0, 0, QTableWidgetItem('data1')) (0,0)의 위치에 data1을 삽입
        #self.tbl.setItem(0, 1, QTableWidgetItem('data2'))
        
        count = 1;
        for i in range(10):
            for j in range(5):
                fcnt = '%02d-%02d' % (i+1,j+1) 
                #포맷팅 (10진수(d)를 2자리로 표현하여 전체를 문자열로 저장)
                #strcnt = str(count)
                self.tbl.setItem(i, j, QTableWidgetItem(fcnt))
                #count+=1
        
        
        self.setWindowTitle('Table Exam') 
        self.setGeometry(50, 50, 800, 600)
        self.show()
        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())
        
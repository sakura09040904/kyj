# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 12:00:54 2021

@author: user9
"""

from pymongo import MongoClient
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
    
        self.initUI()        
        
    def initUI(self):       
# Widget 영역        
        self.lbArea = QLabel("Station",self)
        self.lbArea.setGeometry(15, 30, 40, 30)
        self.leArea = QLineEdit(self)
        self.leArea.setGeometry(60, 30, 120, 30)
        
        self.btnFind = QPushButton("Search",self)
        self.btnFind.setGeometry(190, 30, 80, 30)
        self.btnFind.clicked.connect(self.btnFindEvent)
        
        self.tbl = QTableWidget(self)
        self.tbl.setGeometry(30, 80, 400, 300)
        self.tbl.setColumnCount(2)
        self.tbl_col = ['name', 'price']
        self.tbl.setHorizontalHeaderLabels(self.tbl_col)
        
# Window 영역            
        self.setWindowTitle('Graph Exam')
        self.setGeometry(50,50,600,400)
        self.show()        
        
        
# 메서드 영역        
# Event Handler        
    def btnFindEvent(self):
        self.tbl.clear()
        total = 0
        
        conn = MongoClient('mongodb://localhost:27017/') # MongoDB 연결 객체 생성
        db = conn['test'] # test DB 전달
        collection = db['product']  

        if self.leArea.text():
            namesel = self.leArea.text()
            query = {'name':namesel}
            result = collection.find(query)
            total = collection.find(query).count()
            if total == 0:
                QMessageBox.about(self,'ERROR','Data is not found')
                    
        else :
            result = collection.find()
            total = collection.find().count()
        
        self.tbl.setRowCount(total)
        
        row=0
        for item in result:
            self.tbl.setItem(row, 0, QTableWidgetItem(item['name']))
            price = int(item['price'])
            self.tbl.setItem(row, 1, QTableWidgetItem(str(price)))
            row += 1            
     
        
# Main 영역        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())
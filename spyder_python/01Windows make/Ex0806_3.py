# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 11:08:55 2021

@author: user9
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDateEdit, QTimeEdit, \
    QDateTimeEdit, QTextEdit
from PyQt5.QtCore import QDate, QTime, QDateTime

class MyApp(QWidget) :
    def __init__(self) :
        super().__init__() 
        self.initUI()
        
    def initUI(self) :
        dedit = QDateEdit(self) # 날짜 Edit bar 생성 및 위치 설정
        dedit.move(30, 30)
        dedit.setDate(QDate.currentDate()) # 현재 날짜를 dedit에 설정
        
        tedit = QTimeEdit(self) # 시간 Edit bar 생성 및 위치 설정
        tedit.move(30,60)
        tedit.setTime(QTime.currentTime()) # 현재 시간을 tedit에 설정
        
        dtedit = QDateTimeEdit(self) # 날짜/시간 Edit bar 생성 및 위치 설정
        dtedit.move(30, 90)
        dtedit.setDateTime(QDateTime.currentDateTime()) # 현재 날짜/시간으로 설정
        
        te = QTextEdit(self)
        te.setGeometry(30, 120, 300, 200)
       
        self.setWindowTitle('My Window') 
        self.setGeometry(50, 50, 500, 400)
        self.show()
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
      


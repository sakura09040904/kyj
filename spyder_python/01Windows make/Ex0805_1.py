# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:15:06 2021

@author: user9
"""

# wikidocs.net/book/2165 파이썬으로 만드는 나만의 GUI 프로그램

# 레이아웃, 버튼

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget) :
    def __init__(self) :
        super().__init__() 
        self.initUI()
        
    def initUI(self) :
        btn1 = QPushButton('Button1', self)   # 버튼 생성
        btn2 = QPushButton('Button2', self)
        btn3 = QPushButton('Button3', self)
        
        vbox = QVBoxLayout()  # 박스 레이아웃
        vbox.addWidget(btn1)  # 레이아웃에 버튼 추가
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        
        self.setLayout(vbox)  # 레이아웃 관리 객체 생성
        
        self.setWindowTitle('My Window') 
        self.setGeometry(100, 100, 300, 300)
        self.show()
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
      
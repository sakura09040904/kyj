# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 13:28:36 2021

@author: user9
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDial, \
    QLCDNumber

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.lcd.setAutoFillBackground(True)
        self.lcd.move(30,30)
        
        self.dial = QDial(self)
        self.dial.move(30, 80)
        
        self.dial.valueChanged.connect(self.lcd.display) 
        # 이벤트 연결(lcd와 dial을 연결). dial이 움직일 때 lcd값이 변화
        
        self.btn1 = QPushButton('Button 1', self)
        self.btn1.setGeometry(30, 250, 150, 50)
        # 버튼 생성 후 크기.위치 설정
        self.btn2 = QPushButton('Button 2', self)
        self.btn2.setGeometry(30, 350, 150, 50)
        
        self.btn1.clicked.connect(self.btn1Event)
        # 이벤트 연결(btn1 클릭 이벤트와 btn1Event 메서드를 연결). btn1 클릭 시 메서드 실행
        self.btn2.clicked.connect(self.btn2Event)
        
        self.setWindowTitle('Event Exam Window')
        self.setGeometry(50, 50, 500, 500)
        self.show()
        
    def btn1Event(self) :
        self.resize(700,500)
        
    def btn2Event(self) :
        self.resize(500, 700)
                
        
        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())
                
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 14:22:31 2021

@author: user9
"""
# 이벤트연결, 메시지박스
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, \
    QLCDNumber, QDial, QMessageBox
from PyQt5.QtCore import Qt # 키보드 정보    

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.pbarvalue = 50
        self.lcd = QLCDNumber(self)
        self.lcd.setAutoFillBackground(True)
        self.lcd.move(30,30)
        
        self.dial = QDial(self)
        self.dial.move(30, 80)
        
        self.dial.valueChanged.connect(self.lcd.display) 
         # 이벤트 연결(lcd와 dial을 연결). dial이 움직일 때 lcd값이 변화
        
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 200, 200, 50) 
        self.pbar.setValue(self.pbarvalue)
        
        self.btn1 = QPushButton('Button 1',self)
        self.btn1.setGeometry(30, 300, 150, 30)
        self.btn2 = QPushButton('Button 2',self)
        self.btn2.setGeometry(30, 350, 150, 30)
        
        self.btn1.clicked.connect(self.btn1Event)
        self.btn2.clicked.connect(self.btn2Event)
        # 이벤트 연결(btn 클릭 이벤트와 btnEvent 메서드를 연결). 
        # 메서드 호출시 ()를 빼고 입력
        
        self.setWindowTitle('Event Exam Window')
        self.setGeometry(50, 50, 500, 500)
        self.show()
        
    def btn1Event(self):
        if self.pbarvalue >= 100 :
            self.pbarvalue = 100            
        else :
            self.pbarvalue += 10
        self.pbar.setValue(self.pbarvalue)    
            
    def btn2Event(self):
        if self.pbarvalue <= 0 :
            self.pbarvalue = 0
        else :
            self.pbarvalue -= 10
        self.pbar.setValue(self.pbarvalue) 
        
    def keyPressEvent(self, e) : # e: 입력된 키(키보드) / 클릭 위치(마우스)        
        if e.key() == Qt.Key_Left : # 왼쪽 방향키
            if self.pbarvalue <= 0 :
                self.pbarvalue = 0            
            else :
                self.pbarvalue -= 10
            self.pbar.setValue(self.pbarvalue)  
        
        elif e.key() == Qt.Key_Right :
            if self.pbarvalue >= 100 :
                self.pbarvalue = 100            
            else :
                self.pbarvalue += 10
            self.pbar.setValue(self.pbarvalue)
        elif e.key() == Qt.Key_Escape :
            self.close()
        elif e.key() == Qt.Key_1 : # 1 입력시, 
            QMessageBox.about(self, 'caption', 'Message') # Message Box 생성
            
                                        
            
            
            
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())
                        
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 10:40:03 2021

@author: user9
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, \
    QCalendarWidget
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self) # 슬라이더 객체 생성, 가로설정(Horizontal)
        self.slider.move(30, 30) # 슬라이더 위치
        self.slider.setRange(0, 50) # 슬라이더 전체 범위 생성
        self.slider.setSingleStep(2) # 한번에 움직이는 단위
        
        self.dial = QDial(self) # 다이얼 객체 생성
        self.dial.move(30, 70)
        self.dial.setRange(0, 50)
        
        cal = QCalendarWidget(self)
        cal.move(30, 200)
        cal.setGridVisible(True) 
        
        self.setWindowTitle('Slider Test Window')
        self.setGeometry(50, 50, 500, 500)
        self.show()
        
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
      
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:47:40 2021

@author: user9
"""

# 버튼, 라벨, 체크박스, 라디오버튼

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, \
    QLabel, QCheckBox, QRadioButton
from PyQt5.QtCore import Qt

class MyApp(QWidget) :
    def __init__(self) :
        super().__init__()
        self.initUI()
        
    def initUI(self) :

        label1 = QLabel('Label 1', self) # 라벨 객체 생성
        label1.setAlignment(Qt.AlignCenter) # 가운데 정렬
        font1 = label1.font() # 폰트 변수 설정
        font1.setPointSize(20) # 폰트 크기
        font1.setBold(True) # 진하게
        
        label2 = QLabel('Label 2', self)
        label2.setAlignment(Qt.AlignCenter) 
        font2 = label2.font() 
        font2.setPointSize(20)
        font2.setBold(True)
        
        cb = QCheckBox('My Check Box', self) # 체크박스 생성
        
        rbtn1 = QRadioButton('My Radio Button1') # Radio 버튼 생성
        rbtn2 = QRadioButton('My Radio Button2')
        rbtn1.setChecked(True) # check상태로 시작
        
        
        
        
        
        label1.setFont(font1) # 폰트 적용
        label2.setFont(font2)

        layout = QVBoxLayout() # 레이아웃 객체 생성
        
        layout.addWidget(label1) # 레이아웃에 라벨추가
        layout.addWidget(label2)
        layout.addWidget(cb) # 레이아웃에 체크박스 추가
        layout.addWidget(rbtn1)
        layout.addWidget(rbtn2)
        
        self.setLayout(layout) # 레이아웃 관리 객체 설정
        self.setWindowTitle('My Window') 
        self.setGeometry(100, 100, 300, 300)
        self.show()
        
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
              
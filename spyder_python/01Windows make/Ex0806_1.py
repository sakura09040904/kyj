# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 09:45:56 2021

@author: user9
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLineEdit, QProgressBar

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        cb = QComboBox(self) # 콤포박스 생성 및 항목 추가, 위치설정
        cb.addItem('Seoul')
        cb.addItem('Busan')
        cb.addItem('Cheongju')
        cb.move(30, 30)
        
        ql = QLineEdit(self) # Text Line box 생성 및 위치 설정
        ql.move(30, 60)
        
        self.pbar = QProgressBar(self) # 진행 상황 표시바 생성 및 위치설정 
        self.pbar.setGeometry(30, 90, 450, 30)
        self.pbar.setValue(50) # 50%로 고정
        
        self.setWindowTitle('Combobox and Textbox Exam')
        self.setGeometry(50, 50,500,300)
        self.show()
        
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())
              
        
            
        
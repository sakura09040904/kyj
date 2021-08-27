# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow #윈도우 생성을 위한 Lib import
from PyQt5.QtCore import QDate, Qt  # 날짜, 시간

# QMainWindow을 상속받은 class MyApp생성 (My App윈도우를 생성하는 클래스)



class MyApp(QMainWindow) :
    def __init__(self) : # __init__(self) : class 생성자
        super().__init__() # 부모 class 생성자 호출
        self.date = QDate.currentDate()
        self.initUI() # 메서드 호출

    def initUI(self) :  # 윈도우 생성 메서드
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
        self.setWindowTitle('My App') #타이틀바
        self.resize(800,600) # 윈도우 크기
        self.show() # 화면에 등장

if __name__=='__main__':
    app = QApplication(sys.argv) #프로그램 실행
    ex=MyApp() # 객체 생성
    sys.exit(app.exec_())
        
            

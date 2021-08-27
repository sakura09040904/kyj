# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:21:15 2021

@author: user9
"""
# 버튼 클릭 이벤트(0806_6) + DB와 연동하여 Data 출력 및 입력(0810_5)

import pymysql
from PyQt5.QtWidgets import *
import sys


class MyApp(QWidget):
    
# 생성자    
    def __init__(self):
        super().__init__()
        self.dbconn()
        self.initUI()
        self.n=0
        
        
    def initUI(self):
        
# Label 및 Button, Line Editor 영역
            self.lb1  = QLabel('제품번호', self)
            self.lb1.setGeometry(30, 30, 100, 30)
            self.lb1.setStyleSheet("clolor : blue;"
                                   "background-color: #6699cc;"
                                   "border-style:solid;"
                                   "border-width:1px;")
            
            self.le1 = QLineEdit(self)
            self.le1.setGeometry(110, 30, 100, 30)
            
            self.lb2  = QLabel('제품명', self)
            self.lb2.setGeometry(30, 60, 100, 30)
            self.lb2.setStyleSheet("clolor : blue;"
                                   "background-color: #6699cc;"
                                   "border-style:solid;"
                                   "border-width:1px;")
            
            self.le2 = QLineEdit(self)
            self.le2.setGeometry(110, 60, 100, 30)
            
            self.lb3  = QLabel('재고량', self)
            self.lb3.setGeometry(30, 90, 100, 30)
            self.lb3.setStyleSheet("clolor : blue;"
                                   "background-color: #6699cc;"
                                   "border-style:solid;"
                                   "border-width:1px;")
            
            self.le3 = QLineEdit(self)
            self.le3.setGeometry(110, 90, 100, 30)
            
            self.lb4  = QLabel('단가', self)
            self.lb4.setGeometry(30, 120, 100, 30)
            self.lb4.setStyleSheet("clolor : blue;"
                                   "background-color: #6699cc;"
                                   "border-style:solid;"
                                   "border-width:1px;")
            
            self.le4 = QLineEdit(self)
            self.le4.setGeometry(110, 120, 100, 30)
            
            self.lb5  = QLabel('제조업체', self)
            self.lb5.setGeometry(30, 150, 100, 30)
            self.lb5.setStyleSheet("clolor : blue;"
                                   "background-color: #6699cc;"
                                   "border-style:solid;"
                                   "border-width:1px;")
            
            self.le5 = QLineEdit(self)
            self.le5.setGeometry(110, 150, 100, 30)
            
            self.btn1 = QPushButton('Insert', self)
            self.btn1.setGeometry(20, 200, 100, 30)
            self.btn1.clicked.connect(self.btn1Event) #함수 호출시 ()를 빼고
            
            self.btn2 = QPushButton('Load', self)
            self.btn2.setGeometry(130, 200, 100, 30)
            self.btn2.clicked.connect(self.btn2Event)
            
            self.btn3 = QPushButton('Previous', self)
            self.btn3.setGeometry(20, 240, 100, 30)
            self.btn3.clicked.connect(self.btn3Event)
            
            self.btn4 = QPushButton('Next', self)
            self.btn4.setGeometry(130, 240, 100, 30)
            self.btn4.clicked.connect(self.btn4Event)
            
            self.btn5 = QPushButton('Edit', self)
            self.btn5.setGeometry(20, 280, 100, 30)
            self.btn5.clicked.connect(self.btn5Event) 
            
            self.btn6 = QPushButton('Delete', self)
            self.btn6.setGeometry(130, 280, 100, 30)
            self.btn6.clicked.connect(self.btn6Event)

            
            self.leFind = QLineEdit(self)
            self.leFind.setGeometry(20, 320, 100, 30)
            
            self.btnFind = QPushButton('Find', self)
            self.btnFind.setGeometry(130, 320, 100,30)
            self.btnFind.clicked.connect(self.btnFindEvent)
            

            
            
            
# Window 영역            
            self.setWindowTitle('DB exam')
            self.setGeometry(50,50,1500,800)
            self.show()
            
            
            
            
# 메서드 영역            

# DB 연결
    def dbconn(self):            
        self.conn = pymysql.connect(host='127.0.0.1', user='bigdata', password='12345678', db='big_data', charset='utf8')
        
        self.cursor = self.conn.cursor()
        
        
# Event Handler            
# Button1. Insert            
    def btn1Event(self):
        # DB에 data 입력시 %s 사용(not formatting)
        # exucute 함수 호출 시 insert할 value를 sql과 함께 input 
        # insert 후 DB연결 객체를 호출하여 commit 필요
        sql = "INSERT INTO product VALUES(%s, %s, %s, %s, %s)"
        val1 = self.le1.text() # Line Editor에 입력된 text
        val2 = self.le2.text()
        val3 = self.le3.text()
        val4 = self.le4.text()
        val5 = self.le5.text()
        self.cursor.execute(sql, (val1, val2, val3, val4, val5))
        self.conn.commit()
        
        QMessageBox.about(self, 'INSERT', 'Insert Complete!')
        
        self.le1.clear()
        self.le2.clear()
        self.le3.clear()
        self.le4.clear()
        self.le5.clear()
        
# Button2. Load  
    def btn2Event(self):
        sql = "SELECT * FROM product"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()

        self.tblDis()
        
        QMessageBox.about(self, 'LOAD', 'LOAD Complete!')
        
        self.n=0
        self.leDis()
        
    
        
# Button3. PRE             
    def btn3Event(self):
        sql = "SELECT * FROM product"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()       
        self.n = self.n-1
        
        self.totalrows = len(self.result)
        self.lb6 = QLabel(str(self.n)+' / '+str(self.totalrows),self)
        self.lb6.setGeometry(30, 0, 40, 30)        
        if (self.n < 0):
            self.n = 0
            QMessageBox.about(self, 'STOP', 'This is First Value')

        self.leDis()
        # QMessageBox.about(self, 'PREVIOUS', 'Previous value is Loaded')         
        
# Button4. Next          
    def btn4Event(self):
        sql = "SELECT * FROM product"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        row = len(self.result)        
        self.n = self.n+1
        
        if (self.n > row-1):
            self.n = row
            QMessageBox.about(self, 'STOP', 'This is Last Value')
                    
        self.leDis()
        # QMessageBox.about(self, 'NEXT', 'Next Value Loaded')        
        
# Button5. Edit     
    def btn5Event(self):
        sql = "UPDATE product SET pro_num=%s, pro_name=%s, amount=%s, price=%s, company=%s WHERE pro_num=%s"
        val1 = self.le1.text() 
        val2 = self.le2.text()
        val3 = self.le3.text()
        val4 = self.le4.text()
        val5 = self.le5.text()
        self.cursor.execute(sql, (val1, val2, val3, val4, val5, val1))
        self.conn.commit()       
        
        QMessageBox.about(self, 'Edit', 'Value is Edited')
        
        sql = "SELECT * FROM product"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        
        self.tblDis()
        
# Button6. Delete     
    def btn6Event(self):
        sql = "DELETE FROM product WHERE pro_num=%s"
        val1 = self.le1.text()
        self.cursor.execute(sql,val1)
        self.conn.commit()

        QMessageBox.about(self, 'DELETE', 'Value is Deleted')        
        
        sql = "SELECT * FROM product"
        self.cursor.execute(sql)
        self.result = self.cursor.fetchall()
        
        self.tblDis()
        
# Button Find        
    def btnFindEvent(self):
        if len(self.leFind.text())==0:
            sql = "SELECT * FROM product"
            self.cursor.execute(sql)
        else :            
            sql = "SELECT * FROM product WHERE pro_name = %s"
            self.cursor.execute(sql,(self.leFind.text()))

        self.result = self.cursor.fetchall()
        count = len(self.result)
        if count == 0:
            QMessageBox.about(self, 'FIND', str(count)+" data is founded")
            self.tbl.clear()
        
        else:
            QMessageBox.about(self, 'FIND', str(count)+" data is founded")
            self.leDis()
            self.tblDis()
        
# Cell click                 
    def tblCellEvent(self, row, col):
        self.n = row
        self.leDis()
                

# Display 영역
# Table Display
    def tblDis(self):  # 현재 상태의 Table을 Display            
        row = len(self.result)
        col = len(self.result[0])
        self.tbl = QTableWidget(row, col,self)
        self.tbl.setGeometry(20, 370, 500, 400)
        self.tbl_col = ['제품번호','제품명','재고량','단가','제조업체']
        self.tbl.setHorizontalHeaderLabels(self.tbl_col)
        i = 0
        for item in self.result:
            for j in range(col):
                val = str(item[j])
                self.tbl.setItem(i, j, QTableWidgetItem(val))
            i+=1    
            
        self.tbl.show()
        self.tbl.cellClicked.connect(self.tblCellEvent)
        
# Line Editor Display
    def leDis(self):   # 현재 Data를 Line Editor에 Display
        item = self.result[self.n]
        self.le1.setText(item[0])
        self.le2.setText(item[1])
        self.le3.setText(str(item[2]))
        self.le4.setText(str(item[3]))
        self.le5.setText(item[4])        
        
                
        
        
        
                        
        
        
        
# Main 영역        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())                
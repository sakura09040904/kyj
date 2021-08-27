# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 15:04:11 2021

@author: user9
"""
# 테이블만들기(0806_4) + DB와 연동하여 Data추출(0810_4)

import pymysql
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem
import sys

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        conn = pymysql.connect(host='127.0.0.1', user='bigdata', password='12345678',\
                               db='big_data', charset='utf8')
        cursor = conn.cursor()            
        sql = 'select * from product'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        row = len(result)
        col = len(result[0])
        
        self.tbl = QTableWidget(row,col, self)
        self.tbl.setGeometry(30, 30, 600, 400)
        self.col_head = ["상품코드", "상품명", "재고량", "단가", "제조사"]
        self.tbl.setHorizontalHeaderLabels(self.col_head)
        
        '''
        for i in range(row):
            for j in range(col):
                re=str(result[i][j])
                self.tbl.setItem(i, j, (QTableWidgetItem(re)))
        '''
        row = 0
        for item in result:
            for j in range(col):
                re = str(item[j])
                self.tbl.setItem(row, j, QTableWidgetItem(re))
            row += 1
            
        self.show()
        
        cursor.close()
        conn.close()
        
        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())        
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:21:09 2021

@author: user9
"""
# DB와 연동하여 Data 출력

import pymysql

# db 접속
conn=pymysql.connect(host='127.0.0.1', user='bigdata', password='12345678', \
                     db='big_data', charset='utf8')
    
cursor = conn.cursor() # db 안에서 활동할 수 있는 객체 cursor 생성     

sql = 'select * from customer'

cursor.execute(sql) # sql 실행
result = cursor.fetchall()  # 모든 결과 레코드를 튜플로 반환해서 result 변수에 저장 (table전체)
print("Customer")      
for item in result :
    print(item)  
print("="*80)    
    
sql = 'select * from product'
cursor.execute(sql)
result = cursor.fetchall()

print("Product")      
for item in result :
    print(item)  
print("="*80)    
    


cursor.close()
conn.close() # 접속 종료    
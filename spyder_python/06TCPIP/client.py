# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:41:44 2021

@author: user9
"""

# 온도 Data를 받아 DB에 저장하는 Client (0820_1 + 0810_4)

import socket
import datetime
import pymysql

# DB 연결
conn = pymysql.connect(host='127.0.0.1', user='python', password='12345678', db='test', charset='utf8')
cursor = conn.cursor()

# server 연결 및 소켓 생성
HOST = '192.168.0.9'
PORT = 9999 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 객체 생성

client_socket.connect((HOST,PORT)) # 서버에 접속

while True:
    
    data = client_socket.recv(1024)
    now = datetime.datetime.today()
    nowstr = now.strftime('%Y-%m-%d %H:%M:%S') 
    # formating하여 str로 저장 (%Y:4자리year, %m:2자리month, %H:2자리hour,... )
    print(nowstr)
    rs = data.decode().split(sep=':') # ':'으로 문자열 split. List로 반환
    
    i=1
    for i in range(10):
        rs[i] = int(rs[i])
    print(rs)
    
    sql = "INSERT INTO tblsensor VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (nowstr, rs[0],rs[1],rs[2],rs[3],rs[4],rs[5],rs[6],rs[7],rs[8],rs[9]))
    conn.commit()
    
client_socket.close()    
cursor.close()
conn.close()
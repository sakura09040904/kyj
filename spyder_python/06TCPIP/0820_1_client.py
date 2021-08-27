# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:51:52 2021

@author: user9
"""

# 에코 클라이언트 (서버로 에코 data 송신)
# Console 2/A

import socket

HOST = '192.168.0.9'
PORT = 9999 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 객체 생성

client_socket.connect((HOST,PORT)) # 서버에 접속

while True:
    msg = input('Enter message: ')
    if msg == 'quit':
        break
    
    client_socket.send(msg.encode()) # 입력받은 메시지를 Encoding
    
    data = client_socket.recv(1024) # 서버와 동일한 버퍼크기 설정
    print(data.decode())
    
client_socket.close()    
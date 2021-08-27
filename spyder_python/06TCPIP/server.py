# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:40:04 2021

@author: user9
"""

# 온도 Data 전송 server (0820_1)

import socket
from _thread import *
import time
import numpy as np

# 스레드함수
def functhread(client_socket, addr) :
    print(addr[0], addr[1]) # 클라이언트 정보(IP, Port)
    while True :
        try :            
            # random data 발생 (temperature)
            data = ''
            for item in range(9) :
                data = data + str(np.random.randint(20,30)) +':'
            data = data + str(np.random.randint(20,30))               
            
            client_socket.send(data.encode()) # random data 10개 전송(encoding 필요)
            time.sleep(1) # 1초 지연            
        except ConnectionResetError as e:  # 연결이 되지 않음.           
            break
        
    client_socket.close() # 클라이언트 소켓 종료


HOST = '192.168.0.9' 
PORT = 9999 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

server_socket.bind((HOST,PORT))
server_socket.listen() 

while True :
    print('wait..')
    client_socket, addr = server_socket.accept() 
    # 대기상태, 다음 명령을 실행하지 않음. 접속할 경우 클라이언트 소켓과 IP주소 반환
    
    start_new_thread(functhread, (client_socket,addr)) # 클라이언트 접속, 스레드함수 호출

server_socket.close() # 서버 종료
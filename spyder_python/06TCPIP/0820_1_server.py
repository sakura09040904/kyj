# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:59:11 2021

@author: user9
"""

# 에코 서버 (클라이언트로부터 에코data를 받아서 다시 송신)
# Console 1/A

import socket
from _thread import *

def functhread(client_socket, addr) :
    print(addr[0], addr[1]) # 클라이언트 정보(IP, Port)
    while True :
        try :
            data = client_socket.recv(1024) 
            # 스트림 수신대기. (버퍼크기: 1024byte)
            # 수신된 데이터가 없을 경우 다음 명령을 실행하지 않음
            
            if not data :
                break
            
            print(addr[0], addr[1], data.decode()) # 수신된 data 출력
            
            client_socket.send(data) # 수신된 data를 다시 Echo (encoding 상태) 
                        
        except ConnectionResetError as e:  # 연결이 되지 않음.           
            break
        
    client_socket.close() # 클라이언트 소켓 종료


HOST = '192.168.0.9' # Local loopback address, local host와 동일
PORT = 9999 # 0~65535 범위에서 사용가능 (0~1024는 사용하지 않음)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 객체 생성
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 소켓 옵션설정

server_socket.bind((HOST,PORT)) # 소켓과 서버를 바인딩(연결)
server_socket.listen() # 클라이언트로부터 수신준비, 서버 시작.

while True :
    print('wait..')
    client_socket, addr = server_socket.accept() 
    # 대기상태, 다음 명령을 실행하지 않음. 접속할 경우 클라이언트 소켓과 IP주소 반환
    
    start_new_thread(functhread, (client_socket,addr)) # 클라이언트 접속, 스레드함수 호출

server_socket.close() # 서버 종료
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:06:27 2021

@author: user9
"""

import threading

def functhread(number) : 
    print(threading.currentThread().getName(), number)
    

if __name__ == '__main__' :
    for i in range(10) :
        mythread = threading.Thread(target=functhread, args=(i,)) # 스레드 객체 생성
        mythread2 = threading.Thread(target=functhread, args=(i*2,))
        mythread.start()
        mythread2.start()
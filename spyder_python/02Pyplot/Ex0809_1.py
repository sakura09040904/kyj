# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 09:58:02 2021

@author: user9
"""

# List

myList = []

for i in range(1,11,1):
    myList.append(i)

print(myList)
myList.reverse()        
print(myList)


# Tuple. 
# data 수정 불가. 수정을 원할 경우 재정의 해야함.
# 2개 이상의 변수에 동시 저장 가능

tu = ("Java", "Programing")
print(tu)
tu = ("빅데이터", "프로그래밍")
print(tu)

var1,var2 = tu #각 변수에 저장 
print(var1, var2)

var1, _ = tu # 2개 중 1개만 사용 가능.
print(var1)

# Dictionary

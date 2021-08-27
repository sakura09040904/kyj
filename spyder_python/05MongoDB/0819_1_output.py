# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:55:12 2021

@author: user9
"""

from pymongo import MongoClient

conn = MongoClient('mongodb://localhost:27017/') # MongoDB 연결 객체 생성

print(conn.list_database_names()) # 설치된 db name

db = conn['test'] # test DB 전달
collection = db['product']

'''
a = collection.find_one() # 1개씩 출력
print(a)
print(a['name'], a['price'])
'''

result = collection.find() # 전체반환 (Dictionary)
result.sort('name') # 반대 result.sort('name', -1)

query = {'name':'냉장고'}
query = {'price': {'$gte':100000}} # 연산자 문자열 처리
query = {'price': {'$gte':100000, '$lte':200000}}

result = collection.find(query)


for item in result: # 전체 출력
    print(item)
    print(item['name'], item['price'])
    
'''

비교연산자(in mongo DB)
: $eq(==), $ne(!=), $lt(<), $lte(<=), $gt(>), $gte(>=)

'''
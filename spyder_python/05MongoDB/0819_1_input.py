# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:13:32 2021

@author: user9
"""

from pymongo import MongoClient

conn = MongoClient('mongodb://localhost:27017/') # MongoDB 연결 객체 생성

print(conn.list_database_names()) # 설치된 db name

db = conn['test'] # test DB 전달
collection = db['product'] # collection(product) 전달


'''
a = collection.insert_one({'name':'콘칩', 'price': 2000})
print(a.inserted_id)   # insert_one / insert_many 으로 입력시에만 객체로 반환 가능  
    '''

dicts = [{'name':'배추', 'price': 3000}, {'name':'감자', 'price': 2000}]        

a = collection.insert_many(dicts)
print(a.inserted_ids)    
    
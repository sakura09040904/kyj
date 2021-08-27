# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 15:18:08 2021

@author: user9
"""

# 인공신경망을 이용
# conda install tensorflow 설치 후 (node의 개수를 입력하여 Deap learning을 수행)
# Regression : 수식도출을 중심으로 / Deap learning: 경향을 파악하여 Data 예측을 중심으로

import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import boston_housing

(train_x,train_y), (test_x,test_y) = boston_housing.load_data()
# bonston Dataset을 가져와 train_x,y와 test_x,y 각각에 저장

# 평균과 표준편차
x_mean = train_x.mean() 
x_std = train_x.std()
y_mean = train_y.mean() 
y_std = train_y.std()


# 정규화 (train dataset을 이용해 test dataset을 정규화) / 평균:0, 표준편차:1
train_x -= x_mean
train_x /= x_std
test_x -= x_mean
test_x /= x_std

train_y -= y_mean
train_y /= y_std
test_y -= y_mean
test_y /= y_std

print(train_x[0], train_y[0])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=52, activation='relu', input_shape=(13,)),
    tf.keras.layers.Dense(units=39, activation='relu'),
    tf.keras.layers.Dense(units=26, activation='relu'),
    tf.keras.layers.Dense(units=1)
    ])

model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.07),loss='mse')
model.summary()
# Deap learning 인공신경망 모델 설정
# node: 52개 -> 39개 -> 26개 -> 1개
# learning rate(학습률): 오차 수용 범위 (0.01~0.1)
# loss : 오차 계산 방법

history = model.fit(train_x,train_y, batch_size=32, epochs=25, validation_split=0.2)
# train data를 model에 입력, 로그 저장 (에러 발생 횟수)
# batch size : 입력 데이터를 한번에 보내는 set 개수 (default: 32개)
# epoch : 반복 회수
# validation_split: 입력 data 중 검증용으로 사용할 비율(0.2: 20%)
# val_loss : 검증용 data를 넣었을 때의 오차. fit option을 조정하여 최적의 값을 찾아감.



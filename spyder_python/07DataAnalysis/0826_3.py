# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 15:18:08 2021

@author: user9
"""

# tensorflow를 이용한 인공신경망 모델 
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



# Deap learning 인공신경망 모델 설정
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=52, activation='relu', input_shape=(13,)),
    tf.keras.layers.Dense(units=39, activation='relu'),
    tf.keras.layers.Dense(units=26, activation='relu'),
    tf.keras.layers.Dense(units=1)
    ])

model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.07),loss='mse')
model.summary()
# node(units): 52개 -> 39개 -> 26개 -> 1개(결과값)
# activation(활성함수)
# input_shape : 입력 개수 (train_x)
# optimizer: 오류 발생 시 model의 내부 조건을 어떻게 변경할 것인가.(가중치 갱신. Adam함수모델 사용)
# learning rate(학습률): 오차 수용 범위 (0.01~0.1) / 오차가 발생했을 때 node값의 변경 범위(커질수록 불안정해짐)
# loss : 오차 계산 방법 (mse: regression / sparse_categorical_crossentropy: 분류)
# metrics(분류 model에서만) = ['accuracy']


# train data를 model에 입력, 로그 저장 (에러 발생 횟수)
history = model.fit(train_x,train_y, batch_size=32, epochs=25, validation_split=0.2)
# batch size : 입력 데이터를 한번에 보내는 set 개수 (default: 32개)
# epoch : 반복 회수
# validation_split: 입력 data 중 검증용으로 사용할 비율(0.2: 20%)



# 시각화
# 오차 Graph
# loss: train data를 사용하였을 때의 오차
# val_loss : 검증용 data를 넣었을 때의 오차. fit option을 조정하여 최적의 값을 찾아감.
plt.plot(history.history['loss'],'b--',label='loss')
plt.plot(history.history['val_loss'],'r--',label='val_loss')
plt.xlabel('Epoch')
plt.legend()

plt.show()

# 테스트 데이터 test_x로 모델 평가
model.evaluate(test_x,test_y) 

# test_y / predict_y 비교 Graph
predict_y = model.predict(test_x)

plt.figure(figsize=(5,5))
plt.plot(test_y,predict_y,'b.')
plt.axis([min(test_y), max(test_y), min(test_y), max(test_y)]) # x/y 축 최대/최소값. 

plt.plot([min(test_y),max(test_y)],[min(test_y),max(test_y)], ls='--', c='r') # x=y , 45도로 기준line 설정

plt.show()
























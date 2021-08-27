# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 13:24:35 2021

@author: user9
"""

# Data를 불러와 DF로 Cleanung 후 인공신경망 모델 생성 (0826_3 + 0827_1)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf

# csv 파일 -> data frame으로 저장
red_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
white_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')

red_df['type'] = 0
white_df['type'] = 1

wine = pd.concat([red_df,white_df])

plt.hist(wine['type'])
plt.xticks([0,1])
plt.show()

# Data 졍규화 (0~1)
wine_nor = (wine-wine.min())/(wine.max()-wine.min()) 

# 비복원 추출(frac = 1: 100%추출). Data Shuffle for machine learning
wine_shuffle = wine_nor.sample(frac=1)

# Data 분리를 위해 numpy로 변환 (각 행마다 wine_np[i] 배열로 접근)
wine_np = wine_shuffle.to_numpy()

# 전체 Data 중 80%-train / 20%-test로 추출
# wine_np[row,column]로 cut.(':'으로 배열 범위 지정시 마지막 부분은 포함되지 않음)
train_idx = int(len(wine_np) *0.8)
train_x, train_y = wine_np[:train_idx, :-1], wine_np[:train_idx, -1] 
test_x, test_y = wine_np[train_idx:, :-1], wine_np[train_idx:, -1]
# print(train_x[0],'\n',train_y[0],'\n',test_x[0],'\n',test_y[0])

# machine learning modeling
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=48, activation='relu', input_shape=(12,)),
    tf.keras.layers.Dense(units=36, activation='relu'),
    tf.keras.layers.Dense(units=12, activation='relu'),
    tf.keras.layers.Dense(units=2, activation='softmax') # red/white 두개의 결과로 출력
    ])
model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.07),\
              loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.summary()

history = model.fit(train_x,train_y, batch_size=32, epochs=25, validation_split=0.2)

# Graph (Loss & Accuracy)
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(history.history['loss'],'b--', label='loss')
plt.plot(history.history['val_loss'],'r--', label='val_loss')
plt.xlabel('Epoch')
plt.legend()

plt.subplot(1,2,2)
plt.plot(history.history['accuracy'],'b--', label='accuracy')
plt.plot(history.history['val_accuracy'],'r--', label='val_accuracy')
plt.xlabel('Epoch')
plt.legend()

plt.show()

# Test data 입력시 결과
model.evaluate(test_x,test_y)














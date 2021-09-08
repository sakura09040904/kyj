# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 13:29:59 2021

@author: user9
"""

# boston Data set를 이용한 Linear Regression

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import seaborn as sns # interactive plot 제공, 내장 dataset 제공

boston = load_boston() # 데이터셋 다운로드
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names) # 데이터프레임으로 저장

print(boston_df.head()) # 독립변수(13개) - X data

boston_df['PRICE'] = boston.target

print(boston_df.head()) # 종속변수(가격) 추가 - Y data (13개의 X data로부터 영향을 받음)
print(boston_df.info())

Y = boston_df['PRICE']
X = boston_df.drop(['PRICE'],axis=1,inplace=False) # 13개의 독립변수 저장

# print(X)

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3) 
# 훈련 데이터셋과 테스트 데이터셋을 분리하여 저장

lr = LinearRegression() # 선형회귀모델 생성
lr.fit(x_train,y_train) # train Dataset 적용

y_predict = lr.predict(x_test) # 생성된 함수에 Test Dataset을 넣어서 결과를 예측
print(y_predict[0])

mse = mean_squared_error(y_test,y_predict) # 예측결과와 실제 결과의 오차(잔차)
rmse = np.sqrt(mse)

print(mse,rmse)
print(lr.coef_,lr.intercept_) # 기울기(13개 각각의 회귀계수)와 y절편

fig,axs = plt.subplots(figsize=(16,16), nrows=5, ncols=3)
x_feat = ['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT']

for i,feat in enumerate(x_feat): # enumerate(list) : 리스트로부터 index,value를 획득
    row = int(i/3)
    col = i%3
    sns.regplot(x=feat, y='PRICE', data=boston_df, ax=axs[row][col])
    


# 자동차 연비 선형회귀모델 생성(0826_2) + pearson상관계수와 heatmap

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression # 선형회귀 함수 사용
from sklearn.model_selection import train_test_split # 데이터 분리 (train/test)
from sklearn.metrics import mean_squared_error, r2_score # MSE /상관계수 사용 
import matplotlib.pyplot as plt
import seaborn as sns

data_df = pd.read_csv('C:/kyj/spyder_python/07DataAnalysis/auto_mpg.csv')


# .drop(axis=1) : column 삭제 (axis=0 row 삭제) / inplace: 변경 요소(False:없음)
data_df = data_df.drop(['car_name','origin','horsepower'], axis=1, inplace=False)

'''
print(data_df.head())
print(data_df.shape) # 행과 열의 개수 출력
print(data_df.info()) # .info(): 각 column별 data type 
print(data_df.describe()) # .describe(): 통계적 정보 (min,max,mean,std,count)
'''

Y = data_df['mpg'] # result (종속변수-연비)
X = data_df.drop(['mpg'], axis=1, inplace=False) # 독립변수

# 데이터 분리 (data shuffle 후 진행됨)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3) 

# 선형 회귀함수 생성
lr = LinearRegression()
lr.fit(X_train, Y_train)

# 함수에 test data를 넣어 predict data 생성
Y_predict = lr.predict(X_test)

# 실제 결과 data와 predict data를 비교하여 mse/rmse 추출 
mse = mean_squared_error(Y_test,Y_predict)
rmse = np.sqrt(mse)
print(mse, rmse)

# lr.coef_ : 각 변수에 대한 기울기(상관계수)/ lr.intercept_ : y 절편
print(lr.coef_, lr.intercept_)

# 기울기를 Series로 저장 / np.round(data,2) : 2자리수까지 data를 반올림. 
coef = pd.Series(data=np.round(lr.coef_,2), index=X.columns) 
print(coef)

# 임의의 값 넣어 예측    
result = lr.predict([[8,350,3200,22,99]])
print(result)

'''
# Graph ()
# regplot: scatter plot과 line plot을 함께 볼 수 있음 (lmplot: 여러개의 regplot)
fig, axs = plt.subplots(figsize=(16,16), nrows=2, ncols=3)
X_head = ['cylinders', 'displacement', 'weight', 'acceration', 'model_year']
color=['r','g','b','y','k']

for i,head in enumerate(X_head):
    row = int(i/3)
    col = i%3
    sns.regplot(x=head, y='mpg', data = data_df, ax=axs[row][col], color=color[i])
'''


# 피어슨 상관계수 (correlation)
df_corr = data_df.corr(method='pearson')
print(df_corr)
# df_corr.to_csv('C:/kyj/spyder_python/07DataAnalysis/df_corr.csv')


# pairplot : 각 column(변수)들의 모든 상관 관계를 출력
sns.pairplot(data_df, hue='mpg')
plt.show()

# heatmap
heatmap_data = data_df[['mpg','cylinders', 'displacement', 'weight', 'acceration', 'model_year']]
sns.heatmap(heatmap_data.astype(float).corr(), linewidths=0.1, annot=True)
plt.show()









    
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 11:32:03 2021

@author: user9
"""
# Data cleaning using pandas
# https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# csv 파일 -> data frame으로 저장
red_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep=';')
white_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv', sep=';')

# type 항목 추가 (red/white 입력)
red_df.insert(0,column='type',value='red') 
white_df.insert(0,column='type',value='white') 

# Data frame concat
wine = pd.concat([red_df,white_df])

# space bar -> under bar in columns
wine.columns = wine.columns.str.replace(' ','_')  

# data frame의 통계적 information 출력 (num, mean, std, min/max)
print(wine.describe())

# quality 항목의 중복되는 value
wine.quality.unique()
# quality 항목에서 중복되는 value의 개수를 내림차순으로 카운트
wine.quality.value_counts()

# type 으로 그룹을 지어 각 그룹마다 quality에 대한 describe()
wine.groupby('type')['quality'].describe()
wine.groupby('type')['quality'].mean()
wine.groupby('type')['quality'].std()

# type이 red인 경우 quality를 히스토그램으로 출력 (sns.displot() / plt.hist())
red_wine_quality = wine.loc[wine['type']=='red', 'quality']
white_wine_quality = wine.loc[wine['type']=='white', 'quality']

sns.distplot(red_wine_quality, kde=True, label='red wine')
sns.distplot(white_wine_quality, kde=True, label='white wine')
plt.title('Quality of wine')
plt.legend()
plt.show()

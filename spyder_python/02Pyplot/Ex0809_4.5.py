# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:20:18 2021

@author: user9
"""

#히스토그램

import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(10,3,20000) 
#평균 10, 표준편차 3, 개수 20000인 정규분포

plt.hist(data, bins=300, color = 'green')
# bin: 가로축 구간의 개수

plt.show()


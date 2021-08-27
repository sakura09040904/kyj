# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:27:44 2021

@author: user9
"""



import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0.0, 5.0) # 0.0~5.0 50개의 linear한 value 생성
x2 = np.linspace(0.0, 2.0)
y1 = np.cos(2*np.pi*x1)*np.exp(-x1) # dampling graph
y2 = np.cos(2*np.pi*x2) # cosine graph

plt.subplot(2,1,1)
plt.plot(x1,y1,'o-')
plt.subplot(2,1,2)
plt.plot(x2,y2,'r^--')

plt.show()

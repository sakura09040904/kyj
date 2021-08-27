# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 13:46:40 2021

@author: user9
"""

import matplotlib.pyplot as plt
import numpy as np

names = ['groupA', 'groupB', 'groupC']
values = [1,10,100]

plt.Figure(figsize=(9,3))

plt.subplot(1,3,1)
plt.bar(names,values)

plt.subplot(1,3,2)
plt.scatter(names,values)

plt.subplot(1,3,3)
plt.plot(names,values)

plt.show()
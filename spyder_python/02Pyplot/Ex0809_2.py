# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 11:20:15 2021

@author: user9
"""
# 데이터 시각화

import matplotlib.pyplot as plt
import numpy as np

# marker:.ov^<> / line:- -- -. : / color:rgblcmkw

"""
plt.plot([1,2,3,4],[1,4,9,16],'r^:')
plt.ylabel('number')
plt.axis([0,6,0,20]) #[x시작,x끝,y시작,y끝]

"""

# numpy를 활용 그래프
# range:정수 / arange:실수 (시작,끝,간격)
t = np.arange(0.0, 5.0, 0.2) 


"""

plt.plot(t,2*t,'r--',t,t**2,'b:')
plt.plot(t,t**3,'g-')

"""

# subplot

plt.figure(figsize=(9,3)) # 여러개의 plot (크기(행,열))

plt.subplot(1,3,1) # (1,3)의 첫번째
plt.plot(t,t,'r--')
plt.xlabel('y=x')


plt.subplot(1,3,2)
plt.plot(t,2*t,'g:')
plt.xlabel('y=2x')

plt.subplot(1,3,3)
plt.plot(t,t**2,'b-')
plt.xlabel('y=x**2')

plt.suptitle('Sub Plot Example')

plt.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 10:46:18 2021

@author: user9
"""
# conda install opencv (영상처리)

import cv2
import matplotlib.pyplot as plt

img1r = cv2.imread('C:/kyj/spyder_python/07DataAnalysis/image1_680448.jpg') # img read
img1 = cv2.cvtColor(img1r, cv2.COLOR_BGR2RGB) # Convert color (BGR-> RGB)
img2r = cv2.imread('C:/kyj/spyder_python/07DataAnalysis/image2_550364.jpg')
img2 = cv2.cvtColor(img2r, cv2.COLOR_BGR2RGB)

'''

plt.axis('off') # x/y축 눈금제거 (axis() 축설정)
plt.imshow(img1) # img 변수를 이용하여 화면 출력
plt.show()

'''

plt.subplot(121)
plt.axis('off')
plt.imshow(img1)

plt.subplot(122)
plt.axis('off')
plt.imshow(img2)

plt.show()
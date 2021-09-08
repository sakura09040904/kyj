# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 13:32:06 2021

@author: user9
"""


# Graph Drawing,CB box,Radio Button(0813_1) + open API data crolling(0812_3)

from bs4 import BeautifulSoup
import urllib.request as ulib
import urllib.parse as parse
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import font_manager, rc
import cv2

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
    
        self.initUI()        
        
    def initUI(self):       
        font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
        rc('font', family=font_name)
        
        self.img1r = cv2.imread('C:/kyj/spyder_python/07DataAnalysis/image1_680448.jpg')
        self.img2r = cv2.imread('C:/kyj/spyder_python/07DataAnalysis/image2_550364.jpg')
        self.img3r = cv2.imread('C:/kyj/spyder_python/07DataAnalysis/image3_650507.jpg')
        
# Widget영역

        # LineEdit & Button
        self.leArea = QLineEdit()
        self.btnFind = QPushButton('search', self)
        self.btnFind.clicked.connect(self.btnFindEvent)

        
        # Table
        self.tbl = QTableWidget(self)
        self.tbl.setColumnCount(4)
        self.tbl_col = ['Date','pm10', 'pm25','Ozon']
        self.tbl.setHorizontalHeaderLabels(self.tbl_col)
        
        # Radio button
        self.rbtn1 = QRadioButton("Graph type 1", self)
        self.rbtn2 = QRadioButton("Graph type 2", self)
        self.rbtn3 = QRadioButton("Graph type 3", self)
        self.rbtn1.clicked.connect(self.rbtnEvent)
        self.rbtn2.clicked.connect(self.rbtnEvent)
        self.rbtn3.clicked.connect(self.rbtnEvent)
        
        # Graph
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig) 

        
# Layout 영역
        
        layout1 = QHBoxLayout() 
        layout1.addWidget(self.leArea)
        layout1.addWidget(self.btnFind)
                       
        layout2 = QVBoxLayout() 
        layout2.addWidget(self.tbl)
        
        layout3 = QHBoxLayout()
        layout3.addWidget(self.rbtn1)
        layout3.addWidget(self.rbtn2)
        layout3.addWidget(self.rbtn3)
              
        layout4 = QVBoxLayout() 
        layout4.addWidget(self.canvas)
            
        layout = QVBoxLayout() 
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addLayout(layout4)
            
        layout.setStretchFactor(layout1, 1)
        layout.setStretchFactor(layout2, 1) 
        layout.setStretchFactor(layout3, 1) 
        layout.setStretchFactor(layout4, 1) 
            
        self.setLayout(layout)

# Window 영역            
        self.setWindowTitle('Graph Exam')
        self.setGeometry(50,50,1200,800)
        self.show()        
        
        
# 메서드 영역

# Search Button 
    def btnFindEvent(self):
        img1 = cv2.cvtColor(self.img1r, cv2.COLOR_BGR2RGB)
        
        self.fig.clear()
        
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.axis('off')
        self.ax1.imshow(img1)
        
        self.canvas.draw()

# Radio Button    

    def rbtnEvent(self):
        
        self.fig.clear()
        
        if self.rbtn1.isChecked() :
            self.draw1()
        elif self.rbtn2.isChecked() :
            self.draw2()
        elif self.rbtn3.isChecked() :
            self.draw3()    
            
        self.canvas.draw()                    

# Draw   
    # rbtn1       
    def draw1(self):
        img1 = cv2.cvtColor(self.img1r, cv2.COLOR_BGR2RGB)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        num = 100
        # numstr = 'Num:%d'% num # formatting
        numstr = '%d X %d'%(img1.shape[1], img1.shape[0]) # (.shape[0]:hight/.shape[1]:width)
        cv2.putText(img1, numstr, (10,40), font, 1.1, (255,0,0), 2) 
        cv2.putText(img1, 'Cat', (img1.shape[1]-100,img1.shape[0]-30), font, 1.5, (0,0,255), 3)

        self.ax1 = self.fig.add_subplot(111)
        self.ax1.axis('off')
        self.ax1.imshow(img1)
    
    # rbtn2    
    def draw2(self):       
        img1 = cv2.cvtColor(self.img1r, cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(self.img2r, cv2.COLOR_BGR2RGB)
        
        self.ax1 = self.fig.add_subplot(121)
        self.ax1.axis('off')
        self.ax1.imshow(img1)
        self.ax2 = self.fig.add_subplot(122)
        self.ax2.axis('off')
        self.ax2.imshow(img2)
        
    # rbtn3
    def draw3(self):
        img1 = cv2.cvtColor(self.img1r, cv2.COLOR_BGR2RGB)
        img2 = cv2.cvtColor(self.img2r, cv2.COLOR_BGR2RGB)
        img3 = cv2.cvtColor(self.img3r, cv2.COLOR_BGR2RGB)
        
        img1s = cv2.resize(img1, dsize=(380,300))
        img2s = cv2.resize(img2, dsize=(380,300))
        img3s = cv2.resize(img3, dsize=(380,300))
        
        self.ax1 = self.fig.add_subplot(131)
        self.ax1.axis('off')
        self.ax1.imshow(img1s)
        self.ax2 = self.fig.add_subplot(132)
        self.ax2.axis('off')
        self.ax2.imshow(img2s)
        self.ax3 = self.fig.add_subplot(133)
        self.ax3.axis('off')
        self.ax3.imshow(img3s)        
        
        
                
# Main 영역        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())
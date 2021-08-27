# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:32:20 2021

@author: user9
"""

# Layout, Figure를 이용한 Graph draw

import pymysql
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):        
            
            self.le1 = QLineEdit()

# Draw            
            self.fig = plt.Figure()
            
            ax1 = self.fig.add_subplot(221)
            data1 = [1,2,3,4]
            data2 = [1,4,9,16]
            ax1.plot(data1,data2)
            
            ax2 = self.fig.add_subplot(222)
            data1 = [1,2,3,4]
            data2 = [2,4,6,8]
            ax2.plot(data1,data2)
            
            ax3 = self.fig.add_subplot(223)
            data1 = [1,2,3,4]
            data2 = [1,8,27,64]
            ax3.plot(data1,data2)
            
            ax4 = self.fig.add_subplot(224)
            data1 = [1,2,3,4]
            data2 = [3,6,9,12]
            ax4.plot(data1,data2)            
            
            
            self.canvas = FigureCanvas(self.fig) 
            self.canvas.draw()
            
# Layout (윈도우 크기 변경 가능)          

            layout1 = QVBoxLayout() # Vertical Box Layout1. 캔버스 영역
            layout1.addWidget(self.canvas)
            
            
            layout2 = QVBoxLayout() # 2. Line Editor 영역
            layout2.addWidget(self.le1)
            
            layout = QHBoxLayout() # Horizontal Box Layout
            layout.addLayout(layout1)
            layout.addLayout(layout2)
            
            layout.setStretchFactor(layout1, 1) # 영역 크기 변경 가능여부 true
            layout.setStretchFactor(layout2, 0) # false
            
            self.setLayout(layout) # Window에 layout 설정
            
                        
            
# Window 영역            
            self.setWindowTitle('Graph Exam')
            self.setGeometry(50,50,1200,600)
            self.show()
                        
            
        
# Main 영역        
if __name__=='__main__':
    app = QApplication(sys.argv) 
    ex=MyApp() 
    sys.exit(app.exec_())                  
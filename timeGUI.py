#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon

class welcomePage(QMainWindow):
    

    close_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.initUI() 
        #界面绘制交给InitUi方法
        
        
    def initUI(self):  
        self.setWindowTitle('时光桥牌')
        #设置窗口的图标，引用当前目录下的time.png图片
        self.setWindowIcon(QIcon('time.png'))        
        self.setGeometry(300, 300, 600, 600) 
        
        self.btn = QToolButton(self)
        self.btn.setText("开始游戏")
        self.btn.resize(100, 60)
        self.btn.move(250, 400)
        self.show()
   
        
        

    def closeEvent(self, event):
        #是否确认退出
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class gamePage(QMainWindow):
    def __init__(self, parent=None):
        super(gamePage, self).__init__(parent)
        self.resize(800, 1000)
        self.setStyleSheet("background: black")

    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.close()
        
if __name__ == "__main__":
    App = QApplication(sys.argv)
    ex = welcomePage()
    s = gamePage()
    ex.btn.clicked.connect(s.handle_click)
    ex.btn.clicked.connect(ex.hide)
    ex.close_signal.connect(ex.close)
    ex.show()
    sys.exit(App.exec_())
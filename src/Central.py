#!/usr/bin/python3
#! -*- coding: utf-8 -*-
'''
Created on 4 févr. 2016

@author: ade
'''
import sys, graphics, Control
from PyQt5.QtWidgets import (QMainWindow, QApplication, QHBoxLayout,
                             QVBoxLayout, QPushButton, QWidget, QTextEdit)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class CentralWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self. initUI()
        
    def initUI(self):
        
        self.board = graphics.Board(self)
        
        #fboard = graphics.BoardFrontal(self)
        controller = Control.Controler(self)
        fboard = QTextEdit(self)
        fboard.resize(300,300)
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(fboard)
        vbox.addStretch(1)
        
        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        hbox.addWidget(controller)
        hbox.addStretch(1)
        
        
        self.setLayout(hbox)
        
        controller.checkAbc.toggled[bool].connect(self.board.setABC)
        controller.checkAlt.toggled[bool].connect(self.board.setAlt)
        controller.numFret.valueChanged[int].connect(self.board.setNumActiveFrets)
        controller.actionButton.clicked.connect(self.giveNote)
        
        self.setGeometry(300,300,300,200)
        #self.setMaximumSize(300, 200)
        self.setWindowTitle('CentralWidget')
        self.show()

    def giveNote(self):
        print(self.board.nameNote(*self.board.randNote()))
    
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CentralWidget()
    sys.exit(app.exec_())
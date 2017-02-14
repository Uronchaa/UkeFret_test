'''
Created on 17 févr. 2016

@author: ade
'''
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QFormLayout, QVBoxLayout,
                             QCheckBox, QSpinBox, QPushButton)
from PyQt5.QtCore import Qt


class Controler(QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self. initUI()
        
    def initUI(self):
        self.menu = QVBoxLayout(self)
        
        self.checkAbc = QCheckBox(self)
        self.checkAlt = QCheckBox(self)
        
        self.numFret = QSpinBox(self)
        self.numFret.setRange(0,21)
        self.numFret.setValue(10)
        #self.numFret.setAlignment(Qt.AlignCenter)
        self.numFret.setMaximumWidth(50)
        
        self.actionButton = QPushButton('Go', self)
        
        self.formlayout = QFormLayout(self)
        self.formlayout.addRow('Number of frets', self.numFret)
        self.formlayout.addRow('A B C... ', self.checkAbc)
        self.formlayout.addRow('Alterations', self.checkAlt)
        self.formlayout.addRow('',self.actionButton)
        
        self.menu.addStretch(1)
        self.menu.addLayout(self.formlayout)
        self.menu.addStretch(1)
        self.setLayout(self.menu)
        
        self.setMinimumSize(200, 100)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Controler()
    ex.show()
    sys.exit(app.exec_())
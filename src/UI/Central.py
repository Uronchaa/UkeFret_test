#!/usr/bin/python3
# ! -*- coding: utf-8 -*-
"""
Created on 4 févr. 2016

@author: ade
"""
import sys
from src.UI.control_wgt import *
from src.UI import Control
from src.base import main
from PyQt5.QtWidgets import (QMainWindow, QApplication, QHBoxLayout,
                             QVBoxLayout, QPushButton, QWidget, QTextEdit)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.board = main.Board()

        # fboard = graphics.BoardFrontal(self)
        controller = Controller()
        fboard = QTextEdit(self)
        fboard.resize(300, 300)

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

        self.setGeometry(300, 300, 300, 200)
        # self.setMaximumSize(300, 200)
        self.setWindowTitle('CentralWidget')
        self.show()

    def giveNote(self):
        print(self.board.nameNote(*self.board.randNote()))


class Controller(QWidget, Ui_Control_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CentralWidget()
    ex.show()
    sys.exit(app.exec_())
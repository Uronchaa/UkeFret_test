#!/usr/bin/python3
# ! -*- coding: utf-8 -*-
"""
Created on 4 févr. 2016

@author: ade
"""
import sys
from src.UI.control_wgt import *
from src.UI import fretbd_wgt
from src.base import fretbd
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QVBoxLayout, QWidget)


# TODO : Add main window

class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.board = fretbd.Board()

        self.fboard = fretbd_wgt.Board_wgt(self)
        controller = Controller()
        self.fboard.resize(300, 300)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.fboard)
        vbox.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addStretch(1)
        hbox.addWidget(controller)
        hbox.addStretch(1)

        self.setLayout(hbox)

        # setup signal / slots for control box
        controller.checkAbc.toggled[bool].connect(self.setABC)
        controller.checkAlt.toggled[bool].connect(self.setAlt)
        controller.numFret.valueChanged[int].connect(self.setNumActiveFrets)
        controller.actionButton.clicked.connect(self.giveNote)

        # Send default values to control box widget
        controller.numFret.setValue(self.board.numActiveFrets)
        controller.checkAbc.setChecked(self.board.isABC)
        controller.checkAlt.setChecked(self.board.hasAlt)

        self.setGeometry(300, 300, 300, 200)
        # self.setMaximumSize(300, 200)
        self.setWindowTitle('CentralWidget')
        self.show()

    def giveNote(self):
        print(self.board.nameNote(*self.board.randNote()))

    def setABC(self, isABC):
        self.board.setABC(isABC)
        self.fboard.repaint()

    def setAlt(self, hasAlt):
        self.board.setAlt(hasAlt)
        self.fboard.repaint()

    def setNumActiveFrets(self, i):
        self.board.setNumActiveFrets(i)
        self.fboard.numInactive = i
        self.fboard.repaint()


class Controller(QWidget, Ui_Control_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CentralWidget()
    ex.show()
    sys.exit(app.exec_())
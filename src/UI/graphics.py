# -*- coding: utf-8 -*-
"""
Created on 4 févr. 2016

@author: ade
"""
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


# TODO: add visual indication of number of active frets

class BoardFrontal(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.width = 150
        self.length = 500
        self.setMinimumSize(self.length + 1, self.width + 1)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        qp.setPen(col)

        qp.setBrush(QColor(128, 64, 0))
        qp.drawRect(0, 0, self.length, self.width)

        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        for i in range(1, 4):
            qp.drawLine(0, i * self.width / 4, self.length, i * self.width / 4)

        qp.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        for i in range(1, 20):
            qp.drawLine(i * self.length / 20, 0, i * self.length / 20, self.width)

    def drawInactive(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BoardFrontal()
    ex.show()
    # a = Board()
    # a.randNote()
    sys.exit(app.exec_())

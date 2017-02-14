
# -*- coding: utf-8 -*-
'''
Created on 4 févr. 2016

@author: ade
'''
import sys,random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

class BoardFrontal(QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        self. initUI()
        
    def initUI(self):
        self.width = 150
        self.length = 500
        self.setMinimumSize(self.length + 1 , self.width + 1)
        
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self, qp):
        col = QColor(0,0,0)
        qp.setPen(col)
        
        qp.setBrush(QColor('brown'))
        qp.drawRect(0,0,self.length,self.width)
        
        pen = QPen(Qt.black, 2, Qt.SolidLine)
        qp.setPen(pen)
        for i in range(1,4):
            qp.drawLine(0,i*self.width/4,self.length,i*self.width/4)
        
        qp.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        for i in range(1,20):
            qp.drawLine(i*self.length/20,0,i*self.length/20,self.width)
        
    def drawInactive(self):
        pass
        
class Board(QWidget):
    
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.numActiveFrets =  12
        self.isABC = True
        self.hasAlt = False
        self.altNotes = [1,3,6,8,10,13,15,18,20]
        self.notes = []
        
        self.setABC(False)
        self.tuning = self.setTuning('gCEA')
        
        
    def setABC(self,isABC):
        """
        setABC(bool)
        True -> A,B,C.. notation
        False -> DO,RE,MI.. notation
        """
        if isABC:
            print('is ABC!')
            self.notes = ['C', '#/♭', 'D',  '#/♭','E', 'F', '#/♭', 'G', '#/♭',
                    'A', '#/♭', 'B', 'C', '#/♭', 'D',  '#/♭', 'E', 'F',
                    '#/♭', 'G', '#/♭', 'A']
        else:
            print('is not ABC!')
            self.notes =  ['DO', '#/♭', 'RE',  '#/♭','MI', 'FA', '#/♭', 'SOL', '#/♭',
                    'LA', '#/♭', 'SI', 'DO', '#/♭', 'RE',  '#/♭','MI', 'FA',
                    '#/♭', 'SOL', '#/♭', 'LA']
    
    def setTuning(self,i):
        tuning = {'gCEA':[7,0,5,9], 'aDF#B':[9,2,6,11], 'dGBE':[2,7,11,5]}
        return tuning[i]
    
    def setAlt(self, hasAlt):
        self.hasAlt = hasAlt
        print('alteration set to: %s' % self.hasAlt)
        
    def setNumActiveFrets(self,i):
        self.numActiveFrets = i
        print('Active frets set to: %s' % self.numActiveFrets)
    
    def nameNote(self,string,fret):
        return self.notes[self.tuning[string-1]+fret]
    
    def randNote(self):
        s = random.randint(1,4)
        f = random.randint(0,self.numActiveFrets)
        if not self.hasAlt:
            while (self.tuning[s-1]+f) in self.altNotes:
                s = random.randint(1,4)
                f = random.randint(0,self.numActiveFrets)
        return s,f
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BoardFrontal()
    ex.show()
    a = Board()
    a.randNote()
    sys.exit(app.exec_())
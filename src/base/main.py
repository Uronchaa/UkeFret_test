# -*- coding: utf-8 -*-
"""
Created on 25 mar. 2017

@author: ade
"""

from PyQt5.QtWidgets import QWidget
import random


class Board:
    def __init__(self):

        self.numActiveFrets = 12
        self.isABC = True
        self.hasAlt = False
        self.altNotes = [1, 3, 6, 8, 10, 13, 15, 18, 20]
        self.notes = []

        self.setABC(False)
        self.tuning = self.setTuning('gCEA')

    def setABC(self, isABC):
        """
        setABC(bool)
        True -> A,B,C.. notation
        False -> DO,RE,MI.. notation
        """
        if isABC:
            print('is ABC!')
            self.notes = ['C', '#/♭', 'D', '#/♭', 'E', 'F', '#/♭', 'G', '#/♭',
                          'A', '#/♭', 'B', 'C', '#/♭', 'D', '#/♭', 'E', 'F',
                          '#/♭', 'G', '#/♭', 'A']
        else:
            print('is not ABC!')
            self.notes = ['DO', '#/♭', 'RE', '#/♭', 'MI', 'FA', '#/♭', 'SOL', '#/♭',
                          'LA', '#/♭', 'SI', 'DO', '#/♭', 'RE', '#/♭', 'MI', 'FA',
                          '#/♭', 'SOL', '#/♭', 'LA']

    def setTuning(self, i):
        tuning = {'gCEA': [7, 0, 5, 9], 'aDF#B': [9, 2, 6, 11], 'dGBE': [2, 7, 11, 5]}
        return tuning[i]

    def setAlt(self, hasAlt):
        self.hasAlt = hasAlt
        print('alteration set to: %s' % self.hasAlt)

    def setNumActiveFrets(self, i):
        self.numActiveFrets = i
        print('Active frets set to: %s' % self.numActiveFrets)

    def nameNote(self, string, fret):
        return self.notes[self.tuning[string - 1] + fret]

    def randNote(self):
        s = random.randint(1, 4)
        f = random.randint(0, self.numActiveFrets)
        if not self.hasAlt:
            while (self.tuning[s - 1] + f) in self.altNotes:
                s = random.randint(1, 4)
                f = random.randint(0, self.numActiveFrets)
        return s, f

if __name__ == '__main__':
    a = Board()
    a.randNote()
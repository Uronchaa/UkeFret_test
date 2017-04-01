# -*- coding: utf-8 -*-
"""
Created on 25 mar. 2017

@author: ade
"""

import sys
from PyQt5.QtWidgets import QApplication
from src.UI import graphics
from src.base import main

app = QApplication(sys.argv)
ex = graphics.BoardFrontal()
ex.show()
a = main.Board()
a.randNote()
sys.exit(app.exec_())
# TODO: rewrite launcher for main program

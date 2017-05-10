# -*- coding: utf-8 -*-
"""
Created on 25 mar. 2017

@author: ade
"""

import sys
from PyQt5.QtWidgets import QApplication
from src.UI import fretbd_wgt
from src.base import fretbd

app = QApplication(sys.argv)
ex = fretbd_wgt.Board_wgt()
ex.show()
a = fretbd.Board()
a.randNote()
sys.exit(app.exec_())
# TODO: rewrite launcher for main program

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control_wgt.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Control_widget(object):
    def setupUi(self, Control_widget):
        Control_widget.setObjectName("Control_widget")
        Control_widget.resize(180, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Control_widget.sizePolicy().hasHeightForWidth())
        Control_widget.setSizePolicy(sizePolicy)
        Control_widget.setMinimumSize(QtCore.QSize(180, 120))
        self.formLayoutWidget = QtWidgets.QWidget(Control_widget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 181, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(8)
        self.formLayout.setObjectName("formLayout")
        self.Fret_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.Fret_label.setObjectName("Fret_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Fret_label)
        self.Eng_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.Eng_label.setObjectName("Eng_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Eng_label)
        self.Alt_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.Alt_label.setObjectName("Alt_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Alt_label)
        self.checkAlt = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkAlt.setText("")
        self.checkAlt.setObjectName("checkAlt")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkAlt)
        self.checkAbc = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkAbc.setObjectName("checkAbc")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkAbc)
        self.numFret = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.numFret.setObjectName("numFret")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.numFret)
        self.actionButton = QtWidgets.QPushButton(Control_widget)
        self.actionButton.setGeometry(QtCore.QRect(60, 80, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionButton.sizePolicy().hasHeightForWidth())
        self.actionButton.setSizePolicy(sizePolicy)
        self.actionButton.setObjectName("actionButton")

        self.retranslateUi(Control_widget)
        QtCore.QMetaObject.connectSlotsByName(Control_widget)

    def retranslateUi(self, Control_widget):
        _translate = QtCore.QCoreApplication.translate
        Control_widget.setWindowTitle(_translate("Control_widget", "Form"))
        self.Fret_label.setText(_translate("Control_widget", "Number of frets "))
        self.Eng_label.setText(_translate("Control_widget", "English notation"))
        self.Alt_label.setText(_translate("Control_widget", "Alterations"))
        self.actionButton.setText(_translate("Control_widget", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Control_widget = QtWidgets.QWidget()
    ui = Ui_Control_widget()
    ui.setupUi(Control_widget)
    Control_widget.show()
    sys.exit(app.exec_())


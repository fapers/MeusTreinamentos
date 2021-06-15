# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calend.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(463, 318)
        self.calendario = QCalendarWidget(Form)
        self.calendario.setObjectName(u"calendario")
        self.calendario.setGeometry(QRect(70, 40, 312, 183))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 240, 401, 41))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Calend\u00e1rio", None))
        self.label.setText(QCoreApplication.translate("Form", u"Data selecionada: ", None))
    # retranslateUi


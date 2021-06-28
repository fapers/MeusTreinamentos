# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela2.ui'
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
        Form.resize(400, 300)
        Form.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 331, 131))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.btnVoltar = QPushButton(Form)
        self.btnVoltar.setObjectName(u"btnVoltar")
        self.btnVoltar.setGeometry(QRect(150, 210, 121, 51))
        font1 = QFont()
        font1.setPointSize(16)
        self.btnVoltar.setFont(font1)
        self.btnVoltar.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Esta \u00e9 a segunda tela", None))
        self.btnVoltar.setText(QCoreApplication.translate("Form", u"Voltar", None))
    # retranslateUi


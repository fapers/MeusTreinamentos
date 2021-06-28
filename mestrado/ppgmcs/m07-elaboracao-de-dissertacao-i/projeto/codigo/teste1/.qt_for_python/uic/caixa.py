# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'caixa.ui'
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
        Form.resize(382, 518)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 400, 101, 41))
        font = QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(70, 130, 241, 41))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.lineEdit.setFont(font1)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 80, 241, 31))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        self.label.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Verificar", None))
        self.label.setText(QCoreApplication.translate("Form", u"Digite algum nome:", None))
    # retranslateUi


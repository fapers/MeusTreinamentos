# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame.ui'
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
        Form.resize(721, 493)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 150, 701, 331))
        self.frame.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.botao1 = QPushButton(self.frame)
        self.botao1.setObjectName(u"botao1")
        self.botao1.setGeometry(QRect(80, 160, 111, 41))
        self.botao1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label1 = QLabel(self.frame)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(350, 60, 191, 41))
        font = QFont()
        font.setPointSize(16)
        self.label1.setFont(font)
        self.btnFrame1 = QPushButton(Form)
        self.btnFrame1.setObjectName(u"btnFrame1")
        self.btnFrame1.setGeometry(QRect(60, 40, 101, 41))
        self.btnFrame1.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.btnFrame2 = QPushButton(Form)
        self.btnFrame2.setObjectName(u"btnFrame2")
        self.btnFrame2.setGeometry(QRect(520, 40, 101, 41))
        self.btnFrame2.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 150, 701, 331))
        self.frame_2.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 40, 191, 71))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.botao1.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label1.setText(QCoreApplication.translate("Form", u"Frame 1", None))
        self.btnFrame1.setText(QCoreApplication.translate("Form", u"Frame 1", None))
        self.btnFrame2.setText(QCoreApplication.translate("Form", u"Frame 2", None))
        self.label.setText(QCoreApplication.translate("Form", u"Frame 2", None))
    # retranslateUi


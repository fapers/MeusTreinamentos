# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulario.ui'
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
        Form.resize(504, 633)
        Form.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 140, 341, 51))
        font = QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(46, 93, 140);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"background-color:rgb(170,255,255)")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 100, 341, 31))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 220, 341, 31))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 340, 341, 31))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 260, 341, 51))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(46, 93, 140);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"background-color:rgb(170,255,255)")
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 380, 341, 51))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(u"border-radius:15px;\n"
"color: rgb(46, 93, 140);\n"
"border-style:outset;\n"
"border-width:4px;\n"
"background-color:rgb(170,255,255)")
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 490, 191, 91))
        font2 = QFont()
        font2.setPointSize(20)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:4px;\n"
"border-color:black;\n"
"background-color:rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:4px;\n"
"border-color:gray;\n"
"background-color:rgb(85, 255, 200);\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"background-color:rgb(85, 255, 127);\n"
"}")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 30, 401, 41))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(0, 127, 127);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_debug = QLabel(Form)
        self.label_debug.setObjectName(u"label_debug")
        self.label_debug.setGeometry(QRect(100, 600, 291, 16))
        self.label_debug.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 490, 191, 91))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:4px;\n"
"border-color:black;\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:4px;\n"
"border-color:gray;\n"
"background-color: rgb(85, 200, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:white;\n"
"background-color: rgb(85, 170, 255);\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Fomul\u00e1rio de Cadastro com SQLite", None))
        self.label.setText(QCoreApplication.translate("Form", u"Nome", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Endere\u00e7o", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Email", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"ENVIAR", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Formul\u00e1rio de cadastro com SQLite", None))
        self.label_debug.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"CONSULTAR", None))
    # retranslateUi


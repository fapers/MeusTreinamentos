# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(385, 494)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 50, 255), stop:1 rgba(89, 150, 244, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 440, 351, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 40, 341, 51))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(100, 110, 191, 41))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.radioButton.setFont(font2)
        self.radioButton.setStyleSheet(u"background-color: rgba(255, 255, 255, 10);")
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(100, 160, 191, 41))
        self.radioButton_2.setFont(font2)
        self.radioButton_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 10);")
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(100, 210, 191, 41))
        self.radioButton_3.setFont(font2)
        self.radioButton_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 10);")
        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(100, 260, 191, 41))
        self.radioButton_4.setFont(font2)
        self.radioButton_4.setStyleSheet(u"border:0px solid;\n"
"color: rgb(255, 0, 0);\n"
"background-color: rgba(255, 255, 255,10);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 340, 101, 51))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Cor selecionada:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Selecione uma cor", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
    # retranslateUi


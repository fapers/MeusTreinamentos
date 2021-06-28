# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela1.ui'
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
        MainWindow.resize(483, 301)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn1 = QPushButton(self.centralwidget)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(50, 100, 391, 141))
        font = QFont()
        font.setPointSize(36)
        self.btn1.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 30, 381, 51))
        font1 = QFont()
        font1.setPointSize(16)
        self.label.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 483, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn1.setText(QCoreApplication.translate("MainWindow", u"Segunda Tela", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tela Principal", None))
    # retranslateUi


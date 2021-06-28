# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
        MainWindow.resize(601, 327)
        self.actionVerde = QAction(MainWindow)
        self.actionVerde.setObjectName(u"actionVerde")
        self.actionVermelho = QAction(MainWindow)
        self.actionVermelho.setObjectName(u"actionVermelho")
        self.actionAzul = QAction(MainWindow)
        self.actionAzul.setObjectName(u"actionAzul")
        self.actionPreto = QAction(MainWindow)
        self.actionPreto.setObjectName(u"actionPreto")
        self.actionBranco = QAction(MainWindow)
        self.actionBranco.setObjectName(u"actionBranco")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 90, 461, 51))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 170, 391, 51))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(244, 244, 244);")
        self.label_2.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 601, 21))
        self.menuCores = QMenu(self.menubar)
        self.menuCores.setObjectName(u"menuCores")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuCores.menuAction())
        self.menuCores.addAction(self.actionVerde)
        self.menuCores.addAction(self.actionVermelho)
        self.menuCores.addAction(self.actionAzul)
        self.menuCores.addSeparator()
        self.menuCores.addAction(self.actionPreto)
        self.menuCores.addAction(self.actionBranco)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionVerde.setText(QCoreApplication.translate("MainWindow", u"Verde", None))
        self.actionVermelho.setText(QCoreApplication.translate("MainWindow", u"Vermelho", None))
        self.actionAzul.setText(QCoreApplication.translate("MainWindow", u"Azul", None))
        self.actionPreto.setText(QCoreApplication.translate("MainWindow", u"Preto", None))
        self.actionBranco.setText(QCoreApplication.translate("MainWindow", u"Branco", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Op\u00e7\u00e3o selecionada no menu:", None))
        self.label_2.setText("")
        self.menuCores.setTitle(QCoreApplication.translate("MainWindow", u"Cores", None))
    # retranslateUi


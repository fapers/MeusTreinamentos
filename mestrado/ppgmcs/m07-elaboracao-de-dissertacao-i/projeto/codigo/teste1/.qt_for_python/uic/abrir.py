# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'abrir.ui'
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
        MainWindow.resize(480, 333)
        self.actionSalvar = QAction(MainWindow)
        self.actionSalvar.setObjectName(u"actionSalvar")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 10, 441, 151))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_3 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 200, 441, 91))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_4.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 21))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menuArquivo.addAction(self.actionSalvar)
        self.menuArquivo.addAction(self.actionAbrir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Idade:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.label_4.setText("")
        self.menuArquivo.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
    # retranslateUi


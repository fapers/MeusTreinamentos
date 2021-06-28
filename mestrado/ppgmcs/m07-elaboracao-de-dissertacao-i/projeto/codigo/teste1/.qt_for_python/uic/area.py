# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'area.ui'
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
        Form.setWindowModality(Qt.ApplicationModal)
        Form.resize(800, 540)
        Form.setMinimumSize(QSize(800, 540))
        Form.setMaximumSize(QSize(800, 540))
        Form.setStyleSheet(u"background-color: rgb(27, 30, 35);")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_cadastro = QFrame(Form)
        self.frame_cadastro.setObjectName(u"frame_cadastro")
        self.frame_cadastro.setMinimumSize(QSize(780, 515))
        self.frame_cadastro.setMaximumSize(QSize(780, 515))
        self.frame_cadastro.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.frame_cadastro.setFrameShape(QFrame.StyledPanel)
        self.frame_cadastro.setFrameShadow(QFrame.Raised)
        self.label_titulo = QLabel(self.frame_cadastro)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(77, 30, 461, 33))
        font = QFont()
        font.setPointSize(20)
        self.label_titulo.setFont(font)
        self.label_titulo.setStyleSheet(u"color: rgb(220, 225, 236);")
        self.label_titulo.setAlignment(Qt.AlignCenter)
        self.btnSalvar = QPushButton(self.frame_cadastro)
        self.btnSalvar.setObjectName(u"btnSalvar")
        self.btnSalvar.setGeometry(QRect(590, 420, 120, 40))
        self.btnSalvar.setMinimumSize(QSize(120, 40))
        self.btnSalvar.setMaximumSize(QSize(120, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.btnSalvar.setFont(font1)
        self.btnSalvar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(85, 170, 127);\n"
"border:0px solid;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-color:gray;\n"
"background-color: rgb(85, 200, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-color:white;\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnAlterar = QPushButton(self.frame_cadastro)
        self.btnAlterar.setObjectName(u"btnAlterar")
        self.btnAlterar.setGeometry(QRect(590, 200, 120, 40))
        self.btnAlterar.setMinimumSize(QSize(120, 40))
        self.btnAlterar.setMaximumSize(QSize(120, 40))
        self.btnAlterar.setFont(font1)
        self.btnAlterar.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"border:0px solid;\n"
"	background-color: rgb(255, 255, 127);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-color:gray;\n"
"background-color: rgb(85, 200, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-color:white;\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnExcluir = QPushButton(self.frame_cadastro)
        self.btnExcluir.setObjectName(u"btnExcluir")
        self.btnExcluir.setGeometry(QRect(590, 250, 120, 40))
        self.btnExcluir.setMinimumSize(QSize(120, 40))
        self.btnExcluir.setMaximumSize(QSize(120, 40))
        self.btnExcluir.setFont(font1)
        self.btnExcluir.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"border:0px solid;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-color:gray;\n"
"background-color: rgb(85, 200, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-color:white;\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.label_2 = QLabel(self.frame_cadastro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 410, 76, 46))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(220, 225, 236);")
        self.lineEdit = QLineEdit(self.frame_cadastro)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 420, 401, 30))
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setMaximumSize(QSize(16777215, 30))
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"color: rgb(86, 138, 242);\n"
"border:0px solid;\n"
"border-radius:15px;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.btnListar = QPushButton(self.frame_cadastro)
        self.btnListar.setObjectName(u"btnListar")
        self.btnListar.setGeometry(QRect(590, 100, 120, 40))
        self.btnListar.setMinimumSize(QSize(120, 40))
        self.btnListar.setMaximumSize(QSize(120, 40))
        self.btnListar.setFont(font1)
        self.btnListar.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"border:0px solid;\n"
"	background-color: rgb(85, 85, 255);\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-color:gray;\n"
"background-color: rgb(85, 200, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"border-radius:15px;\n"
"border-style:outset;\n"
"border-width:1px;\n"
"border-color:white;\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.tableWidget = QTableWidget(self.frame_cadastro)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 80, 470, 300))
        self.tableWidget.setMinimumSize(QSize(470, 300))
        self.tableWidget.setMaximumSize(QSize(470, 300))
        self.tableWidget.setStyleSheet(u"color: rgb(86, 138, 242);\n"
"border:0px solid;\n"
"background-color: rgb(44, 49, 60);")
        self.tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(30)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)

        self.gridLayout.addWidget(self.frame_cadastro, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u00c1rea de Conhecimento", None))
        self.label_titulo.setText(QCoreApplication.translate("Form", u"\u00c1rea de Conhecimento", None))
        self.btnSalvar.setText(QCoreApplication.translate("Form", u"Salvar", None))
        self.btnAlterar.setText(QCoreApplication.translate("Form", u"Alterar", None))
        self.btnExcluir.setText(QCoreApplication.translate("Form", u"Excluir", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Descri\u00e7\u00e3o:", None))
        self.btnListar.setText(QCoreApplication.translate("Form", u"Listar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"DESCRI\u00c7\u00c3O", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"STATUS", None));
    # retranslateUi


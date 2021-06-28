# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check.ui'
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
        Form.resize(479, 390)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 130, 101, 41))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 300, 201, 41))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(260, 50, 171, 241))
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 40, 70, 17))
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(20, 80, 70, 17))
        self.checkBox_3 = QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(20, 120, 70, 17))
        self.checkBox_4 = QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(20, 160, 70, 17))
        self.checkBox_5 = QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(20, 200, 70, 17))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Calcular CheckBox", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Calcular", None))
        self.label.setText(QCoreApplication.translate("Form", u"Valor Total: ", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Pre\u00e7os", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"15,00", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"20,00", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"10,00", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"32,00", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"5,50", None))
    # retranslateUi


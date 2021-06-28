# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import source_rc

class Ui_form_principal(object):
    def setupUi(self, form_principal):
        if not form_principal.objectName():
            form_principal.setObjectName(u"form_principal")
        form_principal.setWindowModality(Qt.NonModal)
        form_principal.resize(1000, 650)
        form_principal.setMinimumSize(QSize(1000, 650))
        form_principal.setMaximumSize(QSize(1000, 650))
        font = QFont()
        font.setPointSize(12)
        form_principal.setFont(font)
        form_principal.setStyleSheet(u"background-color: rgb(27, 30, 35);")
        self.verticalLayout = QVBoxLayout(form_principal)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.div1_2 = QWidget(form_principal)
        self.div1_2.setObjectName(u"div1_2")
        self.div1_2.setMinimumSize(QSize(0, 50))
        self.div1_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.div1_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.div1_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(60, 50))
        self.widget.setMaximumSize(QSize(60, 50))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.w_menu = QWidget(self.widget)
        self.w_menu.setObjectName(u"w_menu")
        self.w_menu.setMinimumSize(QSize(60, 50))
        self.w_menu.setMaximumSize(QSize(256, 50))
        self.w_menu.setStyleSheet(u"background-color: rgb(27, 30, 35);")
        self.gridLayout_2 = QGridLayout(self.w_menu)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblMenu = QLabel(self.w_menu)
        self.lblMenu.setObjectName(u"lblMenu")
        font1 = QFont()
        font1.setPointSize(14)
        self.lblMenu.setFont(font1)
        self.lblMenu.setStyleSheet(u"color: rgb(195, 204, 223);")
        self.lblMenu.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblMenu, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.w_menu, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(self.div1_2)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.w_barra_titulo = QWidget(self.widget_2)
        self.w_barra_titulo.setObjectName(u"w_barra_titulo")
        self.w_barra_titulo.setMinimumSize(QSize(0, 25))
        self.w_barra_titulo.setMaximumSize(QSize(16777215, 25))
        self.w_barra_titulo.setStyleSheet(u"background-color: rgb(30, 34, 41);")
        self.horizontalLayout_2 = QHBoxLayout(self.w_barra_titulo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.titulo = QLabel(self.w_barra_titulo)
        self.titulo.setObjectName(u"titulo")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.titulo.setFont(font2)
        self.titulo.setStyleSheet(u"color: rgb(220, 225, 236);")

        self.horizontalLayout_2.addWidget(self.titulo)

        self.botoes = QFrame(self.w_barra_titulo)
        self.botoes.setObjectName(u"botoes")
        self.botoes.setMinimumSize(QSize(100, 0))
        self.botoes.setMaximumSize(QSize(100, 16777215))
        self.botoes.setFrameShape(QFrame.StyledPanel)
        self.botoes.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.botoes)


        self.verticalLayout_2.addWidget(self.w_barra_titulo)

        self.w_barra_url = QWidget(self.widget_2)
        self.w_barra_url.setObjectName(u"w_barra_url")
        self.w_barra_url.setMinimumSize(QSize(0, 25))
        self.w_barra_url.setMaximumSize(QSize(16777215, 25))
        self.w_barra_url.setStyleSheet(u"background-color: rgb(44, 49, 60);\n"
"border-radius:10px;\n"
"border-width:1px;")
        self.gridLayout_3 = QGridLayout(self.w_barra_url)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 0, 0, 0)
        self.lblStatus = QLabel(self.w_barra_url)
        self.lblStatus.setObjectName(u"lblStatus")
        self.lblStatus.setStyleSheet(u"color: rgb(138, 149, 170);\n"
"border:0px solid;")
        self.lblStatus.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.lblStatus, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.w_barra_url)


        self.horizontalLayout_3.addWidget(self.widget_2)


        self.verticalLayout.addWidget(self.div1_2)

        self.div2_2 = QWidget(form_principal)
        self.div2_2.setObjectName(u"div2_2")
        self.horizontalLayout_4 = QHBoxLayout(self.div2_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.w_menu_lateral = QWidget(self.div2_2)
        self.w_menu_lateral.setObjectName(u"w_menu_lateral")
        self.w_menu_lateral.setMinimumSize(QSize(200, 520))
        self.w_menu_lateral.setMaximumSize(QSize(256, 16777215))
        self.w_menu_lateral.setStyleSheet(u"background-color: rgb(27, 30, 35);")
        self.verticalLayout_4 = QVBoxLayout(self.w_menu_lateral)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.w_menu_lateral)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame_2)

        self.btnGerar = QPushButton(self.w_menu_lateral)
        self.btnGerar.setObjectName(u"btnGerar")
        self.btnGerar.setMinimumSize(QSize(160, 50))
        self.btnGerar.setFont(font)
        self.btnGerar.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"	background-color: rgb(44, 49, 60);\n"
"	color: rgb(86, 138, 242);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(52, 59, 72);\n"
"	color: rgb(86, 138, 242);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(52, 52, 52);\n"
"}")
        self.btnGerar.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btnGerar)

        self.btnTurmas = QPushButton(self.w_menu_lateral)
        self.btnTurmas.setObjectName(u"btnTurmas")
        self.btnTurmas.setMinimumSize(QSize(160, 50))
        self.btnTurmas.setFont(font)
        self.btnTurmas.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"	background-color: rgb(27, 30, 35);\n"
"color: rgb(195, 204, 223);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(86, 138, 242);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(52, 52, 52);\n"
"}")
        self.btnTurmas.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btnTurmas)

        self.btnProfessores = QPushButton(self.w_menu_lateral)
        self.btnProfessores.setObjectName(u"btnProfessores")
        self.btnProfessores.setMinimumSize(QSize(160, 50))
        self.btnProfessores.setFont(font)
        self.btnProfessores.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"	background-color: rgb(27, 30, 35);\n"
"color: rgb(195, 204, 223);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(86, 138, 242);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(52, 52, 52);\n"
"}")
        self.btnProfessores.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btnProfessores)

        self.btnDisponibilidades = QPushButton(self.w_menu_lateral)
        self.btnDisponibilidades.setObjectName(u"btnDisponibilidades")
        self.btnDisponibilidades.setMinimumSize(QSize(160, 50))
        self.btnDisponibilidades.setFont(font)
        self.btnDisponibilidades.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"	background-color: rgb(27, 30, 35);\n"
"color: rgb(195, 204, 223);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(86, 138, 242);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(52, 52, 52);\n"
"}")
        self.btnDisponibilidades.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btnDisponibilidades)

        self.btnCargaHoraria = QPushButton(self.w_menu_lateral)
        self.btnCargaHoraria.setObjectName(u"btnCargaHoraria")
        self.btnCargaHoraria.setMinimumSize(QSize(160, 50))
        self.btnCargaHoraria.setFont(font)
        self.btnCargaHoraria.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"	background-color: rgb(27, 30, 35);\n"
"color: rgb(195, 204, 223);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(86, 138, 242);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(52, 52, 52);\n"
"}")
        self.btnCargaHoraria.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btnCargaHoraria)

        self.btnArea = QPushButton(self.w_menu_lateral)
        self.btnArea.setObjectName(u"btnArea")
        self.btnArea.setMinimumSize(QSize(160, 50))
        self.btnArea.setFont(font)
        self.btnArea.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"	background-color: rgb(27, 30, 35);\n"
"color: rgb(195, 204, 223);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(86, 138, 242);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(52, 52, 52);\n"
"}")
        self.btnArea.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btnArea)

        self.btnComponente = QPushButton(self.w_menu_lateral)
        self.btnComponente.setObjectName(u"btnComponente")
        self.btnComponente.setMinimumSize(QSize(160, 50))
        self.btnComponente.setFont(font)
        self.btnComponente.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"	background-color: rgb(27, 30, 35);\n"
"color: rgb(195, 204, 223);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(86, 138, 242);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(52, 52, 52);\n"
"}")
        self.btnComponente.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btnComponente)

        self.btnMatriz = QPushButton(self.w_menu_lateral)
        self.btnMatriz.setObjectName(u"btnMatriz")
        self.btnMatriz.setMinimumSize(QSize(160, 50))
        self.btnMatriz.setFont(font)
        self.btnMatriz.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"	background-color: rgb(27, 30, 35);\n"
"color: rgb(195, 204, 223);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(86, 138, 242);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(52, 52, 52);\n"
"}")
        self.btnMatriz.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btnMatriz)

        self.btnRestricoes = QPushButton(self.w_menu_lateral)
        self.btnRestricoes.setObjectName(u"btnRestricoes")
        self.btnRestricoes.setMinimumSize(QSize(160, 50))
        self.btnRestricoes.setFont(font)
        self.btnRestricoes.setLayoutDirection(Qt.LeftToRight)
        self.btnRestricoes.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"	background-color: rgb(27, 30, 35);\n"
"color: rgb(195, 204, 223);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(86, 138, 242);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(52, 52, 52);\n"
"}")
        self.btnRestricoes.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btnRestricoes)

        self.btnConfiguracoes = QPushButton(self.w_menu_lateral)
        self.btnConfiguracoes.setObjectName(u"btnConfiguracoes")
        self.btnConfiguracoes.setEnabled(True)
        self.btnConfiguracoes.setMinimumSize(QSize(160, 50))
        self.btnConfiguracoes.setSizeIncrement(QSize(0, 0))
        self.btnConfiguracoes.setBaseSize(QSize(0, 0))
        self.btnConfiguracoes.setFont(font)
        self.btnConfiguracoes.setLayoutDirection(Qt.LeftToRight)
        self.btnConfiguracoes.setStyleSheet(u"QPushButton{\n"
"border:0px solid;\n"
"	background-color: rgb(27, 30, 35);\n"
"color: rgb(195, 204, 223);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(52, 59, 72);\n"
"color: rgb(86, 138, 242);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(52, 52, 52);\n"
"}")
        self.btnConfiguracoes.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btnConfiguracoes)

        self.frame = QFrame(self.w_menu_lateral)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_4.addWidget(self.w_menu_lateral)

        self.widget_3 = QWidget(self.div2_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(800, 550))
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.w_page_principal = QWidget(self.widget_3)
        self.w_page_principal.setObjectName(u"w_page_principal")
        self.w_page_principal.setMinimumSize(QSize(770, 535))
        self.w_page_principal.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.gridLayout_4 = QGridLayout(self.w_page_principal)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, -1, 10)
        self.frame_principal = QFrame(self.w_page_principal)
        self.frame_principal.setObjectName(u"frame_principal")
        self.frame_principal.setEnabled(True)
        self.frame_principal.setMinimumSize(QSize(780, 515))
        self.frame_principal.setMaximumSize(QSize(780, 515))
        self.frame_principal.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_principal)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_principal)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(760, 515))
        self.label.setMaximumSize(QSize(760, 515))
        font3 = QFont()
        font3.setPointSize(20)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: rgb(220, 225, 236);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)


        self.gridLayout_4.addWidget(self.frame_principal, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.w_page_principal)

        self.w_status = QWidget(self.widget_3)
        self.w_status.setObjectName(u"w_status")
        self.w_status.setMinimumSize(QSize(800, 15))
        self.w_status.setMaximumSize(QSize(800, 15))
        self.w_status.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.horizontalLayout = QHBoxLayout(self.w_status)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.label_desenv = QLabel(self.w_status)
        self.label_desenv.setObjectName(u"label_desenv")
        font4 = QFont()
        font4.setFamilies([u"Verdana"])
        font4.setPointSize(6)
        font4.setItalic(False)
        self.label_desenv.setFont(font4)
        self.label_desenv.setStyleSheet(u"color: rgb(138, 149, 170);")

        self.horizontalLayout.addWidget(self.label_desenv)

        self.label_versao = QLabel(self.w_status)
        self.label_versao.setObjectName(u"label_versao")
        self.label_versao.setMinimumSize(QSize(40, 0))
        self.label_versao.setMaximumSize(QSize(40, 16777215))
        self.label_versao.setFont(font4)
        self.label_versao.setStyleSheet(u"color: rgb(138, 149, 170);")

        self.horizontalLayout.addWidget(self.label_versao)


        self.verticalLayout_3.addWidget(self.w_status)


        self.horizontalLayout_4.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.div2_2)


        self.retranslateUi(form_principal)

        QMetaObject.connectSlotsByName(form_principal)
    # setupUi

    def retranslateUi(self, form_principal):
        form_principal.setWindowTitle(QCoreApplication.translate("form_principal", u"Gerador de Grade Hor\u00e1ria Escolar - PRINCIPAL", None))
        self.lblMenu.setText(QCoreApplication.translate("form_principal", u"=", None))
        self.titulo.setText(QCoreApplication.translate("form_principal", u"Janela Principal", None))
        self.lblStatus.setText("")
        self.btnGerar.setText(QCoreApplication.translate("form_principal", u"Gerar Grade", None))
        self.btnTurmas.setText(QCoreApplication.translate("form_principal", u"Turmas", None))
        self.btnProfessores.setText(QCoreApplication.translate("form_principal", u"Professores", None))
        self.btnDisponibilidades.setText(QCoreApplication.translate("form_principal", u"Disponibilidades", None))
        self.btnCargaHoraria.setText(QCoreApplication.translate("form_principal", u"Carga Hor\u00e1ria", None))
        self.btnArea.setText(QCoreApplication.translate("form_principal", u"\u00c1rea de Conhecimento", None))
        self.btnComponente.setText(QCoreApplication.translate("form_principal", u"Componente Curricular", None))
        self.btnMatriz.setText(QCoreApplication.translate("form_principal", u"Matriz Curricular", None))
        self.btnRestricoes.setText(QCoreApplication.translate("form_principal", u"Restri\u00e7\u00f5es", None))
        self.btnConfiguracoes.setText(QCoreApplication.translate("form_principal", u"Configura\u00e7\u00f5es", None))
        self.label.setText(QCoreApplication.translate("form_principal", u"Gerador de Grade Hor\u00e1ria Escolar", None))
        self.label_desenv.setText(QCoreApplication.translate("form_principal", u"Desenvolvido por: F\u00e1bio Pereira de Souza", None))
        self.label_versao.setText(QCoreApplication.translate("form_principal", u"v1.0.0", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'teste.ui'
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
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QSize(900, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 21))
        self.menu_turmas = QMenu(self.menubar)
        self.menu_turmas.setObjectName(u"menu_turmas")
        self.menu_professores = QMenu(self.menubar)
        self.menu_professores.setObjectName(u"menu_professores")
        self.menu_disponibilidade = QMenu(self.menubar)
        self.menu_disponibilidade.setObjectName(u"menu_disponibilidade")
        self.menu_matriz_Curricular = QMenu(self.menubar)
        self.menu_matriz_Curricular.setObjectName(u"menu_matriz_Curricular")
        self.menu_configuracoes = QMenu(self.menubar)
        self.menu_configuracoes.setObjectName(u"menu_configuracoes")
        self.menu_restricoes = QMenu(self.menubar)
        self.menu_restricoes.setObjectName(u"menu_restricoes")
        self.menu_componentes_curriculares = QMenu(self.menubar)
        self.menu_componentes_curriculares.setObjectName(u"menu_componentes_curriculares")
        self.menu_areas_de_conhecimento = QMenu(self.menubar)
        self.menu_areas_de_conhecimento.setObjectName(u"menu_areas_de_conhecimento")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_turmas.menuAction())
        self.menubar.addAction(self.menu_professores.menuAction())
        self.menubar.addAction(self.menu_disponibilidade.menuAction())
        self.menubar.addAction(self.menu_areas_de_conhecimento.menuAction())
        self.menubar.addAction(self.menu_componentes_curriculares.menuAction())
        self.menubar.addAction(self.menu_matriz_Curricular.menuAction())
        self.menubar.addAction(self.menu_configuracoes.menuAction())
        self.menubar.addAction(self.menu_restricoes.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gerador de Grade Hor\u00e1ria Escolar", None))
        self.menu_turmas.setTitle(QCoreApplication.translate("MainWindow", u"Turmas", None))
        self.menu_professores.setTitle(QCoreApplication.translate("MainWindow", u"Professores", None))
        self.menu_disponibilidade.setTitle(QCoreApplication.translate("MainWindow", u"Disponibilidade", None))
        self.menu_matriz_Curricular.setTitle(QCoreApplication.translate("MainWindow", u"Matriz Curricular", None))
        self.menu_configuracoes.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.menu_restricoes.setTitle(QCoreApplication.translate("MainWindow", u"Restri\u00e7\u00f5es", None))
        self.menu_componentes_curriculares.setTitle(QCoreApplication.translate("MainWindow", u"Componentes Curriculares", None))
        self.menu_areas_de_conhecimento.setTitle(QCoreApplication.translate("MainWindow", u"\u00c1reas de Conhecimento", None))
    # retranslateUi


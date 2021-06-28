# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teste.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menu_turmas = QtWidgets.QMenu(self.menubar)
        self.menu_turmas.setObjectName("menu_turmas")
        self.menu_professores = QtWidgets.QMenu(self.menubar)
        self.menu_professores.setObjectName("menu_professores")
        self.menu_disponibilidade = QtWidgets.QMenu(self.menubar)
        self.menu_disponibilidade.setObjectName("menu_disponibilidade")
        self.menu_matriz_Curricular = QtWidgets.QMenu(self.menubar)
        self.menu_matriz_Curricular.setObjectName("menu_matriz_Curricular")
        self.menu_configuracoes = QtWidgets.QMenu(self.menubar)
        self.menu_configuracoes.setObjectName("menu_configuracoes")
        self.menu_restricoes = QtWidgets.QMenu(self.menubar)
        self.menu_restricoes.setObjectName("menu_restricoes")
        self.menu_componentes_curriculares = QtWidgets.QMenu(self.menubar)
        self.menu_componentes_curriculares.setObjectName("menu_componentes_curriculares")
        self.menu_areas_de_conhecimento = QtWidgets.QMenu(self.menubar)
        self.menu_areas_de_conhecimento.setObjectName("menu_areas_de_conhecimento")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gerador de Grade Horária Escolar"))
        self.menu_turmas.setTitle(_translate("MainWindow", "Turmas"))
        self.menu_professores.setTitle(_translate("MainWindow", "Professores"))
        self.menu_disponibilidade.setTitle(_translate("MainWindow", "Disponibilidade"))
        self.menu_matriz_Curricular.setTitle(_translate("MainWindow", "Matriz Curricular"))
        self.menu_configuracoes.setTitle(_translate("MainWindow", "Configurações"))
        self.menu_restricoes.setTitle(_translate("MainWindow", "Restrições"))
        self.menu_componentes_curriculares.setTitle(_translate("MainWindow", "Componentes Curriculares"))
        self.menu_areas_de_conhecimento.setTitle(_translate("MainWindow", "Áreas de Conhecimento"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

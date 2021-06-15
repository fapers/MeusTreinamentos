from PyQt5 import uic, QtWidgets


def menu_verde():
    tela.label_2.setText("Verde")
    tela.label_2.setStyleSheet("color: green")


def menu_azul():
    tela.label_2.setText("Azul")
    tela.label_2.setStyleSheet("color: blue")


def menu_vermelho():
    tela.label_2.setText("Vermelho")
    tela.label_2.setStyleSheet("color: red")


def menu_preto():
    tela.label_2.setText("Preto")
    tela.label_2.setStyleSheet("color: black")


def menu_branco():
    tela.label_2.setText("Branco")
    tela.label_2.setStyleSheet("color: white")


app = QtWidgets.QApplication([])
tela = uic.loadUi('menu.ui')

tela.actionVerde.triggered.connect(menu_verde)
tela.actionAzul.triggered.connect(menu_azul)
tela.actionVermelho.triggered.connect(menu_vermelho)
tela.actionPreto.triggered.connect(menu_preto)
tela.actionBranco.triggered.connect(menu_branco)
tela.show()
app.exec()

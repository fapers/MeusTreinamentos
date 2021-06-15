from PyQt5 import uic, QtWidgets


def chama_segunda_tela():
    tela1.hide()
    tela2.show()
    tela2.label.setText("Olá Fábio!")


def chama_primeira_tela():
    tela2.hide()
    tela1.show()


app = QtWidgets.QApplication([])
tela1 = uic.loadUi('tela1.ui')
tela2 = uic.loadUi('tela2.ui')

tela1.btn1.clicked.connect(chama_segunda_tela)
tela2.btnVoltar.clicked.connect(chama_primeira_tela)

tela1.show()
app.exec()

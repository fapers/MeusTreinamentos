from PyQt5 import uic, QtWidgets


valor = 0


def incrementar_valor():
    global valor
    if valor < 100:
        valor += 10
    janela.progressBar.setValue(valor)
    if(valor == 100):
        janela.pushButton.setProperty("enabled", False)
    else:
        janela.pushButton.setProperty("enabled", True)


def zerar_valor():
    global valor
    valor = 0
    janela.progressBar.setValue(valor)
    janela.pushButton.setProperty("enabled", True)


app = QtWidgets.QApplication([])
janela = uic.loadUi("pbar.ui")
janela.pushButton.setProperty("enabled", True)
janela.pushButton.clicked.connect(incrementar_valor)
janela.pushButton_2.clicked.connect(zerar_valor)

janela.show()
app.exec()

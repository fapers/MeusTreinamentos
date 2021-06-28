from PyQt5 import uic, QtWidgets


def opcao_selecionada():
    cidade = tela.comboBox.currentText()
    tela.label_2.setText(f'Cidade: {cidade}')


app = QtWidgets.QApplication([])
tela = uic.loadUi('combo.ui')

tela.comboBox.addItems([
    "São Paulo",
    "Rio de Janeiro",
    "Montes Claros",
    "Curitiba",
    "Januária"
])

tela.pushButton.clicked.connect(opcao_selecionada)

tela.show()
app.exec()

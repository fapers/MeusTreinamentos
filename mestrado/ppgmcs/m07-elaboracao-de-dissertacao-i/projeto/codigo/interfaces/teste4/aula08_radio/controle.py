from PyQt5 import uic, QtWidgets


def funcao_principal():
    if form.radioButton.isChecked():
        opcao = 'Opção 1 selecionada'
    elif form.radioButton_2.isChecked():
        opcao = 'Opção 2 selecionada'
    elif form.radioButton_3.isChecked():
        opcao = 'Opção 3 selecionada'
    elif form.radioButton_4.isChecked():
        opcao = 'Opção 4 selecionada'
    else:
        opcao = ""
    form.label_2.setText(f"Cor selecionada: {opcao}")



app = QtWidgets.QApplication([])
form = uic.loadUi("janela.ui")
form.pushButton.clicked.connect(funcao_principal)

form.show()
app.exec()

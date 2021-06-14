from PyQt5 import uic, QtWidgets


def funcao_principal():
    if form.radioButton.isChecked():
        print('Opção 1 selecionada')
    elif form.radioButton_2.isChecked():
        print('Opção 2 selecionada')
    elif form.radioButton_3.isChecked():
        print('Opção 3 selecionada')
    elif form.radioButton_4.isChecked():
        print('Opção 4 selecionada')
    else:
        print("")



app = QtWidgets.QApplication([])
form = uic.loadUi("janela.ui")
form.pushButton.clicked.connect(funcao_principal)

form.show()
app.exec()

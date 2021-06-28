from PyQt5 import uic, QtWidgets

def somar():
    soma = 0
    if(tela1.checkBox.isChecked()):
        soma += 15
        tela1.checkBox.setChecked(False)
    if(tela1.checkBox_2.isChecked()):
        soma += 20
        tela1.checkBox_2.setChecked(False)
    if(tela1.checkBox_3.isChecked()):
        soma += 10
        tela1.checkBox_3.setChecked(False)
    if(tela1.checkBox_4.isChecked()):
        soma += 32
        tela1.checkBox_4.setChecked(False)
    if(tela1.checkBox_5.isChecked()):
        soma += 5.50
        tela1.checkBox_5.setChecked(False)

    tela1.label.setText(f'Valor Total: {str(soma)}')


app = QtWidgets.QApplication([])
tela1 = uic.loadUi("check.ui")
tela1.pushButton.clicked.connect(somar)

tela1.show()
app.exec()

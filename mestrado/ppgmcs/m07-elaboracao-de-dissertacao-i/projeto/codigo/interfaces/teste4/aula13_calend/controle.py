from PyQt5 import uic, QtWidgets


def pegar_data():
    data = str(tela1.calendario.selectedDate())
    # print(data[19:30])
    data_formatada = data[19:30]
    tela1.label.setText(f'Data selecionada: {data_formatada}')


app = QtWidgets.QApplication([])
tela1 = uic.loadUi('calend.ui')

tela1.calendario.selectionChanged.connect(pegar_data)
tela1.show()
app.exec()

from PyQt5 import uic, QtWidgets
import sqlite3


def salvar_dados():
    nome = tela.lineEdit.text()
    endereco = tela.lineEdit_2.text()
    email = tela.lineEdit_3.text()

    try:
        banco = sqlite3.connect('banco_cadastro.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados\
             (nome text, endereco text, email text)")

        ''' cursor.execute("INSERT INTO dados VALUES \
             ('"+nome+"', '"+endereco+"', '"+email+"')")'''

        cursor.execute(f"INSERT INTO dados VALUES \
            ('{nome}', '{endereco}', '{email}')")
        banco.commit()
        banco.close()

        print("Dados inseridos com sucesso!")
        tela.label_debug.setText("Dados inseridos com sucesso!")

        limpar_tela()

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados", erro)
        tela.label_debug.setText(f"Erro ao inserir os dados: {erro}")


def listar_dados():
    tela2.show()
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM dados")
    dados_lidos = cursor.fetchall()
    tela2.tableWidget.setRowCount(len(dados_lidos))
    tela2.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            tela2.tableWidget.setItem(
                i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    banco.close()


def limpar_tela():
    tela.lineEdit.setText("")
    tela.lineEdit_2.setText("")
    tela.lineEdit_3.setText("")
    tela.label_debug.setText("")


app = QtWidgets.QApplication([])
tela = uic.loadUi("formulario.ui")
tela2 = uic.loadUi("lista_dados.ui")
tela.pushButton.clicked.connect(salvar_dados)
tela.pushButton_2.clicked.connect(listar_dados)

tela.show()
app.exec()

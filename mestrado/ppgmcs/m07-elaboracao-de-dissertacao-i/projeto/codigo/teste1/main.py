from PyQt5 import uic, QtWidgets
from bancodados.modelo import Area, Componente


def form_area():
    tarea.show()
    tarea.label_titulo.setText("Área de Conhecimento")

    lista = listar_area(tarea)
    tarea.tableWidget.setRowCount(len(lista))
    tarea.tableWidget.setColumnCount(3)

    for i in range(0, len(lista)):
        for j in range(0, 3):
            tarea.tableWidget.setItem(
                i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))
    tarea.btnSalvar.clicked.connect(cadastrar_area)
    tarea.btnListar.clicked.connect(listar_area)


def cadastrar_area():
    nome = tarea.lineEdit.text()
    area = Area(nome)
    area.salvar()
    limpar_campos(tarea)
    sair(tarea)


def listar_area(tarea):
    lista = Area().get_areas()
    return lista


def remover_area(id):
    area = Area("", id)
    area.deletar()


def limpar_campos(form):
    form.lineEdit.setText("")


def sair(form):
    form.hide()


def form_componente():
    tcomponente.show()
    tcomponente.label_titulo.setText("Componentes Curriculares")
    tcomponente.btnSalvar.clicked.connect(cadastrar_componente)


def cadastrar_componente():
    nome = tcomponente.lineEdit.text()
    componente = Componente(nome)
    componente.salvar()


app = QtWidgets.QApplication([])
tela = uic.loadUi("interfaces/main.ui")
# gerar = uic.loadUi("interfaces/grade.ui")
# turmas = uic.loadUi("interfaces/turmas.ui")
# professores = uic.loadUi("interfaces/professores.ui")
# disponibilidades = uic.loadUi("interfaces/disponibilidades.ui")
# carga_horaria = uic.loadUi("interfaces/carga_horaria.ui")
tarea = uic.loadUi("interfaces/area.ui")
tcomponente = uic.loadUi("interfaces/componente.ui")
# matriz = uic.loadUi("interfaces/matriz.ui")
# restricoes = uic.loadUi("interfaces/restricoes.ui")
# configuracoes = uic.loadUi("interfaces/configuracoes.ui")

# tela.btnGerar.clicked.connect(form_grade)
# tela.btnTurmas.clicked.connect(form_turmas)
# tela.btnProfessores.clicked.connect(form_professores)
# tela.btnDisponibilidades.clicked.connect(form_disponibilidades)
# tela.btnCargaHoraria.clicked.connect(form_carga_horaria)
tela.btnArea.clicked.connect(form_area)
tela.btnComponente.clicked.connect(form_componente)
# tela.btnMatriz.clicked.connect(form_matriz_curricular)
# tela.btnRestricoes.clicked.connect(form_restricoes)
# tela.btnConfiguracoes.clicked.connect(form_configuracoes)


tela.show()
app.exec()

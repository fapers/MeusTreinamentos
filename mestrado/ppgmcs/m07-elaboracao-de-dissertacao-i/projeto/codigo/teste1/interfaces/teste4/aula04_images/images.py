import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWidgets import QToolTip, QLabel
from PyQt5 import QtGui


class Window(QMainWindow):
    # Créditos: '''https://youtu.be/iCCejilute4'''
    # Icones gratuitos: https://app.streamlinehq.com/icons
    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "Gerador de Grade de Horários Escolares - \
                      ESCOLA ESTADUAL DELFINO MAGALHÃES"

        button1 = QPushButton('Grade Horária', self)
        button1.move(140, 200)
        button1.resize(250, 80)
        button1.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px; border:0px solid;}\
            QPushButton:hover{\
                background-color:rgb(85, 170, 255);}')
        button1.clicked.connect(self.button1_click)

        button2 = QPushButton('Turmas', self)
        button2.move(410, 200)
        button2.resize(250, 80)
        button2.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px; border:0px solid;}\
            QPushButton:hover{\
                background-color:rgb(85, 170, 255);}')
        button2.clicked.connect(self.button2_click)

        button3 = QPushButton('Professores', self)
        button3.move(140, 300)
        button3.resize(250, 80)
        button3.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px; border:0px solid;}\
            QPushButton:hover{\
                background-color:rgb(85, 170, 255);}')
        button3.clicked.connect(self.button3_click)

        button4 = QPushButton('Matriz Curricular', self)
        button4.move(410, 300)
        button4.resize(250, 80)
        button4.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px; border:0px solid;}\
            QPushButton:hover{\
                background-color:rgb(85, 170, 255);}')
        button4.clicked.connect(self.button4_click)

        button5 = QPushButton('Disponibilidade', self)
        button5.move(140, 400)
        button5.resize(250, 80)
        button5.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px; border:0px solid;}\
            QPushButton:hover{\
                background-color:rgb(85, 170, 255);}')
        button5.clicked.connect(self.button5_click)

        button6 = QPushButton('Parâmetros e \nRestrições', self)
        button6.move(410, 400)
        button6.resize(250, 80)
        button6.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px; border:0px solid;}\
            QPushButton:hover{\
                background-color:rgb(85, 170, 255);}')
        button6.clicked.connect(self.button6_click)

        self.label_1 = QLabel(self)
        self.label_1.setText("  Escolha uma opção!")
        self.label_1.move(250, 100)
        self.label_1.resize(400, 25)
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px;\
             color:"blue";}')

        # IMAGEM PRINCIPAL ESCOLHA A OPÇÃO
        self.label_2 = QLabel(self)
        self.label_2.move(40, 0)
        self.label_2.resize(200, 200)
        self.label_2.setPixmap(QtGui.QPixmap('images/settings.png'))

        # 140 + 250 = 390
        # 390 + 20 = 410
        # 410 + 250 = 660
        # 660 + 140 = 800

        self.load_window()

    def load_window(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def button1_click(self):
        self.label_1.setText("  Geração da Grade Horária   ")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px;\
             color:"red";}')
        self.label_2.setPixmap(QtGui.QPixmap('images/executar.png'))

    def button2_click(self):
        self.label_1.setText("      Turmas Cadastradas      ")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px;\
             color:"green";}')
        self.label_2.setPixmap(QtGui.QPixmap('images/turmas.png'))

    def button3_click(self):
        self.label_1.setText("    Professores Cadastrados   ")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px;\
             color:"green";}')
        self.label_2.setPixmap(QtGui.QPixmap('images/professora.png'))

    def button4_click(self):
        self.label_1.setText("       Matriz Curricular      ")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px;\
             color:"gray";}')
        self.label_2.setPixmap(QtGui.QPixmap('images/solucao.png'))

    def button5_click(self):
        self.label_1.setText("        Disponibilidade       ")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px;\
             color:"gray";}')
        self.label_2.setPixmap(QtGui.QPixmap('images/disponibilidade.png'))

    def button6_click(self):
        self.label_1.setText("    Parâmetros e Restrições   ")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px;\
             color:"gray";}')
        self.label_2.setPixmap(QtGui.QPixmap('images/restricoes.png'))


app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())

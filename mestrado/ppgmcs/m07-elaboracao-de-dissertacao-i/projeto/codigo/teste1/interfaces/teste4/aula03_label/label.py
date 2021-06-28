import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel


class Window(QMainWindow):
    '''https://youtu.be/iCCejilute4'''
    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "Gerador de Grade de Horários Escolares - \
                      ESCOLA ESTADUAL DELFINO MAGALHÃES"

        button1 = QPushButton('Grade Horária', self)
        button1.move(140, 140)
        button1.resize(250, 80)
        button1.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button1.clicked.connect(self.button1_click)

        button2 = QPushButton('Turmas', self)
        button2.move(410, 140)
        button2.resize(250, 80)
        button2.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button2.clicked.connect(self.button2_click)

        button3 = QPushButton('Professores', self)
        button3.move(140, 240)
        button3.resize(250, 80)
        button3.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button3.clicked.connect(self.button3_click)

        button4 = QPushButton('Matriz Curricular', self)
        button4.move(410, 240)
        button4.resize(250, 80)
        button4.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button4.clicked.connect(self.button4_click)

        button5 = QPushButton('Disponibilidade', self)
        button5.move(140, 340)
        button5.resize(250, 80)
        button5.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button5.clicked.connect(self.button5_click)

        button6 = QPushButton('Parâmetros e \nRestrições', self)
        button6.move(410, 340)
        button6.resize(250, 80)
        button6.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button6.clicked.connect(self.button6_click)

        self.label_1 = QLabel(self)
        self.label_1.setText("  Escolha uma opção!")
        self.label_1.move(250, 50)
        self.label_1.resize(400, 25)
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color:"blue";}')

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
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color:"red";}')

    def button2_click(self):
        self.label_1.setText("      Turmas Cadastradas      ")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color:"green";}')

    def button3_click(self):
        self.label_1.setText("    Professores Cadastrados   ")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color:"green";}')

    def button4_click(self):
        self.label_1.setText("       Matriz Curricular      ")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color:"gray";}')

    def button5_click(self):
        self.label_1.setText("        Disponibilidade       ")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color:"gray";}')

    def button6_click(self):
        self.label_1.setText("    Parâmetros e Restrições   ")
        self.label_1.setStyleSheet('QLabel {font:bold; font-size:25px; color:"gray";}')


app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())

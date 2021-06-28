import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "Gerador de Grade de Horários Escolares - \
                      ESCOLA ESTADUAL DELFINO MAGALHÃES"

        button1 = QPushButton('Grade Horária', self)
        button1.move(100, 100)
        button1.resize(250, 80)
        button1.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button1.clicked.connect(self.button1_click)

        button2 = QPushButton('Turmas', self)
        button2.move(400, 100)
        button2.resize(250, 80)
        button2.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button2.clicked.connect(self.button2_click)

        button3 = QPushButton('Professores', self)
        button3.move(100, 240)
        button3.resize(250, 80)
        button3.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button3.clicked.connect(self.button3_click)

        button4 = QPushButton('Matriz Curricular', self)
        button4.move(400, 240)
        button4.resize(250, 80)
        button4.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button4.clicked.connect(self.button4_click)

        button5 = QPushButton('Disponibilidade', self)
        button5.move(100, 380)
        button5.resize(250, 80)
        button5.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button5.clicked.connect(self.button5_click)

        button6 = QPushButton('Parâmetros e \nRestrições', self)
        button6.move(400, 380)
        button6.resize(250, 80)
        button6.setStyleSheet('QPushButton{\
            background-color:#0FB328;\
            font:bold; font-size:20px}')
        button6.clicked.connect(self.button6_click)

        self.load_window()

    def load_window(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()

    def button1_click(self):
        print("Geração da Grade Horária")

    def button2_click(self):
        print("Turmas")

    def button3_click(self):
        print("Professores")

    def button4_click(self):
        print("Matriz Curricular")

    def button5_click(self):
        print("Disponibilidade")

    def button6_click(self):
        print("Parâmetros e Restrições")


app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())

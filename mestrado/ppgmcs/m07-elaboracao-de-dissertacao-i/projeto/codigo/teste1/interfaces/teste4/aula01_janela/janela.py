import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.title = "Gerador de Grade de Horários Escolares - Escola Estadual Delfino Magalhães"
        self.load_window()

    def load_window(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.show()


app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())

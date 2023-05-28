# напиши здесь код третьего экрана приложенияclass FInalWIn(QWidget):
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.aet_appear()
        self.initUI()
        self.show()
    def aet_appear(self):
        self.setWindowTitle('Здоровье')
        self.move(500,200)
        self.resize(900,700)
        self.setStyleSheet("background-color: rgb(102,255,0)")
    def initUI(self):
        self.v_line = QVBoxLayout() 
        self.df = QLabel('Индекс Руфье: 1')
        self.v_line.addWidget(self.df, alignment=Qt.AlignCenter)
        self.setLayout(self.v_line)

    def connects(self):
        pass

app = QApplication([])
my_win = FinalWin()

my_win.show()
app.exec_()


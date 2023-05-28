from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.aet_appear()
        self.initUI()
        self.connects()
        self.show()
    def aet_appear(self):
        self.setWindowTitle('Здоровье')
        self.move(500,200)
        self.resize(900,700)
        self.setStyleSheet("background-color: rgb(220,20,60)")
    
    def initUI(self):
        self.v_line = QVBoxLayout()

        
        self.start = QLabel('Добро пожаловать в программу!')
        self.start2 = QLabel('''Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.
            Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке. У испытуемого, находящегося положении лежа на спине 
            в течение 5 мин, определяют частоту пульса за 15 секунд; затем в течение 45 секунд испытуемый выполняет 30 приседаний.
            После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд, а потом за последние 15 секунд первой минуты периода восстановления.
            Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.'''
        )
        self.b = QPushButton('Начать')
        self.v_line.addWidget(self.start, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.start2)
        self.v_line.addWidget(self.b)
        self.setLayout(self.v_line)
    def connects(self):
        pass

app = QApplication([])
my_win = MainWin()

my_win.show()
app.exec_()


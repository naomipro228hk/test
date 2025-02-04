from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from instr import *
from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show() 
    def initUI(self):
        self.btn_next = QPushButton(txt_next,self)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
        self.line = QVBoxLayout()
        self.line.addWidget(self.hello_text,alignment=Qt.AlignLeft)
        self.line.addWidget(self.instruction,alignment=Qt.AlignLeft)
        self.line.addWidget(self.btn_next,alignment=Qt.AlignCenter)
        self.setLayout(self.line)
    def next_click(self):
        self.tw = TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x,win_y)
app = QApplication([])
mw= MainWin()
app.exec_()
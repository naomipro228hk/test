from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QGroupBox,
    QRadioButton,
    QPushButton,
    QLabel,
    QListWidget,
    QLineEdit,
)
from PyQt5.QtGui import (
    QDoubleValidator,
    QIntValidator,
    QFont,
)

from instr import *




class FinalWin(QWidget):
    def __init__(self,exp):
        """окно, в котором проводится опрос"""
        super().__init__()

        self.exp = exp
        # создаём и настраиваем графические элементы:
        self.initUI()


        # устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()


        # старт:
        self.show()


    def initUI(self):
        """создаёт графические элементы"""
        self.workh_text = QLabel(txt_workheart+self.results())
        self.index_text = QLabel(txt_index+str(self.index))


        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)


    """ устанавливает, как будет выглядеть окно (надпись, размер, место) """


    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def results(self):
        if self.exp.age < 7:
            self.index=0
            return 'no'
        self.index = (
            4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200
        ) / 10
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1  
            if self.index < 21 and self.index >= 17:
                return txt_res2
            if self.index < 17 and self.index >= 12:
                return txt_res3
            if self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1  
            if self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            if self.index < 15.5 and  self.index>= 10.5:
                return txt_res3
            if self.index < 10.5 and self.index>= 5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1  
            if self.index < 18 and self.index>= 14:
                return txt_res2
            if self.index < 14 and self.index>= 9:
                return txt_res3
            if self.index < 9 and self.index>= 3.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 13 or self.exp.age == 14:
            if self.index >= 16.5:
                return txt_res1  
            if self.index < 16.5 and self.index>= 12.5:
                return txt_res2
            if self.index < 12.5 and self.index>= 7.5:
                return txt_res3
            if self.index < 7.5 and self.index>= 2:
                return txt_res4
            else:
                return txt_res5                        
        if self.exp.age >=15:
            if self.index >= 15:
                return txt_res1  
            if self.index < 15 and self.index>= 11:
                return txt_res2
            if self.index < 11 and self.index>= 6:
                return txt_res3
            if self.index < 6 and self.index>= 0.5:
                return txt_res4
            else:
                return txt_res5
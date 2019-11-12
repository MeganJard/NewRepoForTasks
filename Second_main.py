import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPen, QColor
from guiSetup import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from random import randrange

class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.a)
        self.painter = QPainter(self)
        self.c1, self.c2, self.c3, self.c4 = 0,0,0,0
        self.li = []
        self.show()

    def paintEvent(self, e):

        painter = QPainter()
        painter.begin(self)

        painter.setPen(QPen(QColor(randrange(1, 240), randrange(1, 240), randrange(1, 240)), 5))
        for i in range(len(self.li)):

            painter.drawEllipse(self.li[i][0], self.li[i][1], self.li[i][2], self.li[i][3])
        self.li.clear()
        painter.end()


    def a(self):
        for i in range(randrange(2, 4)):
            self.li.append([randrange(50, 400), randrange(50, 400), randrange(20, 60), randrange(20, 60)])
        self.update()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from form import Ui_MainWindow
from keyboard import is_pressed
from threading import Timer
from random import randint
from math import sqrt
import sys


class Game(QMainWindow):
    def __init__(self):
        super(Game, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        '''Method attribute'''
        self.coin = 0
        self.defeat = 0
        self.startPosOne = 120
        self.endPosOne = 420
        self.startPosTwo = 420
        self.endPosTwo = 120
        self.stepOne = 1
        self.directionOne = 1
        self.stepTwo = 1
        self.directionTwo = 1
        '''Timer'''
        self.timerOne = QTimer()
        self.timerOne.timeout.connect(self.turtle_move)
        self.timerOne.timeout.connect(self.border)
        self.timerOne.start(70)

        self.timerTwo = QTimer()
        self.timerTwo.timeout.connect(self.loos)
        self.timerTwo.timeout.connect(self.random_money)
        self.timerTwo.timeout.connect(self.triangle_one_move)
        self.timerTwo.timeout.connect(self.triangle_two_move)
        self.timerTwo.start(3)

    '''Label'''

    def label(self, text='', x=1, y=1, w=1, h=1, objName='', font='Arial', size=1):
        self.userlabel = QtWidgets.QLabel(self.ui.centralwidget)
        self.userlabel.setGeometry(QtCore.QRect(x, y, w, h))
        self.userlabel.setText(text)
        self.userlabel.setFont(QFont(font, size))
        self.userlabel.setObjectName(objName)

    def label_hide(self, time=0):
        t = Timer(time, lambda: self.userlabel.setHidden(True))
        t.start()

    '''Gameplay'''

    def turtle_move(self):
        try:
            self.x_turtle = self.ui.Turtle.x()
            self.y_turtle = self.ui.Turtle.y()
            if is_pressed('w'):
                self.ui.Turtle.setPixmap(QtGui.QPixmap(":/icons/icons/turtleUp.svg"))
                self.ui.Turtle.setGeometry(QtCore.QRect(self.x_turtle, self.y_turtle - 10, 51, 61))

            elif is_pressed('s'):
                self.ui.Turtle.setPixmap(QtGui.QPixmap(":/icons/icons/turtleDown.svg"))
                self.ui.Turtle.setGeometry(QtCore.QRect(self.x_turtle, self.y_turtle + 10, 51, 61))
            elif is_pressed('a'):
                self.ui.Turtle.setPixmap(QtGui.QPixmap(":/icons/icons/turtleLeft.svg"))
                self.ui.Turtle.setGeometry(QtCore.QRect(self.x_turtle - 10, self.y_turtle, 51, 61))
            elif is_pressed('d'):
                self.ui.Turtle.setPixmap(QtGui.QPixmap(":/icons/icons/turtleRight.svg"))
                self.ui.Turtle.setGeometry(QtCore.QRect(self.x_turtle + 10, self.y_turtle, 51, 61))
            elif is_pressed('0'):
                self.defeat = 0
                self.coin = 0
                self.ui.Number.setText(str(self.defeat))
                self.ui.label.setText(str(self.defeat))
        except:
            pass

    def triangle_one_move(self):
        y_pos = self.ui.TriangleOne.y()
        if y_pos > self.endPosOne:
            self.directionOne = -1
            self.ui.TriangleOne.setPixmap(QtGui.QPixmap(":/icons/icons/triangle.svg"))
        elif y_pos < self.startPosOne:
            self.directionOne = 1
            self.ui.TriangleOne.setPixmap(QtGui.QPixmap(":/icons/icons/triangleRotated.svg"))

        y_pos += self.stepOne * self.directionOne
        self.ui.TriangleOne.setGeometry(QtCore.QRect(600, y_pos, 61, 61))

    def triangle_two_move(self):
        y_pos = self.ui.TriangleTwo.y()
        if y_pos > self.startPosTwo:
            self.directionTwo = -1
            self.ui.TriangleTwo.setPixmap(QtGui.QPixmap(":/icons/icons/triangle.svg"))
        elif y_pos < self.endPosTwo:
            self.directionTwo = 1
            self.ui.TriangleTwo.setPixmap(QtGui.QPixmap(":/icons/icons/triangleRotated.svg"))

        y_pos += self.stepTwo * self.directionTwo
        self.ui.TriangleTwo.setGeometry(QtCore.QRect(160, y_pos, 61, 61))

    def loos(self):
        self.player_pos = self.ui.Turtle.pos()
        enemy_one = self.ui.TriangleOne.pos()
        enemy_two = self.ui.TriangleTwo.pos()
        distance_one = sqrt((self.player_pos.x() - enemy_one.x()) ** 2 + (self.player_pos.y() - enemy_one.y()) ** 2)
        distance_two = sqrt((self.player_pos.x() - enemy_two.x()) ** 2 + (self.player_pos.y() - enemy_two.y()) ** 2)
        if distance_one < 50 or distance_two < 50:
            self.defeat += 1
            self.ui.label.setText(str(self.defeat))
            self.ui.Turtle.setGeometry(QtCore.QRect(380, 280, 51, 61))

    def border(self):
        if self.x_turtle < 10:
            self.ui.Turtle.setGeometry(QtCore.QRect(self.x_turtle + 770, self.y_turtle, 51, 61))
        elif self.x_turtle > 770:
            self.ui.Turtle.setGeometry(QtCore.QRect(self.x_turtle - 770, self.y_turtle, 51, 61))
        elif self.y_turtle < -20:
            self.ui.Turtle.setGeometry(QtCore.QRect(self.x_turtle, self.y_turtle + 575, 51, 61))
        elif self.y_turtle > 560:
            self.ui.Turtle.setGeometry(QtCore.QRect(self.x_turtle, self.y_turtle - 575, 51, 61))

    def random_money(self):
        coin_pos = self.ui.Coin.pos()
        distance = sqrt((self.player_pos.x() - coin_pos.x()) ** 2 + (self.player_pos.y() - coin_pos.y()) ** 2)
        if distance < 30:
            self.coin += 1
            self.ui.Number.setText(str(self.coin))
            x_coin = randint(20,780)
            y_coin = randint(20, 580)
            self.ui.Coin.setGeometry(QtCore.QRect(x_coin, y_coin, 31, 31))
    '''End'''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Game()
    game.label(text='Нажмите на цифру 0, '
                    'чтобы сбросить счёт', x=250, y=20, w=350, h=50, objName='LabelUser',
               font='Times', size=10)
    game.label_hide(time=10)
    game.show()
    sys.exit(app.exec_())

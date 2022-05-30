from random import seed, random, shuffle, randint, choice
from functools import reduce
import sys
from PyQt5.QtWidgets import  QApplication, QWidget, QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton,QLineEdit,QLabel,QComboBox
from  PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from math import sqrt
from kenken import *
from solver import *















class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'KenKen'
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 1000
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.layout = QVBoxLayout()
        self.CreateLayout()
        # Show widget
        self.show()

    def CreateLayout(self):

        self._generate_button = QPushButton('Generate Board', self)
        self.layout.addWidget(self._generate_button)
        self._generate_button.setToolTip('press this to generate randon KeneKen board with the specified size')
        self._generate_button.clicked.connect(self.Generate)

        self.nameLabel = QLabel(self)
        self.layout.addWidget(self.nameLabel)
        self.nameLabel.setText('Size:')

        self.size_entry = QLineEdit(self)
        self.layout.addWidget(self.size_entry)

        # Create table
        self.tableWidget = QTableWidget()
        # Add box layout, add table to box layout and add box layout to widget
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout)
        #self.tableWidget.move(0,0)

        self.algoLabel = QLabel(self)
        self.layout.addWidget(self.algoLabel)
        self.algoLabel.setText('Algorithm: ')

        self.algo_entry = QComboBox()
        self.algo_entry.addItem('Backtracking')
        self.algo_entry.addItem('Backtracking with Forward Checking')
        self.algo_entry.addItem('Backtracking with Arc consistency')
        self.layout.addWidget(self.algo_entry)




        self.solve_button = QPushButton('Solve', self)
        self.layout.addWidget(self.solve_button)
        self.solve_button.setToolTip('press this to generate randon KeneKen board with the specified size')
        self.solve_button.clicked.connect(self.Solve)
from random import seed, random, shuffle, randint, choice
from functools import reduce
import sys
from PyQt5.QtWidgets import  QApplication, QWidget, QTableWidget,QTableWidgetItem,QVBoxLayout,QPushButton,QLineEdit,QLabel,QComboBox
from  PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from math import sqrt
from kenken import *
from solver import *









def random_color():
    R = randint(0,255)
    G = randint(0,255)
    B = randint(0,255)
    return R,G,B

def euclidistance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def top_left(cage):
    min_distance = 10000
    TopLeft = None
    for pos in cage:
        dist = euclidistance(pos[1],pos[0],1,1)
        if dist < min_distance:
            min_distance = dist
            TopLeft = pos
    return TopLeft






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

        
        
        
 

       

        

    @pyqtSlot()
    def Generate(self):
        self.size = int(self.size_entry.text())
        _,self.cliques = generate(size=self.size)
        self.tableWidget.setRowCount(self.size)
        self.tableWidget.setColumnCount(self.size)
        for c in self.cliques:
            color = random_color()
            cage = c[0]
            
            TopLeft = top_left(cage=cage)
            
            for idx in cage:
                self.tableWidget.setItem(idx[1]-1,idx[0]-1,QTableWidgetItem())
                self.tableWidget.item(idx[1]-1,idx[0]-1).setBackground(QtGui.QColor(color[0],color[1],color[2]))
        
            self.tableWidget.item(TopLeft[1]-1,TopLeft[0]-1).setText(c[1]+'('+str(c[2])+')')

    
    @pyqtSlot()
    def Solve(self):
        ken = Kenken(self.size,self.cliques)
        algorithm = self.algo_entry.currentText()
        if algorithm == "Backtracking":
            assignment = backtracking_search(ken)
        elif algorithm == "Backtracking with Forward Checking":
            assignment = backtracking_search(ken,inference=forward_checking)
        elif algorithm == "Backtracking with Arc consistency":
            assignment = backtracking_search(ken,inference=mac)
            


        
        for cage in assignment:
            for i in range(len(cage)):
                value = assignment[cage][i]
                idx = cage[i]
                temp = self.tableWidget.item(idx[1]-1,idx[0]-1).text()
                self.tableWidget.item(idx[1]-1,idx[0]-1).setText(temp + ' ' + str(value))

                
            

            

        
        
        
       
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())







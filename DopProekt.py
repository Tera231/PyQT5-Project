# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'DopProekt.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from pyqtgraph import PlotWidget

class Ui_InstructionForm(QWidget):
    def __init__(self, parent):
        super(Ui_InstructionForm, self).__init__(parent)
        self.parent = parent
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Window)
        self.setupUi(self)
        self.show()
        self.setWindowTitle("Graph Calculator")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(431, 338)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 40, 441, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.graphicsView = PlotWidget(Form)
        self.graphicsView.setGeometry(QtCore.QRect(0, 90, 431, 241))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(100, 0, 111, 41))
        self.pushButton2.setObjectName("pushButton2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.run)
        self.pushButton2.clicked.connect(self.save)

    def run(self):
        formula = list(self.plainTextEdit.toPlainText())
        self.points = []
        if formula[1] != 'x' and formula[0] == '-':
            formula[formula.index('x')] = '* x'
            formula = list(''.join(formula))
        for i in range(-100, 100):
            y = formula + []
            if i > 0:
                y[y.index('x')] = str(i)
            else:
                y[y.index('x')] = '(' + str(i) + ')'
            try:
                self.points.append(float(eval(''.join(y))))
            except TypeError:
                pass
        self.graphicsView.clear()
        if len(self.points) > 100:
            self.graphicsView.plot([i for i in range(-100, 100)], self.points)
        else:
            self.graphicsView.plot([i for i in range(100)], self.points)

    def save(self):
        f = open('points.txt', 'r')
        lines = f.readlines()
        f.close()
        f = open('points.txt', 'w')
        for i in range(-100, 100):
            n = str((str(i) + ' ' + str(self.points[100 + i]) + '\n'))
            f.write(n)
        f.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Сгенерировать"))
        self.pushButton2.setText(_translate("Form", "Сохранить в файл"))

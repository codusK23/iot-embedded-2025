import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

class WindowClass(QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.ui = uic.loadUi("btnClick.ui", self)
		self.ui.show()

	def slot1(self):
		self.ui.label.setText("L-Btn Clicked")

	def slot2(self):
		self.ui.label.setText("R-Btn Clicked")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	app.exec_()

import RPi.GPIO as GPIO
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

GPIO.setmode(GPIO.BCM)

RED = 14
GREEN = 18
BLUE = 15

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

class WindowClass(QDialog):
	def __init__(self, parent = None):
		super().__init__(parent)
		self.ui = uic.loadUi("ledControl.ui", self)
		self.ui.show()

	def power(self, r, g, b):
		GPIO.output(RED, GPIO.LOW if r else GPIO.HIGH)
		GPIO.output(GREEN, GPIO.LOW if g else GPIO.HIGH)
		GPIO.output(BLUE, GPIO.LOW if b else GPIO.HIGH)

	def red(self):
		self.ui.label.setText("RED")
		self.ui.label.setStyleSheet("Color : red")
		self.power(1, 0, 0)


	def green(self):
		self.ui.label.setText("GREEN")
		self.ui.label.setStyleSheet("Color : green")
		self.power(0, 1, 0)

	def blue(self):
		self.ui.label.setText("BLUE")
		self.ui.label.setStyleSheet("Color : blue")
		self.power(0, 0, 1)


	def off(self):
		self.ui.label.setText("OFF")
		self.ui.label.setStyleSheet("Color : black")
		self.power(0, 0, 0)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = WindowClass()
	app.exec_()

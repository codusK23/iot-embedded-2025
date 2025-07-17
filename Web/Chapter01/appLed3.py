from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

RED = 18
GREEN = 14
BLUE = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

@app.route('/')
def ledFlask():
	return "<h1>LED Control Web</h1>"

@app.route('/led/<color>/<state>')
def led(color, state):
	if color == 'red':
		pin = RED
	elif color == 'green':
		pin = GREEN
	elif color == 'blue':
		pin = BLUE

	if state == 'on':
		GPIO.output(pin, GPIO.LOW)
	else:
		GPIO.output(pin, GPIO.HIGH)
	return "LED" + color + state

@app.route('/led/clean')
def gpiocleanup():
	GPIO.cleanup()
	return "<h1> GPIO CLEANUP </h1>"

if __name__ == "__main__":
	app.run(host='0.0.0.0')

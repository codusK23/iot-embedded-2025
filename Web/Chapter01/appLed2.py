from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def ledFlask():
	return "<h1>LED Control Web</h1>"

@app.route('/led/<state>')
def led(state):
	if state == 'on':
		GPIO.output(ledPin, GPIO.LOW)
	else:
		GPIO.output(ledPin, GPIO.HIGH)
	return "LED" + state

@app.route('/led/clean')
def gpiocleanup():
	GPIO.cleanup()
	return "<h1> GPIO CLEANUP </h1>"

if __name__ == "__main__":
	app.run(host='0.0.0.0')

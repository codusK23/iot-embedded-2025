import RPi.GPIO as GPIO
import time
import sys
import tty
import termios

piezoPin = 24

Melody = {'1': 262, '2': 294, '3': 330,
		  '4': 349, '5': 392, '6': 440,
		  '7': 494, '8': 523, '9': 587, '0': 659}

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

sound = GPIO.PWM(piezoPin, 440)
sound.start(0)

def get_key():
	fd = sys.stdin.fileno()
	old = termios.tcgetattr(fd)
	try:
		tty.setraw(fd)
		return sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old)

try:
	print("연주를 시작하시오.")
	while True:
		key = get_key()
		if key == 'q':
			break

		if key in Melody:
			freq = Melody[key]
			print(f"{key} : {freq}")
			sound.ChangeFrequency(freq)
			sound.start(50)

			time.sleep(0.15)
			sound.stop()
		else:
			pass
		time.sleep(0.02)

except KeyboardInterrupt:
	GPIO.cleanup()

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED = 14
GREEN = 18
BLUE = 15

buttonPin = 17

cnt = 0

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN)


def color_change(cnt):
	GPIO.output(RED, GPIO.HIGH)
	GPIO.output(GREEN, GPIO.HIGH)
	GPIO.output(BLUE, GPIO.HIGH)
	if cnt == 1:
        print("LED : OFF")
    elif cnt == 2:
        GPIO.output(RED, GPIO.LOW)
        print("LED : RED")
    elif cnt == 3:
        GPIO.output(GREEN, GPIO.LOW)
        print("LED : GREEN")
    elif cnt == 0:
        GPIO.output(BLUE, GPIO.LOW)
        print("LED : BLUE")

try:
	while True:
		if (GPIO.input(buttonPin) == GPIO.LOW):
			cnt = (cnt + 1) % 4
			color_change(cnt)
			while (GPIO.input(buttonPin) == GPIO.LOW):
				time.sleep(0.01)
		time.sleep(0.01)

except KeyboardInterrupt:
	GPIO.cleanup()

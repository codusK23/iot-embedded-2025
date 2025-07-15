import RPi.GPIO as GPIO
import time

swPin = 14
relayPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(relayPin, GPIO.OUT)

GPIO.output(relayPin, False)

def relay_control(channel):
	if (GPIO.input(swPin) == GPIO.LOW):
		GPIO.output(relayPin, True)
		print("LED : ON")

	else:
		GPIO.output(relayPin, False)
		print("LED : OFF")

GPIO.add_event_detect(swPin, GPIO.BOTH, callback=relay_control, bouncetime=200)

try:
	while True:
		pass

except KeyboardInterrupt:
	GPIO.cleanup()

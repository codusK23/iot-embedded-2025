import RPi.GPIO as GPIO
import time

RED = 14
BLUE = 15
buttonPin = 23
piezoPin = 24

Melody = [880, 440, 880, 440, 880, 440, 880, 440, 880, 440]

GPIO.setmode(GPIO.BCM)

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(piezoPin, GPIO.OUT)

sound = GPIO.PWM(piezoPin, 440)

btn_p = False
siren = False
led = True

cnt = 0

try:
	while True:
		if (GPIO.input(buttonPin) == GPIO.LOW):
			if not btn_p:
				siren = not siren
				print("siren", "ON" if siren else "OFF")
				btn_p = True
				time.sleep(0.2)
		else:
			btn_p = False

		if siren:
			for i in range(len(Melody)):
				if (GPIO.input(buttonPin) == GPIO.LOW):
					if not btn_p:
						siren = False
						btn_p = True
						print("Siren OFF")
						break
				else:
					btn_p = False

				sound.start(50)
				sound.ChangeFrequency(Melody[i])

				if led:
					GPIO.output(RED, GPIO.LOW)
					GPIO.output(BLUE, GPIO.HIGH)
				else:
					GPIO.output(RED, GPIO.HIGH)
					GPIO.output(BLUE, GPIO.LOW)

				led = not led
				time.sleep(0.2)

			sound.stop()

		else:
			GPIO.output(RED, GPIO.HIGH)
			GPIO.output(BLUE, GPIO.HIGH)
			sound.stop()

		time.sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()

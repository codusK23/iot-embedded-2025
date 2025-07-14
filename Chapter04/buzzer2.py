import RPi.GPIO as GPIO
import time

piezoPin = 18

Melody = [262, 294, 330, 349, 392, 440, 494, 523]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

sound = GPIO.PWM(piezoPin, 440)					# 해당 핀에 440hz 출력

try:
	while True:
		sound.start(50)							# 듀티비 50% PWM 시작
		for i in range(0, len(Melody)):
			sound.ChangeFrequency(Melody[i])	# 주파수 변경
			time.sleep(0.5)
		sound.stop()							# WPM 중지
		time.sleep(1)

except KeyboardInterrupt:
	GPIO.cleanup()

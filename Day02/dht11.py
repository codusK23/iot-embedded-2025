import RPi.GPIO as GPIO
import time
import adafruit_dht
import board
import mysql.connector

dhtPin = 23

GPIO.setmode(GPIO.BCM)
# GPIO.setup(dhtPin, GPIO.IN)

dht = adafruit_dht.DHT11(board.D23)

db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "raspi",
	database = "TESTDB"
)

cursor = db.cursor()

while True:
	try:
		temp = dht.temperature
		humi = dht.humidity
		print("Temp: ", temp)
		print("Humi: ", humi)

		cursor.execute(
			"INSERT INTO dht11_data (temp, humi) VALUES (%s, %s)", (temp, humi)
		)
		db.commit()
		time.sleep(5)

	except RuntimeError as error:
		print(error.args[0])

	except KeyboardInterrupt:
		GPIO.cleanup()
		break

dhtPin.exit()

import Adafruit_DHT
import time
import RPi.GPIO as GPIO

#Initialize PIN 17 for the DHT22 data;
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17

#sets the mode to broadcom (GPIO pinout);
GPIO.setmode(GPIO.BCM)


# Relay
# Tells python that GPIO 4 is an output;
rpin = 4
GPIO.setup(rpin, GPIO.OUT)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print ("Temp={0:0.01f}C Humidity={1:0.1f}%".format(temperature, humidity))

    if humidity > 45.0:
        GPIO.output(rpin, GPIO.HIGH)
        print('Relay 1 on')
        time.sleep(5)
    else:
        GPIO.output(rpin, GPIO.LOW)
        time.sleep(5)
        print('Relay 1 OFF')

# GPIO.cleanup()

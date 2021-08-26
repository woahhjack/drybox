import Adafruit_DHT
import time
import RPi.GPIO as GPIO

#Initialize PIN 4 for the DHT11 data;
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

#sets the mode to broadcom (GPIO pinout);
GPIO.setmode(GPIO.BCM)

# Note: The relay is active low.
# Tells python that GPIO 14 is an output;
GPIO.setup(17, GPIO.OUT)

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print ("Temp={0:0.01f}C Humidity={1:0.1f}%".format(temperature, humidity))
        if temperature > 25:
            GPIO.output(17, GPIO.LOW)
            print('Relay 1 on')
            time.sleep(2)
        else:
            GPIO.output(17, GPIO.HIGH)
            time.sleep(2)
            print('Relay 1 OFF')

GPIO.cleanup()


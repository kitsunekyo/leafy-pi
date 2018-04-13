import Adafruit_DHT
import RPi.GPIO as GPIO
import getopt, sys

GPIO.setwarnings(False)

dht_pin = 4

def get_DHT():
    dht_sensor = Adafruit_DHT.DHT11
    obj = dict()
    humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, dht_pin)
    if humidity is not None and temperature is not None:
        print(humidity)
        print(temperature)
        return([humidity, temperature])
    else:
        print(0)
        return([])

if __name__ == '__main__':
    get_DHT()

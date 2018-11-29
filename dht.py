#!/usr/bin/env python

import time
import Adafruit_DHT
import datetime


# sensor type
sensor = Adafruit_DHT.DHT11

# data input pin
pin = 4

f = open("data.txt", 'a', 0)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    if humidity is not None and temperature is not None:
        f.write('{}\t{}\t{}\n'.format(
            datetime.datetime.now(), temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

    time.sleep(300)

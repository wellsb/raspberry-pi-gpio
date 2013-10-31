import RPi.GPIO as GPIO
import sys
import time
from random import choice

pin_out = [13,15,7,12,16,22]
pin_in = [11, 18]
ison = [1,2]

intev = 0.01
times = 2000

def pin_out_setup():
        global pin_out
        for this_out_pin in pin_out:
                GPIO.setup(this_out_pin, GPIO.OUT)

def pin_in_setup():
        global pin_in
        for this_in_pin in pin_in:
                GPIO.setup(this_in_pin, GPIO.IN)        

pin_out_setup()
pin_in_setup()

for x in range(0, times):

        this_out_pin = choice(pin_out)
        print (this_out_pin)
        if choice(ison) == 1:
                GPIO.output(this_out_pin, False)
        time.sleep(intev)
        if choice(ison) == 1:
                GPIO.output(this_out_pin, True)
        time.sleep(intev)

sys.exit()

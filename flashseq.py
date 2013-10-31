import RPi.GPIO as GPIO
import sys
import time
from random import choice

ison = [1,2,3]
pin_out = [13,15,7,12,16,22]
intev = 0.05
times = 2000000

debug = False

def pin_out_setup():
        for this_out_pin in pin_out:
                GPIO.setup(this_out_pin, GPIO.OUT)

def pin_in_setup():
        in_pin = [11, 18]
        for this_in_pin in in_pin:
                GPIO.setup(this_in_pin, GPIO.IN)

def checkin():
        global intev
        if GPIO.input(18):
                if intev < 0.50:        
                        intev = intev + 0.01
                        print "intev "
                        print (intev)

        elif GPIO.input(11):
                if intev > 0.01:
                        intev = intev - 0.01
                        print "intev "
                        print (intev)

def forwards():
        global pin_out
        for this_out_pin in pin_out:
                checkin()
                GPIO.output(this_out_pin, False)
                time.sleep(intev)
                checkin()
                time.sleep(intev)
                GPIO.output(this_out_pin, True)
                checkin()               

def backwards():
        global pin_out
        for this_out_pin in reversed(pin_out):
                checkin()
                GPIO.output(this_out_pin, False)
                time.sleep(intev)
                checkin()               
                time.sleep(intev)
                GPIO.output(this_out_pin, True)         

def randomed():
        for r in range(0, 20):
                this_out_pin = choice(pin_out)
                if choice(ison) == 1 or 2:
                        if debug:
                                print "ON: ",(this_out_pin)
                        GPIO.output(this_out_pin, False)
                time.sleep(intev)
                if choice(ison) == 1:
                        if debug:
                                print "OFF: ",(this_out_pin)
                        GPIO.output(this_out_pin, True)

pin_out_setup()
pin_in_setup()

print "intev:", (intev)
for x in range(0, times):
        if debug:
                print (x) ,":",(times)

        forwards()
        checkin()
        randomed()
        checkin()
        backwards()
        checkin()
        randomed()
        checkin()

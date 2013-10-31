#!/usr/bin/env python

import RPi.GPIO as GPIO, time
import sys
import time
from random import choice

out_pin = [13,15,7,12,16,22]
for this_out_pin in out_pin:
        GPIO.setup(this_out_pin, GPIO.OUT)

in_pin = [11, 18]
for this_in_pin in in_pin:
        GPIO.setup(this_in_pin, GPIO.IN)

intev = 0.05
times = 1

while True:
	if GPIO.input(18):
		print "Button 18"
		for x in range(0, times):

        		for this_out_pin in out_pin:
                		print (this_out_pin)
                		GPIO.output(this_out_pin, False)
                		time.sleep(intev)
                		GPIO.output(this_out_pin, True)
                		time.sleep(intev)

	elif GPIO.input(11):
                print "Button 11"
                for x in range(0, times):
                
                        for this_out_pin in reversed(out_pin):
                                print (this_out_pin)
                                GPIO.output(this_out_pin, False)
                                time.sleep(intev)
                                GPIO.output(this_out_pin, True)
                                time.sleep(intev)
	else:
		print "Listen"
	time.sleep(0.1)

sys.exit()


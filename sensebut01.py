#!/usr/bin/env python

import RPi.GPIO as GPIO, time

in_pin = [11, 18]
for this_in_pin in in_pin:
        GPIO.setup(this_in_pin, GPIO.IN)

while True:
	if GPIO.input(18):
		print "Button 18"
	elif GPIO.input(11):
		print "Button 11"
	else:
		print "Listen"
	time.sleep(0.1)

#!/usr/bin/python3
# Script for shutting down RaspberryPI on  Button Press or event
# Timo Klinge

import os
import time
import RPi.GPIO as GPIO

# use broadcom pin numbers
# setup the pin with internal pullups enabled and pin in reading mode
PIN = 26 # change pin # accordingly

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

# define the shutdown function 

def shutdown(channel):
    print("Shutting Down!")
    time.sleep(5)
    os.system("sudo shutdown -h now")

# Add function to execute when Button is pressed

GPIO.add_event_detect(PIN, GPIO.FALLING, callback=shutdown, bouncetime=2000)

#Wait
while 1:
    time.sleep(1)


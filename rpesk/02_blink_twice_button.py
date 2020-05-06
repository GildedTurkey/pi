# 02_blink_twice.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

import RPi.GPIO as GPIO
import time
from gpiozero import Button

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)
red_pin1 = 18
red_pin2 = 23

GPIO.setup(red_pin1, GPIO.OUT)
GPIO.setup(red_pin2, GPIO.OUT)

button = Button(17)

try:
    while True:
        button.wait_for_press()
        GPIO.output(red_pin1, True)     # True means that LED turns on
        GPIO.output(red_pin2, True)    # False means that LED turns off
        button.wait_for_press()
        GPIO.output(red_pin1, False)
        GPIO.output(red_pin2, False)
finally:  
    print("Cleaning up")
    GPIO.cleanup()
    
    # You could get rid of the try: finally: code and just have the while loop
    # and its contents. However, the try: finally: construct makes sure that
    # when you CTRL-c the program to end it, all the pins are set back to 
    # being inputs. This helps protect your Pi from accidental shorts-circuits
    # if something metal touches the GPIO pins.

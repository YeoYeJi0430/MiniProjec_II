import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED = 23; GREEN = 25; BLUE = 24

GPIO.setup(RED,GPIO.OUT)
GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.output(BLUE,0)

try:
    while (True):
        GPIO.output(RED, 255)
        GPIO.output(GREEN, 0)
        GPIO.output(BLUE, 0)
        time.sleep(1)
        GPIO.output(RED, 0)
        GPIO.output(GREEN, 255)
        GPIO.output(BLUE, 0)
        time.sleep(1)
        GPIO.output(RED, 0)
        GPIO.output(GREEN, 0)
        GPIO.output(BLUE, 255)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
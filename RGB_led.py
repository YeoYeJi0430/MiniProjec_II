import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
RED = 25
GREEN = 23
BLUE = 24
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
try:
    while(True):
        GPIO.output(RED, 255)
        GPIO.output(GREEN, 0)
        GPIO.output(BLUE, 0)
        time.sleep(1)           #1s
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
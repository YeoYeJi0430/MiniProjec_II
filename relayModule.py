import RPi.GPIO as GPIO
import time

relay_pin = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

def switch_on(pin):
    GPIO.output(pin, GPIO.HIGH)

def switch_off(pin):
    GPIO.output(pin, GPIO.LOW)

#if __name__ == '__main__':
try:
    switch_on(relay_pin)
    time.sleep(5)
    switch_off(relay_pin)
    time.sleep(5)
    
except KeyboardInterrupt as ex:
    pass
finally:
    GPIO.cleanup()
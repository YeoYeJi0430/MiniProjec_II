import serial
import RPi.GPIO as GPIO

port = '/dev/ttyACM0'
brate = 9600 #boudrate
search = 'RESULT'
ser = serial.Serial(port, baudrate=brate, timeout=None)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
RED = 23; GREEN = 24; BLUE = 25
GPIO.setup(RED,GPIO.OUT); GPIO.output(RED,0)
GPIO.setup(GREEN,GPIO.OUT); GPIO.output(GREEN,0)
GPIO.setup(BLUE,GPIO.OUT); GPIO.output(BLUE,0)

def procValid(isOk):
    if isOk == True:
        GPIO.output(RED, GPIO.LOW)  
        GPIO.output(GREEN, GPIO.HIGH)       #출입 확인 - isOK -> green on
        print('Opened')
    elif isOk == False:
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(GREEN, GPIO.LOW)
        print('Not Opened')                 #red on -> 불법침입자!

while True:
    if ser.in_waiting != 0:
        content = ser.readline()
        content = content[:-2].decode('utf-8')
        if search in content:
            vals = content.split(':')
            if vals[1] == 'ON':
                procValid(True)
            else:
                procValid(False)
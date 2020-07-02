import serial

port = '/dev/ttyACM0'
brate = 9600
cmd = 'temp'

ser = serial.Serial(port, baudrate=brate, timeout=None)
print(ser.name)

while True:
    if ser.in_waiting != 0:
        content = ser.readline()
        print(content)

#카드 종류마다 uid가 달라서 구분 가능.
#라즈베리파이 코드에서 실행
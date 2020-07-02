import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import json
import time

def on_connect(client, userdata, flags, rc):    #연결됐을때 메시지
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):   #연결안됐을때메시지
    print(str(rc))

def on_subscribe(client, userdata, mid, granted_qos):
    print("subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    json_data = json.loads(str(msg.payload.decode("utf-8"))) #json으로 넘어온데이터를 디코더 해줘서 아래쪽처럼 배열로 들어감
    dev_id = json_data["dev_id"]    #my id
    state = json_data["state"]  #on/off
    
    if dev_id == 'YJYeo':
        print(dev_id)
        print(state)
        process_alarm(state)

def process_alarm(state):
    if state == 'ON':
        GPIO.output(RED, 255)   #이상상태일때 레드
        GPIO.output(GREEN, 0)
        GPIO.output(BLUE, 0)
    elif state == 'OFF':
        GPIO.output(RED, 0)
        GPIO.output(GREEN, 255) #정상일때 그린
        GPIO.output(BLUE, 0) 

# RGB LED 모듈 초기화
GPIO.setmode(GPIO.BCM)
RED = 25; GREEN = 23; BLUE = 24
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)

GPIO.output(RED,0)
GPIO.output(GREEN,255)
GPIO.output(BLUE,0)

try:
    # 새로운 클라이언트 생성
    client = mqtt.Client()
    # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_subscribe(topic 구독),
    # on_message(발행된 메세지가 들어왔을 때)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe
    client.on_message = on_message
    # address : localhost, port: 1883 에 연결
    client.connect('210.119.12.52', 1883)
    # common topic 으로 메세지 발행
    client.subscribe('home/device/control/', 1)
    client.loop_forever()
finally:
    GPIO.cleanup()
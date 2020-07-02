import paho.mqtt.client as mqtt
import Adafruit_DHT as dht
import json
import time
import datetime as dt
import uuid

from collections import OrderedDict

sensor = dht.DHT11
pin = 13
count = 0
try:
    dev_id = "YJYeo" # dev_id
    broker_address = "210.119.12.52"    #강사님pc ip
    client2 = mqtt.Client(dev_id)
    client2.connect(broker_address)
    while True:
        count+=1
        currtime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')   #ms표기
        #센서값 가져오기
        h, t = dht.read_retry(sensor, pin)
        #groupdata 만들기
        raw_data = OrderedDict()
        raw_data["dev_id"] = dev_id
        raw_data["time"] = currtime
        raw_data["temp"] = "{0:0.1f}".format(t)
        raw_data["humid"] = "{0:0.1f}".format(h)

        pub_data = json.dumps(raw_data, ensure_ascii=False, indent="\t") #(,아스키로 변환안하겠다,들여쓰기는 t)

        #mqtt published
        print(dev_id, pub_data)
        client2.publish("home/device/data/", pub_data)                  #강사님 컴퓨터의 해당 경로로 데이터 감.
        time.sleep(5)
except Exception as ex:
    print("Error raised", ex) #에러 알려줌

#온습도 데이터 강사님 컴터로 ㄱㄱ

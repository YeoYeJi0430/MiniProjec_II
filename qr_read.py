import pyzbar.pyzbar as pyzbar
import cv2
import serial
import time

cap = cv2.VideoCapture(0)
count = 0
port = '/dev/ttyACM0'
brate = 9600
ser = serial.Serial(port, baudrate=brate, timeout=None)
print(ser.name)
# PKNU2020Fighting!!
hashVal = 'D67C69FFACCF947DBEAD024F8FF722D0'

def procQrcode(data):
    global count # 얘는 글로벌, 함수에서 쓰고 싶을때 global 사용
    count = count + 1
    if data == hashVal:
        ser.write(b'1') #아두이노쪽으로 데이터 전달(b <= 바이트)
    else:
        ser.write(b'2') #잘못됐을때 2
    
    count = 0

i = 0
while (cap.isOpened()):
    ret, img = cap.read()

    if not ret:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    decoded = pyzbar.decode(gray)
    qrcode_data = ''

    for d in decoded:
        x, y, w, h = d.rect

        qrcode_data = d.data.decode("utf-8")
        qr_type = d.type

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        text = '%s (%s)' % (qrcode_data, qr_type)
        # print("{}".format(qrcode_data))
        cv2.putText(img, text, (x, y), cv2.FONT_ITALIC,
                    1, (0, 255, 255), 2, cv2.LINE_AA)
        if count == 0:
            procQrcode(qrcode_data)

    cv2.imshow('img', img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        i += 1
        # print("{}".format(qrcode_data))
        cv2.imwrite('D:\\c_%03d.jpg' % i, img)

cap.release()
cv2.destroyAllWindows()
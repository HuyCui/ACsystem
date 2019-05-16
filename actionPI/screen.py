import serial
from time import sleep
import time

def wirte_time(serial):
    ti = 0
    
    while True:
        serial.write(b"CLS(3);\r\n")
        serial.write("DS48(1,2,'action  ".encode('utf-8')+str(ti).encode('utf-8')+"s',1);\r\n".encode('utf-8'))
        time.sleep(0.5)
        ti = ti +0.5


def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data

if __name__ == '__main__':
    serial = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)  #/dev/ttyUSB0
    if serial.isOpen() :
        print("open success")
    else :
        print("open failed")
    #serial.write("CLS(3);\r\n".encode('utf-8'))
    wirte_time(serial)
    

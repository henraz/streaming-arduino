import serial
import time
from datetime import datetime

arduino = serial.Serial('/dev/ttyUSB0', 9600)

info_leitura = {"lux":'',
                "temperatura":'',
                "umidade":'',
                "data": ''}

while True:
    if arduino.inWaiting() > 0:
        data = arduino.readline().decode('utf-8').strip().split(",")
        info_leitura["lux"] = data[0]
        info_leitura["temperatura"] = data[1]
        info_leitura["umidade"] = data[2]
        info_leitura["data"] = datetime.now().isoformat(sep=" ")
        print(info_leitura)

    time.sleep(10)
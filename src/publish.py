import json
import serial
import time
from datetime import datetime
from google.cloud import pubsub_v1

def main():
    
    PROJECT_ID = "project-id"
    TOPIC_ID = "topic-name"

    info_dict = {"lux":'',
            "temperatura":'',
            "umidade":'',
            "data_sensor": ''}

    publisher = pubsub_v1.PublisherClient()
    topic = publisher.topic_path(PROJECT_ID, TOPIC_ID)

    arduino = serial.Serial('/dev/ttyUSB0', 9600)

    while True:

        if arduino.inWaiting() > 0:
            data_arduino = arduino.readline().decode('utf-8').strip().split(",")
            info_dict["lux"] = data_arduino[0]
            info_dict["temperatura"] = data_arduino[1]
            info_dict["umidade"] = data_arduino[2]
            info_dict["data_sensor"] = datetime.now().isoformat(sep=" ")

            data_publish = json.dumps(info_dict).encode("utf-8")
            future = publisher.publish(topic, data_publish)
            print(f"Mensagem publicada em {topic}.")

        time.sleep(10)

if __name__ == '__main__':
    main()
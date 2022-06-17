from time import sleep
import psutil
from datetime import datetime
from kafka import KafkaProducer
from json import dumps
import os
import random

def get_log():
    d = dict()
    d["measurement"] = os.environ.get('DOCKER_INFLUXDB_INIT_ORG')
    d["timestamp"] = int(datetime.utcnow().timestamp()*1e3)
    d["ram"] = dict(psutil.virtual_memory()._asdict())
    d["cpu"] = psutil.cpu_percent()
    d["sensor"] = os.environ.get('COMPUTERNAME')
    return d

if __name__ == '__main__':
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'], value_serializer=lambda x: dumps(x).encode('utf-8'))

    for i in range(1000):
        print("sending message", flush=True)
        producer.send(os.environ.get('TOPIC'), value=get_log())
        sleep(5)
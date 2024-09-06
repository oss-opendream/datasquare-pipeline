import socket

import time
from confluent_kafka import Producer
from logs_dummy_data import generate_dummy_log

if __name__ == '__main__':

    config = {
            'bootstrap.servers': 'server1:9092, server2:9092, server3:9092',
        'client.id': socket.gethostname(),
    }

    # Create Producer instance
    producer = Producer(config)
    
    # Produce data by selecting random values from these lists.
    topic = "daily_log"
    logfile = "20240902_logs.txt"

    # 파일 읽는 코드
    # with open(file=logfile, mode='r') as f:
    #     for line in f:
    #         producer.produce(topic, line[:-2])
    #         producer.poll(10000)
    #         producer.flush()

    # 바로 이슈 생성 후 던지기 
    while True:
        line = generate_dummy_log()
        producer.produce(topic, line)
        producer.poll(10000)
        producer.flush()

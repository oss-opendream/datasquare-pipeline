import socket
import time

from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic

from logs_dummy_data import generate_dummy_log

if __name__ == '__main__':

    config = {
            'bootstrap.servers': 'server1:9092, server2:9092, server3:9092',
        'client.id': socket.gethostname(),
    }

    # Produce data by selecting random values from these lists.
    topic = "datasquare_web_log_test"

    # Check Topic
    admin = AdminClient(config)
    topic_dict = admin.list_topics().topics

    if topic in topic_dict:
        pass
    else:
        admin.create_topics([NewTopic(topic, num_partitions=3, replication_factor=3)])
        time.sleep(2)

    # Create Producer instance
    producer = Producer(config)

    # 바로 이슈 생성 후 던지기 
    i = 0
    while True:
        i += 1
        line = generate_dummy_log()
        producer.produce(topic, line)
        producer.poll(10000)
        producer.flush()
        if i%100 == 0:
            print(i)
        

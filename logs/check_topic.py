import socket

import time
from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic

if __name__ == '__main__':

    config = {
            'bootstrap.servers': 'server1:9092, server2:9092, server3:9092',
        'client.id': socket.gethostname(),
    }

    # Create Producer instance
    producer = Producer(config)
    conf = {'bootstrap.servers': 'server1:9092,server2:9092,server3:9092'}
    kadmin = AdminClient(conf)
    topic_dict = kadmin.list_topics().topics

    topic_name = "yoonjae2"

    if topic_name in topic_dict:
        print("yes")
        pass
    else:
        print("no")
        new_topic = kadmin.create_topics([NewTopic(topic_name, num_partitions=3, replication_factor= 3)])
import socket
import time

from confluent_kafka.admin import AdminClient, NewTopic

if __name__ == '__main__':
    conf = {'bootstrap.servers': 'server1:9092, server2:9092, server3:9092'}
    kadmin = AdminClient(conf)
    topic_dict = kadmin.list_topics().topics

    topic_name = 'datasquare_web_log'

    while len(topic_dict) <= 1:
        print('Bootstrap servers are not ready yet. \nRetry after 5 seconds')
        time.sleep(5)
        kadmin = AdminClient(conf)
        topic_dict = kadmin.list_topics().topics

    if topic_name in topic_dict:
        print(f"'{topic_name}' topic found")

    else:
        print(f"'{topic_name}' topic not found. \nNew topic '{topic_name}' will be created.")
        new_topic = kadmin.create_topics([NewTopic(topic_name, num_partitions=3, replication_factor= 3)])

    time.sleep(5)
    topic_dict = kadmin.list_topics().topics
    print(topic_dict.keys())
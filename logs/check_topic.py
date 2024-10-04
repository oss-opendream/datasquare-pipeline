import os
import time

from confluent_kafka.admin import AdminClient, NewTopic

import yaml

if __name__ == '__main__':
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 스크립트가 위치한 디렉토리
        config_path = os.path.join(script_dir, 'kafka_config.yaml')
        
        with open(f"{config_path}", 'r') as file:
            properties = yaml.safe_load(file)
            TOPIC_NAME = properties['TOPIC_NAME']
            BROKER_NUMBER = properties['BROKER_NUMBER']
            BOOTSTRAP_SERVER = properties['BOOTSTRAP_SERVER']

    except FileNotFoundError as e:
        print(e)
        TOPIC_NAME = "datasquare_web_log"
        BROKER_NUMBER = 3
        BOOTSTRAP_SERVER = 'kafka1:9092, kafka2:9092, kafka3:9092'

    conf = {'bootstrap.servers': BOOTSTRAP_SERVER}
    kadmin = AdminClient(conf)
    # 클러스터 메타데이터 추출
    metadata = kadmin.list_topics()
    
    print("_______________________________________")
    while len(metadata.brokers) < BROKER_NUMBER:
        print(f"Found bootstrap servers: {metadata.brokers}")
        print('Bootstrap servers are not ready yet. \nRetry after 5 seconds')
        time.sleep(5)
        metadata = kadmin.list_topics()

    if TOPIC_NAME in metadata.topics:
        print(f"'{TOPIC_NAME}' topic found")
    else:
        print(f"'{TOPIC_NAME}' topic not found. \nNew topic '{TOPIC_NAME}' will be created.")
        time.sleep(2)
        new_topic = kadmin.create_topics([NewTopic(TOPIC_NAME, num_partitions=3, replication_factor= 3)])
        print("Make topic~!")
    
    time.sleep(5)
    topic_dict = kadmin.list_topics().topics
    print(topic_dict.keys())

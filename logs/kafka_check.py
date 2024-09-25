import socket
import time

from confluent_kafka.admin import AdminClient, NewTopic, TopicMetadata
import configparser as parser


if __name__ == '__main__':
    properties = parser.ConfigParser()
    try:
        properties.read('./kafka_config.ini')
    except FileNotFoundError as e:
        print(e)
        TOPIC_NAME = "datasquare_web_log2"
        BROKER_NUMBER = 3
        BOOTSTRAP_SERVER = 'server1:9092, server2:9092, server3:9092'
        



    TOPIC_NAME = properties['TOPIC']['topic_name']
    BROKER_NUMBER = properties['BROKER']['broker_number']
    BOOTSTRAP_SERVER = properties['BOOTSTRAP_SERVER']['bootstrap_server']
    
    conf = {'bootstrap.servers': BOOTSTRAP_SERVER}
    kadmin = AdminClient(conf)
    # topic_dict = kadmin.list_topics().topics
    metadata = kadmin.list_topics()
    # for broker in metadata.brokers:
    #     print(broker)
    #     print(metadata.brokers)

    # topic_name = 'datasquare_web_log'


    # print(topic_name, broker_number)
    # while len(topic_dict) <= 1:
    #     print('Bootstrap servers are not ready yet. \nRetry after 5 seconds')
    #     time.sleep(5)
    #     kadmin = AdminClient(conf)
    #     topic_dict = kadmin.list_topics().topics

    # if topic_name in topic_dict:
    #     print(f"'{topic_name}' topic found")

    # else:
    #     print(f"'{topic_name}' topic not found. \nNew topic '{topic_name}' will be created.")
    #     new_topic = kadmin.create_topics([NewTopic(TOPIC_NAME, num_partitions=3, replication_factor= 3)])

    # time.sleep(5)
    # topic_dict = kadmin.list_topics().topics
    # print(topic_dict.keys())
    print(kadmin.list_consumer_groups())
    # print(dir(kadmin.list_consumer_groups()))
    print(kadmin.describe_cluster())
    print("_______________________________________")
    



    # 클러스터 메타데이터 추출
    metadata = kadmin.list_topics(timeout=10)
    # 브로커 상태 출력
    print("\nKafka 클러스터 브로커 상태:")
    for broker_id, broker in metadata.brokers.items():
        print(f"Broker ID: {broker.id}, Host: {broker.host}, Port: {broker.port}, ")

    # 주제 및 파티션 정보 출력
    print("\nKafka 클러스터에 있는 주제들:")
    for topic_name, topic_metadata in metadata.topics.items():
        partition_count = len(topic_metadata.partitions)
        print(f"Topic: {topic_name}, Partition Count: {partition_count}")


        

    # 클러스터 메타데이터 요약
    print(f"\n클러스터에 있는 브로커 수: {len(metadata.brokers)}")
    print(f"클러스터에 있는 주제 수: {len(metadata.topics)}")

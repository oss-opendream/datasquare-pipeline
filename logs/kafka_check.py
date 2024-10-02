from confluent_kafka.admin import AdminClient
import configparser as parser


if __name__ == '__main__':
    properties = parser.ConfigParser()
    try:
        properties.read('./kafka_config.ini')
    except FileNotFoundError as e:
        print(e)
        TOPIC_NAME = "datasquare_web_log"
        BROKER_NUMBER = 3
        BOOTSTRAP_SERVER = 'kafka1:9092, kafka2:9092, kafka3:9092'
        



    TOPIC_NAME = properties['TOPIC']['topic_name']
    BROKER_NUMBER = properties['BROKER']['broker_number']
    BOOTSTRAP_SERVER = properties['BOOTSTRAP_SERVER']['bootstrap_server']
    
    conf = {'bootstrap.servers': BOOTSTRAP_SERVER}
    kadmin = AdminClient(conf)
    # topic_dict = kadmin.list_topics().topics
    metadata = kadmin.list_topics()
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

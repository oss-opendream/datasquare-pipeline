import configparser
import os
import socket

from confluent_kafka import Consumer
from minio import Minio

from enhanced_rotating_handler import EnhancedRotatingFileHandler


if __name__ == '__main__':

    # Set Kafka configuration
    kafka_config = {
        'bootstrap.servers': 'server2:9092',
        'client.id': socket.gethostname(),
    }

    # Read MinIO Configuration file
    parser = configparser.ConfigParser()
    parser.read('datasquare_kafka2minio.conf')
    access_key = parser.get("MINIO_CREDENTIALS",
                            "ACCESS_KEY")
    secret_key = parser.get("MINIO_CREDENTIALS",
                            "SECRET_KEY")
    bucket_name = parser.get("MINIO_CREDENTIALS",
                             "BUCKET")

    # Create MinIO instance
    minio = Minio('localhost:9000',
                  access_key=access_key,
                  secret_key=secret_key,
                  secure=False)

    # Create Consumer instance
    consumer = Consumer(kafka_config)

    # Consume data
    topics = ["daily_log"]

    consumer.subscribe(topics)

    while True:
        file_dir = 'temp'
        file_name = 'datasquare_log'

        file_path = os.path.join(file_dir, file_name)
        rot_file_handler = EnhancedRotatingFileHandler(
            filename=file_name, when='m', interval=1, maxBytes=50*1024*1024)

        if not os.path.exists(file_dir):
            os.mkdir(file_dir)

        msg = consumer.poll(1.0)

        # MinIO object storage에 저장

        object_name = ''

        minio.fput_object(bucket_name=bucket_name,
                          object_name=object_name,
                          file_path=file_path)

import configparser
import os
import socket
import re
import json

from confluent_kafka import Consumer
from minio import Minio
from file_rotator import FileRotator


def parse_datetime_from_message(message):
    """
    메시지에서 날짜와 시간 부분을 파싱합니다.
    예: [03/Sep/2024:00:42:10 ] -> 20240903_004210
    """
    match = re.search(r'\[(\d{2})/(\w{3})/(\d{4}):(\d{2}:\d{2}:\d{2})', message)
    if match:
        day, month, year, time = match.groups()
        month_map = {
            'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
            'May': '05', 'Jun': '06',
            'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10',
            'Nov': '11', 'Dec': '12'
        }
        month = month_map[month]
        return f"{year}{month}{day}_{time.replace(':', '')}"
    return "unknown_datetime"


if __name__ == '__main__':

    # Set Kafka configuration
    kafka_config = {
        'bootstrap.servers': 'server1:9092,server2:9092,server3:9092',
        'client.id': socket.gethostname(),
        'group.id': 'datasquare_minio',  # 추가
        'auto.offset.reset': 'earliest'   # 추가
    }

    # Read MinIO Configuration file
    parser = configparser.ConfigParser()
    parser.read('./datasquare_kafka2minio.conf')
    access_key = parser.get("MINIO_CREDENTIALS", "ACCESS_KEY")
    secret_key = parser.get("MINIO_CREDENTIALS", "SECRET_KEY")
    bucket_name = parser.get("MINIO_CREDENTIALS", "BUCKET")

    # Create MinIO instance
    minio_client = Minio('server3:9000',
                         access_key=access_key,
                         secret_key=secret_key,
                         secure=False)

    # Create Consumer instance
    consumer = Consumer(kafka_config)
    topics = ["datasquare_web_log2"]
    consumer.subscribe(topics)

    # File management setup
    file_dir = 'temp'
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)

    current_file_name = None
    rot_file_handler = None

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            consumed_message = msg.value().decode('utf-8')
            try:
                message_value = json.loads(consumed_message)['message']
                print(message_value)
                
                if current_file_name is None:
                    # 첫 번째 메시지에서 파일 이름을 결정합니다.
                    datetime_str = parse_datetime_from_message(message_value)
                    current_file_name = f"{datetime_str}_datasquare.log"
                    file_path = os.path.join(file_dir, current_file_name)
                    rot_file_handler = FileRotator(
                        base_filename=file_path, interval_seconds=30, max_bytes=50*1024*1024)
                    
                # 메시지를 파일에 씁니다.
                if rot_file_handler.write(message_value + "\n"):
                
                    # 회전된 파일을 MinIO에 업로드합니다.
                    minio_client.fput_object(bucket_name=bucket_name,
                                            object_name=current_file_name,
                                            file_path=file_path)

                    # 기존 파일 이름을 초기화합니다.
                    current_file_name = None
            except:
                pass

    except KeyboardInterrupt:
        print("Kafka consumer interrupted.")
    finally:
        # Clean up
        consumer.close()
        if rot_file_handler:
            rot_file_handler.close()

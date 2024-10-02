#!/bin/bash

# 서버 배열
servers=( \
  "ds-db" \
  "ds-server" \
  "kafka1" \
  "kafka2" \
  "kafka3" \
  "minio" \
  "elk" \
  )


# 서버에 맞는 compose 파일 배열
compose_files=( \
  "docker-compose-server-ds_db.yml" \
  "docker-compose-server-ds_server.yml" \
  "docker-compose-server-kafka1.yml" \
  "docker-compose-server-kafka2.yml" \
  "docker-compose-server-kafka3.yml" \
  "docker-compose-server-minio.yml" \
  "docker-compose-server-prom_elk.yml" \
  )

# 반복문을 사용하여 서버별로 docker-compose 명령 실행
for i in ${!servers[@]}; do
  echo "Docker composing ${servers[$i]} up..."
  DOCKER_CMD="docker compose -f ~/datasquare-pipeline/docker/yml/server/${compose_files[$i]} up -d"
  ssh ${servers[$i]} "$DOCKER_CMD"
done

# -o 옵션을 넣으면 kafka4 
while getopts "a" opt; do
    case $opt in
        a)
            echo "Docker composing kafka4 up..."
            DOCKER_CMD="docker compose -f ~/datasquare-pipeline/docker/yml/server/docker-compose-server-kafka4.yml up -d"
            ssh kafka "$DOCKER_CMD"
            ;;
    esac
done


# Kafka Topic 생성 Python script 실행
/usr/local/pyenv/versions/ds_env/bin/python ~/datasquare-pipeline/logs/check_topic.py

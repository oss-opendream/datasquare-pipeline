#!/bin/bash

# 서버 배열
servers=("kafka1" "kafka2" "kafka3" "kafka4")

# 서버에 맞는 compose 파일 배열
compose_files=("docker-compose-server1.yml" "docker-compose-server2.yml" "docker-compose-server3.yml" "docker-compose-server4.yml")

# 반복문을 사용하여 서버별로 docker-compose 명령 실행
for i in ${!servers[@]}; do
  echo "Docker composing server[$((i+1))] up..."
  DOCKER_CMD="docker compose -f ~/datasquare-pipeline/docker/yml/${compose_files[$i]} up -d"
  ssh ${servers[$i]} "$DOCKER_CMD"
done

# Kafka Topic 생성 Python script 실행
~/.pyenv/versions/ds_env/bin/python ~/datasquare-pipeline/logs/check_topic.py

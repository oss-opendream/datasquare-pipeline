#!/bin/bash

# 서버 배열
servers=( \
  "kafka1" \
  "kafka2" \
  "kafka3" \
  # "ds-server" \
  # "prom-elk" \
  # "minio1" \
  )

# 서버에 맞는 compose 파일 배열
compose_files=( \
  "docker-compose-server1.yml" \
  "docker-compose-server2.yml" \
  "docker-compose-server3.yml" \
  "docker-compose-server-filebeat.yml" \
  "docker-compose-server-prom-elk.yml" \
  "docker-compose-server-minio.yml" \
  )
  
# 반복문을 사용하여 서버별로 docker-compose 명령 실행
for i in ${!servers[@]}; do
  echo "Docker composing server[$((i+1))] down..."
  DOCKER_CMD="docker compose -f ~/datasquare-pipeline/docker/yml/${compose_files[$i]} down"
  ssh ${servers[$i]} "$DOCKER_CMD"
done

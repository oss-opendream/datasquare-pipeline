#!/bin/bash
# 서버 배열
servers=("server1" "server2" "server3")

# 서버에 맞는 compose 파일 배열
compose_files=("docker-compose-server1.yml" "docker-compose-server2.yml" "docker-compose-server3.yml")

# 반복문을 사용하여 서버별로 docker-compose 명령 실행
for i in ${!servers[@]}; do
  echo "Docker composing server[$i] down..."
  DOCKER_CMD="docker compose -f ~/datasquare-pipeline/docker/yml/${compose_files[$i]} down"
  ssh ${servers[$i]} "$DOCKER_CMD"
done

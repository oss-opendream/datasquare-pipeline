#!/bin/bash

#DOCKER RUN CMD
DOCKER_CMD="docker compose -f ~/datasquare-pipeline/docker/kafka.yml up -d"

ssh server1 "$DOCKER_CMD"
ssh server2 "$DOCKER_CMD"
ssh server3 "$DOCKER_CMD"

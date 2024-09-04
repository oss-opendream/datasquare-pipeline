#!/bin/bash

#DOCKER DOWN CMD
DOCKER_CMD="docker compose -f ~/datasquare-pipeline/docker/kafka.yml down"

ssh server1 "$DOCKER_CMD"
ssh server2 "$DOCKER_CMD"
ssh server3 "$DOCKER_CMD"

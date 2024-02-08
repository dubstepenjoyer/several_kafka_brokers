#!/bin/bash

python3 preparation.py

sudo docker-compose up -d

echo "Wait for 30 seconds till Kafka cluster will start"  
  
sleep 30

python3 create_topic.py
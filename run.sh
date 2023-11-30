#!/bin/bash

if [[ -v IP ]]; then
    echo "IP already set"
else
    python3 preparation.py
fi

docker-compose up -d

echo "Wait for 10 seconds till Kafka cluster will start"  
  
sleep 10s 

python3 create_topic.py
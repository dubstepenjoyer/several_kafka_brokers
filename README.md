# several kafka brokers

Project with 3 kafka brokers in docker containers

Most popular kafka-administration CLI commands

Before to start you need to download kafka sh-files (check Apache Kafka official website)

Check topics in cluster: 
```
./bin/kafka-topics.sh --bootstrap-server {ip}:{port} --list
```


Topic Details:
```
./bin/kafka-topics.sh --bootstrap-server {ip}:{port} --describe --topic {topic_name}
```


Create topic:
```
./bin/kafka-topics.sh --create --topic {topic_name} --bootstrap-server {ip}:{port}
```

Delete topic:
```
./bin/kafka-topics.sh --delete --topic {topic_name} --bootstrap-server {ip}:{port}
```

Write in topic:
```
./bin/kafka-console-producer.sh --topic {topic_name} --bootstrap-server {ip}:{port}
```

Read from topic:
```
./bin/kafka-console-consumer.sh --topic {topic_name} --bootstrap-server {ip}:{port}
```
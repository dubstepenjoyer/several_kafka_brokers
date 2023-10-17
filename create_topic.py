from kafka.admin import KafkaAdminClient, NewTopic


admin = KafkaAdminClient(
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'], 
    client_id='admin'
)

topic_list = [
    NewTopic(name='cluster-logs', num_partitions=3, replication_factor=3),
    NewTopic(name='callbacks', num_partitions=3, replication_factor=3),
    NewTopic(name='stream-links', num_partitions=3, replication_factor=3),
    NewTopic(name='create-process', num_partitions=3, replication_factor=3),
    NewTopic(name='process-changes', num_partitions=3, replication_factor=3),
    NewTopic(name='test', num_partitions=3, replication_factor=3)
    ]

admin.create_topics(new_topics=topic_list)

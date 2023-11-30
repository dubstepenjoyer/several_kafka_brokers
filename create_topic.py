from kafka.admin import KafkaAdminClient, NewTopic


admin = KafkaAdminClient(
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'], 
    client_id='admin'
)

topics_names = ['cluster-logs', 'callbacks', 'stream-links', 'create-process', 'process-changes', 'test']

topics_to_create = []

admin_response = admin.list_topics()

for topic_name in topics_names:
    if topic_name not in admin_response:
        topics_to_create.append(NewTopic(name=topic_name, num_partitions=3, replication_factor=3))

if topics_to_create:
    admin.create_topics(new_topics=topics_to_create)

from kafka.admin import KafkaAdminClient, NewTopic


admin = KafkaAdminClient(
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'], 
    client_id='admin'
)

topic_list = [
    NewTopic(name='cluster-logs'),
    NewTopic(name='callbacks'),
    NewTopic(name='stream-links'),
    NewTopic(name='create-process'),
    NewTopic(name='process-changes'),
    NewTopic(name='test')
    ]

admin.create_topics(new_topics=topic_list)

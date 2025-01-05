# test_kafka_producer.py
from kafka import KafkaProducer
import json

def send_to_kafka(topic, data):
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(topic, data)
    producer.flush()

# Test the producer
send_to_kafka('test_topic', {'message': 'Hello, Kafka!'})
print("Message sent to Kafka.")

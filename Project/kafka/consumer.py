from kafka import KafkaConsumer
import json

def consume_from_kafka(topic):
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'],
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    for message in consumer:
        data = message.value
        # Process the data and send it to the recommendation model
        print(f"Received data: {data}")

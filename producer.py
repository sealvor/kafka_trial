from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_server=["localhost:9092"])

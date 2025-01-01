from kafka import KafkaProducer
import csv
import time

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send data to Kafka
with open('ecommerce_churn.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header
    for row in reader:
        producer.send('ecommerce-data2', value=','.join(row).encode('utf-8'))
        print(f"Sent: {row}")
        time.sleep(0.1)  # Simulate streaming

producer.close()

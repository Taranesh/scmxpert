# pylint: disable=broad-except
'''importing packages'''
import os
import json
import pymongo
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from dotenv import load_dotenv
load_dotenv()

# Connect to MongoDB
CLIENT = pymongo.MongoClient(os.getenv("mongodbUri"))
DB = CLIENT['scmxpertlite']
DATA_STREAM = DB["datastream"]

# Set up Kafka consumer
BOOTSTRAP_SERVERS = "localhost:9092"

try:
# Creates a Kafka consumer instance and subscribes to the 'Taranesh' topic.\
# If successful, prints a message 'Starting the Consumer'. If an exception occurs,\
# prints an error message with the details of the exception.
    CONSUMER = KafkaConsumer(
        'Taranesh',
        BOOTSTRAP_SERVERS=BOOTSTRAP_SERVERS,
        auto_offset_reset='latest',
        group_id='group-A')
    print("Starting the Consumer\n")

# if the consumer is unable to connect to the Kafka server due to a network issue,\
#  such as a firewall block or network outage
except ConnectionError as exception:
    raise ConnectionError(f"Failed to connect to Kafka server: {exception}") from exception

#if the consumer is unable to establish a connection to the Kafka server\
#  within a specified time limit.
except TimeoutError as exception:
    raise TimeoutError(f"Timed out while connecting to Kafka server: {exception}") from exception

#if an unknown or unexpected error occurs during the creation of the consumer.
except KafkaError as exception:
    print(f"Failed to create Kafka consumer: {exception}")


try:
    for data in CONSUMER:
        try:
            if data != None:
                print("Data received from kafka\n")
                print(json.loads(data.value))
                DATA_STREAM.insert_one(json.loads(data.value))
                print("Data sended to Database\n")
        except json.JSONDecodeError as exception:
            print(f"Failed to parse JSON message: {exception}")
        except Exception as exception:
            print(f"Failed to save message to MongoDB: {exception}")
except KeyboardInterrupt:
    print("Consumer interrupted by user")
except Exception as exception:
    print(f"Consumer error: {exception}")
finally:
    CONSUMER.close()

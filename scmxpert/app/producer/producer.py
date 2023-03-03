# pylint: disable=broad-except
"""
importing packages
"""
import socket
import os
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv()

socket_connection = socket.socket()
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")             
socket_connection.connect((HOST, int(PORT)))
bootstrap_servers =os.getenv("bootstrap_servers")


producer = KafkaProducer(bootstrap_servers=bootstrap_servers, retries=5)

topicName = os.getenv("topic_name")

while True:
    try:
        data=socket_connection.recv(70240)
        print(data)
        producer.send(topicName, data)

    except Exception as exception:
        print(exception)
socket_connection.close()
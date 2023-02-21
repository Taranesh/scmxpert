# pylint: disable=broad-except
from ensurepip import bootstrap
import socket    
import json 
import os
from pathlib import Path
from dotenv import load_dotenv
from kafka import KafkaProducer

BASE_DIR = Path(__file__).resolve().parent
load_dotenv()

SOCKET_CONNECTION = socket.socket()
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")             
SOCKET_CONNECTION.connect((HOST, int(PORT)))
BOOTSTRAP_SERVERS = "localhost:9092"


PRODUCER = KafkaProducer(BOOTSTRAP_SERVERS=BOOTSTRAP_SERVERS, retries=5)

topicName = "Taranesh"

while True:
    try:
        DATA = SOCKET_CONNECTION.recv(70240)
        # Check if data is not empty

        # json_acceptable_string = data.replace("'", "\"")
        # load_data = json.loads(json_acceptable_string)
        # print(load_data)
        # for data in load_data:
        PRODUCER.send(topicName, DATA)

    except json.JSONDecodeError as json_error:
        # Invalid JSON data received when the JSON data received from the socket is
        #  not in the correct format. We catch this exception and print an error message
        print("Error decoding JSON data: ", json_error)
    except Exception as exception:
        # Other exceptions catch-all exception that will handle any other exceptions that
        # may occur during the execution of the code
        print("Error occurred: ", exception)
    SOCKET_CONNECTION.close()

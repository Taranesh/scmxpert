import socket   
import os 
import time    
import pymongo   
import json 
import sys
from kafka import KafkaConsumer
from dotenv import load_dotenv
load_dotenv()


CLIENT = pymongo.MongoClient(os.getenv("mongodbUri"))
DB = CLIENT['scmxpertlite']
DATA_STREAM = DB["datastream"]

topicName = os.getenv("topic_name")    
print(topicName)
bootstrap_servers= os.getenv("bootstrap_servers")
try:
    consumer = KafkaConsumer(topicName, bootstrap_servers=bootstrap_servers, auto_offset_reset='latest')
    for data in consumer:
        try:
            data = json.loads(data.value)
            print(data)
            mdata = DATA_STREAM.insert_one(data)
        except json.decoder.JSONDecodeError:
            continue
except KeyboardInterrupt:
    sys.exit()


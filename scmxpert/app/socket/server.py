# pylint: disable=broad-except
import socket
import json
import time

socket_connection = socket.socket()
socket_connection.bind(('',12345))
socket_connection.listen(3)
client, address = socket_connection.accept()

data = {"Battery_Level":3.52, "Device_Id":1156053076, "First_Sensor_temperature":19.4 , "Route_From":"Hyderabad, India", "Route_To":"Louisville, USA"}
while True:
    try:
        userdata = (json.dumps(data)+"\n").encode('utf-8')
        client.send(userdata)
        time.sleep(1)
    except Exception as exception:
        client.close()

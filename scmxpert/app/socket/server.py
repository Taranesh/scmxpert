import socket
import json
import time
try:
    s = socket.socket()
    print("Socket Created")
    s.bind(('',12345))
    s.listen(3)
    print("waiting for connections")
    c, addr = s.accept()

    data = {"Battery_Level":3.52, "Device_Id":1156053076, "First_Sensor_temperature":19.4 , "Route_From":"Hyderabad, India", "Route_To":"Louisville, USA"}


    while True:
        try:
            print("connected with", addr)
            userdata = (json.dumps(data)+"\n").encode('utf-8')
            print(userdata)
            c.send(userdata)
            time.sleep(100)
        except socket.error as e:
            print(f"Socket error occurred: {e}")
            c.close()
            break
        except json.JSONDecodeError as e:
            print(f"JSON decoding error occurred: {e}")
            c.close()
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            c.close()
            break
except socket.error as e:
    print(f"Socket error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
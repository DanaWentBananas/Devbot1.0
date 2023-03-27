import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

#env variables
load_dotenv()
robotID = os.getenv("robot_id")

#topics
topics = ["move/"+robotID,"configure/"+robotID, "test"]

#functions
def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print("Connected to broker!")
        for topic in topics:
            client.subscribe(topic)
    else:
        print("Connection failed with error code %s" % rc)

def on_message(client,userdata,message):
    if(message.topic == "move/"+robotID):
        print(message.payload.decode())
    elif(message.topic == "configure/"+robotID):
        print(message.payload.decode())
    elif(message.topic == "test"):
        print(message.payload.decode())


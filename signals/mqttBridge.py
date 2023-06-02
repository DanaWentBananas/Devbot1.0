import paho.mqtt.client as mqtt
import os
from dotenv import Dotenv
from mind import mqttHandler
dotenv = Dotenv('/home/pi/Devbot1.0/.env') 
os.environ.update(dotenv)

robotID = os.getenv("robot_id")
broker = os.getenv("mqtt_broker")
name = os.getenv("mqtt_username")
pswd = os.getenv("mqtt_pwd")
topics = ["move/"+robotID,"configure/"+robotID, "move"]

class mqttBridge:
    def __init__(self):
        self.client = mqtt.Client(client_id=robotID)
        self.client.username_pw_set(name,pswd)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker)
        self.client.publish("move","HI")
        
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker!")
            for topic in topics:
                client.subscribe(topic)
        else:
            print("Connection failed with error code %s" % rc)
        
    def on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        mqttHandler.handle(message)
        
    def start(self):
        self.client.loop_start()
        
    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()

    def keepgoing(self):
        self.client.loop_forever()

import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

load_dotenv()
robotID = os.getenv("robot_id")
broker = os.getenv("mqtt_broker")
name = os.getenv("mqtt_username")
pswd = os.getenv("mqtt_pwd")
topics = ["move/"+robotID,"configure/"+robotID, "move"]

class MQTTHandler:
    def __init__(self, car):
        self.car = car
        self.client = mqtt.Client(client_id=robotID)
        self.client.username_pw_set(name,pswd)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(broker)
        
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker!")
            for topic in topics:
                client.subscribe(topic)
        else:
            print("Connection failed with error code %s" % rc)
        
    def on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        if message == "1":
            #self.car.forward()
            print("moving forward")
        elif message == "2":
            #self.car.turn_left()
            print("turning left")
        elif message == "3":
            #self.car.turn_right()
            print("turning right")
        elif message == "4":
            print("reverse")
        elif message == "stop":
            #self.car.stop()
            print("stop")
        else:
            print("Invalid message: "+message)
        
    def start(self):
        self.client.loop_start()
        
    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()

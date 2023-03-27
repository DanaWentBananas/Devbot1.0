import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
import util

#enviroment variables
load_dotenv()
broker = os.getenv("mqtt_broker")
name = os.getenv("mqtt_username")
pswd = os.getenv("mqtt_pwd")
robotID = os.getenv("robot_id")

#____setup
client = mqtt.Client(client_id="dana")
client.username_pw_set(name,pswd)
#callbacks
client.on_connect = util.on_connect
client.on_message = util.on_message
client.connect(broker)
#loop
client.loop_start()

while True:
    pass

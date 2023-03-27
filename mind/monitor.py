import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
import util

#enviroment variables
load_dotenv()
broker = os.getenv("mqtt_broker")
name = os.getenv("mqtt_username")
pswd = os.getenv("mqtt_pwd")

#mqtt setup
client = mqtt.Client()
client.username_pw_set(name,pswd)
#callbacks
client.on_message = util.msg
client.connect(broker)
client.subscribe("$SYS/broker/clients/connected")
client.subscribe("poop")

client.loop_forever()
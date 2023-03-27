import paho.mqtt.client as mqtt

def msg(client,userdata,message):
    print(message.payload.decode())

client = mqtt.Client()
client.username_pw_set("mqtt", "mqtt333")
client.connect("44.202.67.39")

client.on_message = msg

client.subscribe("button/clicked")
client.loop_forever()
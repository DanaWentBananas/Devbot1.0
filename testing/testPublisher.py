import paho.mqtt.client as mqtt

def on_publish(client,userdata,result):             #create function for callback
    print(result)

client = mqtt.Client()

client.username_pw_set("myadmin", "admin333")
client.connect("44.202.67.39")

client.on_publish = on_publish

client.publish("testTopic", "1")
import paho.mqtt.client as mqtt
import json

MQTT_ADDRESS = "soldier.cloudmqtt.com"
MQTT_PORT = 10514
MQTT_TIMEOUT = 10

TOPIC = "test"

client = mqtt.Client()

def on_message(client,userdata,msg):
    print (msg.payload)

client.username_pw_set("ctuqpqym","Xk5GNcWqcmZG")
client.connect(MQTT_ADDRESS,MQTT_PORT,MQTT_TIMEOUT)
client.subscribe(TOPIC)

client.on_message = on_message

client.loop_forever()

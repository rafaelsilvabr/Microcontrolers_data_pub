import paho.mqtt.client as mqtt
import json

MQTT_ADDRESS = "soldier.cloudmqtt.com"
MQTT_PORT = 10514
MQTT_TIMEOUT = 60

client = mqtt.Client()

client.username_pw_set("ctuqpqym","Xk5GNcWqcmZG")
client.connect(MQTT_ADDRESS,MQTT_PORT,MQTT_TIMEOUT)

'''
msg={'temp': 20,
    'humid': 50}
'''

msg = {'estado':False,
	'registred':False,
	'localId':'id1',
	'regInfos':{
	    "data": {
	      "description": "A simple sensor",
	      "capabilities": [
	        "n",
	        "temperature",
	        "humidity",
	        "pressure"
	      ],
	      "status": "active",
	      "lat":10,
	      "lon":12
	    }
	},
	'data':{
		"data": [{
	      "temperature": 30
	    }]
	}
}


#client.publish("test","helloworld",qos=1,retain=True)
client.publish("data",json.dumps(msg),qos=1,retain=True)

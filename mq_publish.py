import paho.mqtt.client as mqtt
from random import randrange, uniform
import time


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost",1883,60)

client.loop_forever()


client.publish("test/temp","23.4")
client.subscribe("test/temp")
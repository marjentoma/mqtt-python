import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect

client.connect("test.mosquitto.org", 1883, 60)

# time.sleep(1)
# message=input("Enter a message: ")
while True:
    message=input("Enter a message: ")
    client.loop()
    client.publish("eleasar/message", message)
    print(message)
    time.sleep(1)
   
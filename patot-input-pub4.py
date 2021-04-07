import paho.mqtt.client as mqtt
import time

topic =input("Enter the topic: ")
payload =input("Enter the payload: ")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    print(" ")
    print("This is a publisher client")
    print("Published topic: " + topic)
    print("Published payload: " + payload)
    print(" ")

client = mqtt.Client()
client.on_connect = on_connect

client.connect("test.mosquitto.org", 1883, 60)

time.sleep(1)
while True:
    client.loop()
    client.publish(topic, payload)
    time.sleep(1)

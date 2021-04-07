import paho.mqtt.client as mqtt

# topic = "junrey/pn/c1/comlab/temperature"
topic = input("Enter topic to subscribe: ")

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc)+"\n")
    print("This is a subscriber client")
    print("Subscribed topic: " + topic+"\n")

    client.subscribe(topic)
def on_message(client, userdata, msg):
    print(msg.topic + ": " + str(msg.payload.decode()))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
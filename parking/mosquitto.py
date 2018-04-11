import paho.mqtt.client as mqtt
from . import views

def on_connect(client, userdata, flags, rc):
    client.subscribe('/sensor/status')

def on_message(client, userdata, msg):
    views.status = msg.payload.decode()
    status = [int(stat) for stat in list(msg.payload.decode())]

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.2.180.134", 1883, 60)
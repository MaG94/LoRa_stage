#!/usr/bin/python

import paho.mqtt.client as mqtt
import time
import json
from configuration import username, password, ca_path

mqtt_params = {
    "broker_address":  "ptnetsuite.a2asmartcity.io",
    "broker_port": 8883,
    "keep_alive_interval": 60,
    "topic": "#",
    "ca_path": ca_path,
    "insecure_tls": True,
    "qos": 2,
    "username": username,
    "password": password
}

def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("connection OK")
    else:
        print("connection refused", rc)

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_message(client, userdata, message):
    print("message received " , str(message.payload.decode("utf-8")))
    json_obj = str(message.payload.decode("utf-8")
    parse_data(json_obj)
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


# Need to be written
def parse_data(json_obj):


topic = "/sub/v1/users/unimib/apps/#"
client = mqtt.Client("unimib::8000")
client.username_pw_set(mqtt_params["username"],mqtt_params["password"])
client.tls_set(ca_certs=mqtt_params["ca_path"])
client.tls_insecure_set(mqtt_params["insecure_tls"])

client.on_connect = on_connect
client.on_log = on_log
client.on_message = on_message


print("Connecting to broker ", mqtt_params["broker_address"])
client.connect(mqtt_params["broker_address"], mqtt_params["broker_port"], mqtt_params["keep_alive_interval"])
client.loop_start()
print("Subscribing to topic ", "/sub/v1/users/unimib/apps/#")
r = client.subscribe("/sub/v1/users/unimib/apps/#")
if r[0]==0:
    print("everything fine")
else:
    print("bad subscription")

time.sleep(10000)
client.loop_stop()
client.disconnect()

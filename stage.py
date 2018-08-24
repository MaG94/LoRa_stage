#!/usr/bin/python

import paho.mqtt.client as mqtt
import time
import json
import sqlite3
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

def restore_database():
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('DROP TABLE IF EXISTS datas')
    db.commit()
    cursor.execute('''
    CREATE TABLE datas(seqno int PRIMARY KEY, temperature int, umidity_percentage int,
                        rssi int, modBW int, snr float)
                       ''')
    db.commit()

def decode_unicode_values(values_array):
    decoded_value = ""
    for value in values_array:
        data = bytes(value, 'utf-8')
        numb = b'u00'
        final = b'\\' + numb + data
        result = final.decode('unicode-escape').encode('latin1').decode('utf8')
        decoded_value += result

    return decoded_value

def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("connection OK")
    else:
        print("connection refused", rc)

def on_log(client, userdata, level, buf):
    print("log: ", buf)

def on_message(client, userdata, message):
    print("message received " , str(message.payload.decode("utf-8")))
    msg = str(message.payload.decode("utf-8"))
    json_obj = json.loads(msg)
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
    if(message.topic == "/sub/v1/users/unimib/apps/1/devices/a8610a3037458f01/uplink/2"):
        parse_and_load_data(json_obj)

# Need to be written
def parse_and_load_data(json_obj):
    raw_payload = json_obj["payload"]
    payload = [raw_payload[i:i + 2] for i in range(0, len(raw_payload), 2)]
    temperature  = decode_unicode_values([payload[0], payload[1]])
    umidity_percentage = decode_unicode_values([payload[2], payload[3]])
    seqno = json_obj["seqno"]
    adr = json_obj["statistics"]["adr"]
    channel = json_obj["statistics"]["channel"]
    duplicate = json_obj["statistics"]["duplicate"]
    freq = json_obj["statistics"]["freq"]
    modBW = json_obj["statistics"]["modBW"]
    rssi = json_obj["statistics"]["rssi"]
    sf = json_obj["statistics"]["sf"]
    snr = json_obj["statistics"]["snr"]

    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO datas(seqno, temperature, umidity_percentage, rssi, modBW, snr)
                  VALUES(?,?,?,?,?,?)''', (seqno, temperature, umidity_percentage, rssi, modBW, snr))

    db.commit()

restore_database()
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
print("Subscribing to topic ", topic)
r = client.subscribe(topic)
if r[0]==0:
    print("everything fine")
else:
    print("bad subscription")

time.sleep(10000)
client.loop_stop()
client.disconnect()

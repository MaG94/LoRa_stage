# LoRa_stage
Simple python script, based on MQTT protocol, that perform a connection to a LoRa server using PAHO library. After the connection is established, data sent by a temperature sensor is retrieved, parsed and stored into a database.

# What are MQTT and PAHO?
The **MQTT protocol** is a machine-to-machine (M2M)/”Internet of Things” connectivity protocol. Designed as an extremely lightweight publish/subscribe messaging transport, it is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium. The **Eclipse Paho** project is the reference implementation for the MQTT protocol.

# Environment setup
### First step
First of all, to use this application you have to download python 
```
sudo apt-get install python3.6
```
### Second step
Then you have install **pip**
```
sudo apt-get install python-pip
```
### Third step
The following step is to install **paho**
```
sudo pip install paho-mqtt
```
### Fourth step 
In the end you have to create your own **configuration.py** file where you will put your own connection parameters like **username**, **password** and **certificate path**

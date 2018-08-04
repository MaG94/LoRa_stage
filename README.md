# LoRa_stage
Simple python script, based on MQTT protocol, that perform a connection to a LoRa server using PAHO library. After the connection is established, data sent by a temperature sensor is retrieved, parsed and stored into a database.

# What are MQTT and PAHO?
The **MQTT protocol** is a machine-to-machine (M2M)/”Internet of Things” connectivity protocol. Designed as an extremely lightweight _**publish/subscribe messaging transport**_, it is useful for connections with remote locations where a small code footprint is required and/or network bandwidth is at a premium. The **Eclipse Paho** project is the reference implementation for the MQTT protocol.

# Publish/subscribe pattern
The publish/subscribe pattern (also known as pub/sub) provides an alternative to traditional client-server architecture. In the client-sever model, a client communicates directly with an endpoint.The pub/sub model decouples the client that sends a message (the publisher) from the client or clients that receive the messages (the subscribers). The publishers and subscribers never contact each other directly. In fact, they are not even aware that the other exists. The connection between them is handled by a third component (the broker). The job of the broker is to filter all incoming messages and distribute them correctly to subscribers. So, let’s dive a little deeper into some of the general aspects of pub/sub (we’ll talk about MQTT specifics in a minute).
![](https://www.hivemq.com/wp-content/uploads/pub-sub-mqtt-1024x588.png =250x250)

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

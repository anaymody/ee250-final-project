import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    client.subscribe("jjzhu/savebutton")

def on_message(client, userdata, msg):
    print(str(msg.payload, "utf-8"))
    advicefile = open("advice.html", "a")
    advicefile.write("<li>" + str(msg.payload, "utf-8") + "</li><br>")

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)        
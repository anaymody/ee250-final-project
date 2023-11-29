"""EE 250L Lab 04 Starter Code

Run vm_subscriber.py in a separate terminal on your VM."""

# Team members; Jalan Zhu and Anay Mody
# Github: https://github.com/usc-ee250-fall2023/lab-04-web-services-lab04_janay/tree/lab05
# in branch lab05

import paho.mqtt.client as mqtt
import time

# def ultrasonic_callback(client, userdata, message):
#     # #the third argument is 'message' here unlike 'msg' in on_message 
#     # print("custom_callback: " + message.topic + " " + "\"" + 
#     #     str(message.payload, "utf-8") + "\"")
#     # print("custom_callback: message.payload is of type " + 
#     #       str(type(message.payload)))
#     print("VM: " + str(message.payload, "utf-8") + " cm")

# def button_callback(client, userdata, message):
#     # #the third argument is 'message' here unlike 'msg' in on_message 
#     # print("custom_callback: " + message.topic + " " + "\"" + 
#     #     str(message.payload, "utf-8") + "\"")
#     # print("custom_callback: message.payload is of type " + 
#     #       str(type(message.payload)))
#     if str(message.payload, "utf-8") == "1":
#             print("Button pressed!")

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("jjzhu/savebutton")
    # client.message_callback_add("jjzhu/ultrasonicRanger/customCallback", ultrasonic_callback)
    # client.subscribe("jjzhu/button/customCallback")
    # client.message_callback_add("jjzhu/button/customCallback", button_callback)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print(str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="test.mosquitto.org", port=1883, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)        
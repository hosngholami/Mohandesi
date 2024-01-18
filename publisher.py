import paho.mqtt.client as mqtt

client = mqtt.Client()


def on_connect(c, userdata, flags, rc):
    client.publish('test' , 10)


def on_message(client, userdata, msg):
    print(msg.payload.decode('utf-8'))





# client.connect('mqtt.eclipseprojects.io', 1883, 60)
client.connect('localhost', 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
import paho.mqtt.client as mqtt
class Sale:

    list_property_listener = ""
    

    @staticmethod
    def addPropertyListener(IPropertyListener):
        global list_property_listener
        list_property_listener = IPropertyListener
        
    @staticmethod
    def publish_property_event(name, value):
        global list_property_listener
        global client, mqtt
        client = mqtt.Client()
        def on_connect(c, userdata, flags, rc):
           name = str(type(list_property_listener).__name__)
           
           
           i = 0
           while True:
                print('if you want save,you should write 0')
                factor = int(input('select product: '))

                if factor == 0:
                    client.publish(name , 0)
                    break
                client.publish(name , factor)
        #    client.publish('test', 10)


        def on_message(client, userdata, msg):
           client.publish('test', 10)


        # client.connect('mqtt.eclipseprojects.io', 1883, 60)
        client.connect('localhost', 1883, 60)
        client.on_connect = on_connect
        client.on_message = on_message

        client.loop_forever()

    def set_total():
        pass
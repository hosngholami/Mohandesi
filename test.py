from sales.Abserver.interface import IPropertyListener
from sales.Sales import Sale
import paho.mqtt.client as mqtt
class PropertyListener(IPropertyListener):
    def on_proprety_listener(self, source, name, value):
        print('test')



    def subscribe(self):
        Sale.addPropertyListener(self)

    

def subscribe():
     global client, mqtt
     client = mqtt.Client()


     def on_connect(client, userdata, flags, rc):
        
        name  = str(PropertyListener.__name__)
        print(name)
        client.subscribe(name)
        print('connected ... ')


     def on_message(client, userdata, msg):
        print(msg.payload.decode('utf-8'))

     client.connect('localhost', 1883, 60)
     client.on_connect = on_connect
     client.on_message = on_message

     client.loop_forever()







     
def register():
    p = PropertyListener()
    p.subscribe()

if __name__ == '__main__':
    subscribe()

    

      
            
       

       
from sales.Abserver.interface import IPropertyListener
from sales.Sales import Sale
import paho.mqtt.client as mqtt
import json
import os

sum = 0
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
        global sum
        id = msg.payload.decode('utf-8')
        with open(os.getcwd() + '/sales/Abserver/database.json', 'r') as data:
            if int(id) == 0:
                print("sum:",sum)
            data = json.load(data)
            for i in range(len(data)):
                 if data[i][0]['id'] == id:
                     print(data[i])
                     sum += int(data[i][0]['price'])
            

     client.connect('localhost', 1883, 60)
     client.on_connect = on_connect
     client.on_message = on_message

     client.loop_forever()







     
def register():
    
    p = PropertyListener()
    p.subscribe()

if __name__ == '__main__':
    
    subscribe()

    

      
            
       

       
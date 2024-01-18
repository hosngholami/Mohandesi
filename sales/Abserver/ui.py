from sales.Abserver.interface import IPropertyListener
from sales.controller import Sale

class PropertyListener(IPropertyListener):
    def on_proprety_listener(self, source, name, value):
        print('test')



    def subscribe(self):
        Sale.addPropertyListener(self)
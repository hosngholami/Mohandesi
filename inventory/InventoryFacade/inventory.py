from .interface import *
import os
import json
class Product(IProduct):
    def is_available(self, product_id):
        is_found = False
        with open(os.getcwd() + '/sales/Abserver/database.json', 'r') as data:
            data = json.load(data)
            for i in range(len(data)):
                 if data[i][0]['id'] == product_id:
                     is_found = True
                 
        return is_found
    
    def warehouse_inventory(self):
        sum  = 0
        with open(os.getcwd() + '/sales/Abserver/database.json', 'r') as data:
            data = json.load(data)
            for i in range(len(data)):
                 sum +=  data[i][0]['count'] 
                 
        return sum
                    
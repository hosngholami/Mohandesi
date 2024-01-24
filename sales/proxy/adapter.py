from sales.proxy.interface import *
import time
import random

class TaxAdapter(IProductAdapter):
    def get_total(self, factors):
        count = 0
        rand = random.randrange(1,3)
        while True:
            
            try:
                count += 1
                if rand == 2:
                    print("you connected to Tax adapter") 
                if count == 5:
                    raise Exception("TimeOut")

            except:
                print('tax adapter is faild')
                return None
        return None
    
    


class GoldTaxProAdapter(IProductAdapter):
    def get_total(self, factors):
        count = 0
        rand = random.randrange(1,3)
        while True:
            
            try:
                count += 1
                if rand == 2:
                    print("you connected to Tax pro adapter ")
                    break
                if count == 5:
                    raise Exception("TimeOut")

            except:
                print('tax pro adapter is faild')
                return None
        return None





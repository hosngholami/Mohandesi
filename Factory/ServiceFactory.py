import importlib
import yaml
class Factory:
    
    instance = None
    accounting_adapter = ""
    inverntory_adapter = ""

    
    def __init__(self):
        pass



    @staticmethod
    def getInstance(factory):
        global instance
        if factory.instance is None:
            factory.instance = Factory()
        return factory.instance




    def getInventoryAdapter(self):
        with open('Factory/config/factory.yml', 'r') as file:
            data = yaml.safe_load(file)
            adpater_name =  data['inventory_adapter'] 
            module_name = data['inventory_module']

        instance = getattr(importlib.import_module(module_name), adpater_name)
        return instance()



    def getAccountingAdapter(self):

        with open('Factory/config/factory.yml', 'r') as file:
            data = yaml.safe_load(file)
            adpater_name =  data['accounting_adapter'] 
            module_name = data['accounting_module']
            

        instance = getattr(importlib.import_module(module_name), adpater_name)
        accounting_factory = instance()
        return accounting_factory
    





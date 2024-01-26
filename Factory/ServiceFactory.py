import importlib
import yaml
class Factory:
    
    instance = None
    accounting_adapter = ""
    inverntory_adapter = ""
    inventory = ""

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
        return instance()
    

    def getSalesPricingStrategy(self):
        with open('Factory/config/factory.yml', 'r') as file:
                data = yaml.safe_load(file)
                strategy_name =  data['strategy_name'] 
                strategy_module = data['strategy_module']
                

        instance = getattr(importlib.import_module(strategy_module), strategy_name)
        return instance()
    

    def get_proxy(self):
        with open('Factory/config/factory.yml', 'r') as file:
                data = yaml.safe_load(file)
                proxy_name =  data['proxy_name'] 
                proxy_adapter = data['proxy_moudle']

        instance = getattr(importlib.import_module(proxy_adapter), proxy_name)
        return instance()
    
    def get_tax_adapter(self):
        list_instance = []
        with open('Factory/config/factory.yml', 'r') as file:
            data = yaml.safe_load(file)
            source_name =  data['source_name'] 
            source_module = data['source_module']
            for i in range(len(source_name)) :
                instance = getattr(importlib.import_module(source_module), source_name[i])
                list_instance.append(instance())
        return list_instance
    
    
                
       
         
         
  






from accounting.externalsystem.adapter import *
import yaml
import sys
import types
import importlib


class AccouningtFactory():
    def getInventoryAdapter(self):
        with open('shop/config/factory.yml', 'r') as file:
            data = yaml.safe_load(file)
            adpater_name =  data['inventory_adapter'] 
            module_name = data['inventory_module']
        instance = getattr(importlib.import_module(module_name), adpater_name)
        inventory_factory = instance()
        return inventory_factory

    def getAccountingFactory(self):
        with open('shop/config/factory.yml', 'r') as file:
            data = yaml.safe_load(file)
            adpater_name =  data['accounting_adapter'] 
            module_name = data['accounting_module']
        instance = getattr(importlib.import_module(module_name), adpater_name)
        accounting_factory = instance()
        return accounting_factory
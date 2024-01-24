from sales.proxy.interface import IProductAdapter
from Factory.ServiceFactory import Factory
from Factory import ServiceFactory
import random
class Proxy(IProductAdapter):

    iProxySale = IProductAdapter

    def get_adapter(self):
        factory = Factory.getInstance(Factory)
        adapter = factory.get_tax_adapter()
        for i in range(len(adapter)):
            instance = adapter[i]
            instance.get_total(10)
            





    def get_total(self, factors):
        pass
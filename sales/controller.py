from Factory.ServiceFactory import Factory
from sales.Strategy.PercentDisCountPricingStrategy import SalesPricingStrategy
from sales.Strategy.interface import *
from sales.Abserver.interface import *
from sales.Sales import Sale
import paho.mqtt.client as mqtt

factors = [
    {'code':'100', 'count':10, 'total_price':150000},
    {'code':'101', 'count':5, 'total_price':250000},
    {'code':'102', 'count':8, 'total_price':60000},
    {'code':'103', 'count':6, 'total_price':7000},
    {'code':'104', 'count':1, 'total_price':20000},
    {'code':'105', 'count':2, 'total_price':110000},
]



product = [
    {'id':1,' title':'p1', 'price':150, 'code': 100},
    {'id':2,' title':'p2', 'price':100, 'code': 100},
    {'id':3,' title':'p3', 'price':250, 'code': 100},
    {'id':4,' title':'p4', 'price':600, 'code': 100},
    {'id':5,' title':'p5', 'price':700, 'code': 100},
    {'id':6,' title':'p6', 'price':800, 'code': 100},
    {'id':7,' title':'p7', 'price':100, 'code': 100},
    {'id':8,' title':'p8', 'price':250, 'code': 100},
    {'id':9,' title':'p9', 'price':110, 'code': 100},
    {'id':10,' title':'p10', 'price':120, 'code': 100},
]

factory = Factory.getInstance(Factory)


def get_adapter():
    
    accounting =  factory.getAccountingAdapter()
    print(accounting.sale(factors))


def get_strategy():
    strategy = factory.getSalesPricingStrategy()
    print(strategy.get_total(factors))



@staticmethod
def publisher():
    while True:
        
        Sale.publish_property_event('test', 10)
        



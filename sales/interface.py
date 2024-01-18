from abc import ABC, abstractclassmethod
import sys  


class IAccountingAdapter(object):
    @abstractclassmethod
    def factor(self, credit_payment, price):
        pass

    @abstractclassmethod
    def sale(self, factors):
        pass


class IInventoryAdapter(object):
    @abstractclassmethod
    def get_product(self, product_id):
        pass
    
    def add_product(self, product):
        pass

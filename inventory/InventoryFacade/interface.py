from abc import ABC, abstractclassmethod
import sys  


class IProduct(object):
    @abstractclassmethod
    def is_available(self, product_id):
        pass

    @abstractclassmethod
    def warehouse_inventory(self):
        pass

from abc import ABC, abstractclassmethod
import sys  


class IProductAdapter(object):
    @abstractclassmethod
    def get_total(self, factors):
        pass



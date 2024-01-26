from abc import ABC, abstractclassmethod
import sys  


class ISalesPricingStrategy(object):

    

    @abstractclassmethod
    def get_total(self, factors):
        pass
from .composit import *
import sys
class BestForCustomer(CompositPricingStrategy):
    def get_total(self, factors):
        maxsize = 0 
        for i in range(len(super().sale_princing_strategy)):
            instance = super().sale_princing_strategy[i]
            total = instance.get_total(factors)
            if maxsize < total:
                maxsize = total
        return maxsize
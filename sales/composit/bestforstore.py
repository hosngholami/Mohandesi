from .composit import *
import sys
class BestForStore(CompositPricingStrategy):
    def get_total(self, factors):
        min = sys.maxsize
        for i in range(len(super().sale_princing_strategy)):
            instance = super().sale_princing_strategy[i]
            total = instance.get_total(factors)
            if min > total:
                min = total
        return min
from sales.proxy.interface import *


class TaxAdapter(IProductAdapter):
    def get_total(self, factors):
        print('tax')
        return 'tax'
    


class GoldTaxProAdapter(IProductAdapter):
    def get_total(self, factors):
        print('tax pro')
        return 'tax pro'





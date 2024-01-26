from .interface import *
from .inventory import *
class InventoryFacade:
    instance = None
    product:IProduct = Product()

    @staticmethod
    def getInstance(facade):
        global instance
        if facade.instance is None:
            facade.instance = InventoryFacade()
        return facade.instance
    
    
    def is_available(self, product_id):
            status = self.product.is_available(product_id)

            if status == True:
                 print('product is found')
            else:
                 print('product not found')
    def get_total_product(self):
        print('total product: ', self.product.warehouse_inventory())
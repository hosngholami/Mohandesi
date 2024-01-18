from sales.interface import IInventoryAdapter



class InventoryAdapter(IInventoryAdapter):
    def get_product(self, product_id):
        return "phone"
    
    def add_product(self, product):
        return super().add_product(product)

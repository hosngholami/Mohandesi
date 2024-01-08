from shop.interface import IAccountingAdapter



class GrantNorthccountAdapter(IAccountingAdapter):
    def factor(self, credit_payment, price):
        return "you'r conntect to GrantNorthccount"
    
    def sale(self, price, delivery):
        if delivery == True:
            return price + 500000
        else:
            return price
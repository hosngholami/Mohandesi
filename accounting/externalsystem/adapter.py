from shop.interface import IAccountingAdapter



class SAPAccountAdapter(IAccountingAdapter):
    def factor(self, credit_payment, price):
        return "you'r conntected to SAPAccount"
    
    def sale(self, price, delivery):
        if delivery == True:
            return price + 10000
        else:
            return price



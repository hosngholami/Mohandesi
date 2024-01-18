from sales.interface import IAccountingAdapter



class SAPAccountAdapter(IAccountingAdapter):
    def factor(self, credit_payment, price):
        return "you'r conntected to SAPAccount"
    
    def sale(self, factors):
        print("you'r connected to system SAPAccounting Adapter")
        sum = 0
        for factor in factors:
            sum += int(factor['total_price']) + ((factor['total_price'] * 8)/ 100)
            
        return sum


from sales.interface import IAccountingAdapter



class GrantNorthccountAdapter(IAccountingAdapter):
    def factor(self, credit_payment, price):
        return "you'r conntect to GrantNorthccount"
    
    def sale(self,factors):
        print("you'r connected to system GrantNorthccountAdapter")
        sum = 0
        for factor in factors:
            sum += int(factor['total_price']) + ((factor['total_price'] * 5)/ 100)
            
        return sum
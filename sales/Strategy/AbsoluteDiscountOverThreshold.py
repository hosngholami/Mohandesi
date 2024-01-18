from sales.Strategy.interface import ISalesPricingStrategy

class SalesPricingStrategy(ISalesPricingStrategy):
    

    def get_total(self, factors):
        discount = 35 #percent
        count = 8
        sum = 0
        
        for factor in factors:
            sum += factor['total_price']

        if len(factors) > 5:
            sum = sum - ((sum * discount) / 100)
            
        return sum
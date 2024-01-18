from sales.Strategy.interface import ISalesPricingStrategy


class SalesPricingStrategy(ISalesPricingStrategy):
    

    def get_total(self, factors):
        percent = 10
        sum = 0
        for factor in factors:
            sum += factor['total_price']

        return (sum - ((sum * percent) / 100))
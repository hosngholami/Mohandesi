from sales.Strategy.interface import ISalesPricingStrategy


class CompositPricingStrategy(ISalesPricingStrategy):
    

    sale_princing_strategy = []

    def add(self, strategy):
        self.sale_princing_strategy.append(strategy)
        

    def get_total(self, factors):
        pass
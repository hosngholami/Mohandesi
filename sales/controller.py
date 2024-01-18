from Factory.ServiceFactory import Factory



factors = [
    {'code':'100', 'count':10, 'total_price':150000},
    {'code':'101', 'count':5, 'total_price':250000},
    {'code':'102', 'count':8, 'total_price':60000},
    {'code':'103', 'count':6, 'total_price':7000},
    {'code':'104', 'count':1, 'total_price':20000},
    {'code':'105', 'count':2, 'total_price':110000},
]






def get_adapter():
    factory = Factory.getInstance(Factory)
    accounting =  factory.getAccountingAdapter()
    print(accounting.sale(factors))
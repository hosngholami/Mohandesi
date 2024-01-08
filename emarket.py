
from sales.servicefactory import AccouningtFactory

if __name__ == '__main__':
    factory = AccouningtFactory()
    accounting = factory.getAccountingFactory()
    inventory = factory.getInventoryAdapter()
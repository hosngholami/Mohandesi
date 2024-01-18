import psycopg2
from Factory.ServiceFactory import Factory


class Shop:
    def __init__(self, id, name):
        self.id = id,
        self.name = name



def adapter():
    factory = Factory.getInstance(Factory)
    accounting =  factory.getAccountingAdapter()
    print(accounting.sale(10, 20))

state = {
    'exit': 0,
    'adapter': 1,
}


if __name__ == '__main__':
    while True:
        print('enter 0 for exit')
        key = input('plese select model: ')
        
        match state[key]:
            case 1:
                adapter()
            case 0:
                exit(1)



    # connection = psycopg2.connect(host="localhost", dbname="emarket", user="postgres", password="123", port=5432)
    

    # cursor = connection.cursor()


    # cursor.execute("""CREATE TABLE IF NOT EXISTS shop (
    #                     id INT PRIMARY KEY,
    #                     name VARCHAR(50)
    #                 )

    #                """)


    # connection.commit()
    # # cursor.close()
    # # connection.close()


    # cursor = connection.cursor()

    # cursor.execute("""
    #             select *  from shop
    #         """)
    
    # list_shop = []
    # for item in cursor.fetchall():
    #     list_shop.append(Shop(item[0], item[1]))


    # for item in list(list_shop):
    #     print(item.id)



    # factory = AccouningtFactory()
    # accounting = factory.getAccountingFactory()
    # inventory = factory.getInventoryAdapter()
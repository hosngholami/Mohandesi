from sales.controller import *
from test import register
state = {
    'exit': 0,
    'adapter': 1,
    'strategy': 2,
    'listener': 3,
    'proxy': 4
}


if __name__ == '__main__':
    while True:
        print('you can write exiit for exit')
        key = input('plese select model: ')
        
        match state[key]:
            case 1:
                get_adapter()
            case 2:
                get_strategy()
            case 3:
                register()
                publisher()
            case 4:
                proxy()
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
from sales.controller import *
from ui_form import register
import os
import json
state = {
    'exit': 0,
    'adapter': 1,
    'strategy': 2,
    'abserver': 3,
    'proxy': 4,
    'facade': 5,
    'composit': 6
}
def get_database_product():
      with open(os.getcwd() + '/sales/Abserver/database.json') as data:
        for item in data:
            print(item)

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
                get_database_product()
                register()
                publisher()
            case 4:
                proxy()
            case 5:
                print('enter 1 for get status product')
                print('enter 2 get wearhouse inventory')
                status  = int(input('please enter number : '))
                if status == 1:
                    product_id = input('enter product id')
                    is_available(product_id=product_id)
                if status == 2:
                    get_total_product()
            case 6:
                composit_strategy()
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
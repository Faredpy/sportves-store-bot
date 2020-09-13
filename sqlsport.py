import pymysql
from config import *

categoryList = []

class oc_product_to_category:
    def __init__(self, product_id, category_id):
        self.product_id = product_id
        self.category_id = category_id

def connect_db():
    try:
        connect = pymysql.connect(*DB_PARAMS)
    except pymysql.OperationalError:
        print('Подключиться не удалось')

    try:
        cursor = connect.cursor()
        cursor.execute(
            "SELECT * FROM oc_product_to_category WHERE category_id IN(59)"
        )
        rows = cursor.fetchall()
        for row in rows:
            categoryId = "{0}".format(row[0])
            categorycategory_id = "{0}".format(row[1])
            categoryList.append(oc_product_to_category(categoryId, categorycategory_id))
    except pymysql.OperationalError:
        print('Курсор залагал')

connect_db()

for stolbec in categoryList:
    print(stolbec.category_id)
    print(stolbec.product_id)
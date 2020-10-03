import pymysql
from config import *

categoryList = {}
idsProduct = []
products = []

def connect(func):
    def wrapper(*args, **kwargs):
        connection = pymysql.connect(**DB_PARAMS)  
        try:                         
            rv = func(connection, *args, **kwargs)
        finally:
            connection.close()
        return rv
    return wrapper

@connect
def getCategory(connection):
        try:
            categoryList.clear()
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM oc_category_description WHERE category_id IN(59, 70, 79)")
            rows = cursor.fetchall()
            for row in rows:
                categoryId = "{0}".format(row[0])
                categoryName = "{0}".format(row[2])
                categoryList[categoryName] = categoryId
            print(categoryList.keys())
            return categoryList
        except pymysql.OperationalError:
            print('Не удалось установить курсор!')
            return []

@connect
def getProductInCategory(connection, categoryId, count=5):
    idsProduct.clear()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM oc_product_to_category WHERE category_id =" + str(categoryId))
    rows = cursor.fetchall()
    i = 0
    for row in rows:
        if(i < count):
            idsProduct.append("{0}".format(row[0]))
        i += 1
    return idsProduct


@connect
def getProduct(connection, idsProduct):
    products.clear()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM oc_product WHERE product_id IN(" + str(','.join(idsProduct)) + ")")
    data = cursor.fetchall()
    len(data)
    for product in data:
        products.append({
            "model": "{0}".format(product[1]),
            "img": "{0}".format(product[11]),
            "price": "{0}".format(product[14]),
        })
    return products

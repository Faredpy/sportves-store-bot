import pymysql
from config import *


class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name


def connect_db(method):
    try:
        connect = pymysql.connect(*DB_PARAMS)
    except pymysql.OperationalError:
        print('Подключится неудалось!')

    if(method == 'getCategory'):
        categoryList = []

        def getCategory():
            try:
                cursor = connect.cursor()
                cursor.execute(
                    "SELECT * FROM oc_category_description WHERE category_id IN(59, 70, 79)")
                rows = cursor.fetchall()
                for row in rows:
                    categoryId = "{0}".format(row[0])
                    categoryName = "{0}".format(row[2])
                    categoryList.append(Category(categoryId, categoryName))
                return categoryList
            except pymysql.OperationalError:
                print('Не удалось установить курсор!')
        return getCategory()
    

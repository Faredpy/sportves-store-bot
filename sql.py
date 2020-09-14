import pymysql
#import mysql.connector
from config import *

#config = {
#  'user': 'root',
#  'password': 'root',
#  'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
#  'database': 'sportves',
#  'raise_on_warnings': True,
#}

#link = mysql.connector.connect(**config)


class Category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name


def connect_db(method):
    try:
        connection = pymysql.connect(user='root',
                                     password='root',
                                     unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
                                     db='sportves')
    except pymysql.OperationalError:
        print('Подключится неудалось!')

    if(method == 'getCategory'):
        categoryList = []

        def getCategory():
            try:
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT * FROM oc_category_description WHERE category_id IN(60, 70, 79)")
                rows = cursor.fetchall()
                for row in rows:
                    categoryId = "{0}".format(row[0])
                    categoryName = "{0}".format(row[2])
                    categoryList.append(Category(categoryId, categoryName))
                return categoryList
            except pymysql.OperationalError:
                print('Не удалось установить курсор!')
        return getCategory()
    

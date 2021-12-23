import pymysql
from pymysql import Error
from pymysql.cursors import Cursor

# Database Connection

connection = pymysql.connect(host='localhost', user='root', password='1234', db='world_x')
# Prepare the Cursor object
cursor = connection.cursor()

# Insert Query
query="""INSERT INTO EMPLOYEE (FIRST_NAME,LAST_NAME,AGE,SALARY)
        VALUES('Blessing','Adesiji',24,3000)
"""
#Execute Query
try:
    cursor.execute(query)
    connection.commit()
except Error as e:
    connection.rollback()
    print("Error:Inserting Row")
finally:
    connection.close()
    print("connection is closed")




import pymysql
from pymysql import Error
from pymysql.cursors import Cursor

# Database Connection

connection = pymysql.connect(host='localhost', user='root', password='1234', db='world_x')
# Cursor object
cursor = connection.cursor()

# Drop table if it already exist
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table

query = """CREATE TABLE EMPLOYEE(
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20),
    age INTEGER,
    Salary float
    )
    """
# Execute Query
cursor.execute(query)
# close Query
connection.close()

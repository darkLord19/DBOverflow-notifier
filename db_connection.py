import mysql.connector as conn
from secrets import Constants  

mydb = conn.connect(
    host=Constants.DB_HOST,
    user=Constants.DB_USER,
    passwd=Constants.DB_PWD
)
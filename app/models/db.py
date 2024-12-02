import mysql.connector

def get_connection():
    mydb = mysql.connector.connect(
        host='localhost',
        user='usuario',
        password='password',
        db='prestamos1_2'
    )
    return mydb  




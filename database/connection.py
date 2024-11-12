import mysql.connector
connection = mysql.connector.connect(
    host='192.168.1.12',
    user='myuser',
    password='123456',
    database='rick_and_morty'
)


cursor = connection.cursor(buffered=True)
cursor.execute("USE rick_and_morty") # select the database
import mysql.connector
# connection = mysql.connector.connect(
#     host='192.168.1.12',
#     user='myuser',
#     password='123456',
#     database='rick_and_morty'
# )

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='Yan',
    password='Gohanyan1',
    database='rick_and_morty',
    use_unicode=True
)

cursor = connection.cursor(buffered=True)
cursor.execute("USE rick_and_morty") # select the database
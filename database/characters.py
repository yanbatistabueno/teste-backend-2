from database.connection import connection, cursor


def get_characters():
    cursor.execute("SELECT * FROM characters")
    tables = cursor.fetchall()

    return tables

def get_current_character(name):
     cursor.execute(f"SELECT * FROM characters WHERE name = '{name}'")
     for row in cursor:
        return row

def insert_characters(name, status, image, url):
     cursor.execute(f"INSERT INTO characters(name, status, image, url) VALUES('{name}', '{status}', '{image}', '{url}')")
     connection.commit()
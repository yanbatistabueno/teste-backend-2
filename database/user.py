from database.connection import connection, cursor

def encrypt_password(string, key):
    resultado = ""
    await_string = str(string)
    for i in range(len(await_string)):
        xor_resultado = (ord(string[i]) ^ ord(key[i % len(key)])) % 95 + 32
        resultado += chr(xor_resultado)
    return resultado

def get_user_time(username):
    cursor.execute(f"SELECT created from user WHERE username = '{username}'")
    for row in cursor:
        return row[0]

def check_credencials(username, password):
    cursor.execute(f"SELECT password from user WHERE username = '{username}'")
    for row in cursor:
        if encrypt_password(password, str(get_user_time(username=username))) == row[0]: 
            return encrypt_password(password, str(get_user_time(username=username)))

def get_user(username, password):
    if(check_credencials(username=username, password=password) != None):
        new_password = check_credencials(username=username, password=password)
        cursor.execute(f"SELECT * FROM user WHERE username = '{username}' AND password = '{new_password}'")
        for row in cursor:
            return row
    

def get_current_date():
    cursor.execute("SELECT CURRENT_DATE()")
    table = cursor.fetchone()
    return table[0]


def create_user(username, email, password, role):
    cursor.execute(f"INSERT INTO user(username, password, email, role, created) VALUES('{username}', '{password}', '{email}', '{role}', CURRENT_DATE())")
    connection.commit()






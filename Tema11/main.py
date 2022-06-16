import getpass
import sqlite3

def main():
    username = input('Nombre de usuario: ')
    password = getpass.getpass('Contraseña: ')

    if verifica_credenciales(username, password):
        print('Login correcto')
    else:
        print('Login incorrecto')
    
    crear_usuario(3, 'Amed', 'maja')


def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"

    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    conn.close()

    if data == None:
        return False
    else:
        return True


def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = """INSERT INTO users(id, username, password) VALUES(?, ?, ?)"""

    rows = cursor.execute(query, (identificador, usuario,clave))
    
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()

#conn = sqlite3.connect('miaplicacion.db')

#cursor = conn.cursor()

#rows = cursor.execute('SELECT * FROM users')
#for row in rows:
 #   print(row)


#cursor.close()
#conn.close()
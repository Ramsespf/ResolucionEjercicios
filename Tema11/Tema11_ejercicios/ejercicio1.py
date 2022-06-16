import sqlite3

def main():
        
    contador = 1
    while contador <= 8:
        id = contador
        nombre = input('Introduzca el nombre del alumno: ')
        apellido = input('Introduzca el apellido del alumno: ')
        insert_alumnos(id, nombre, apellido)
        contador += 1

    busqueda = input('Ingresa el Nombre del estudiante para ver sus datos: ')
    find_alumnos(busqueda)

def insert_alumnos(id, nombre, apellido):
    """Funcion encargada de insertar los datos en la BD

    Args:
        id (int)
        nombre (str)
        apellido (str)
    """    
    conn = sqlite3.connect('escuela.db')
    cursor = conn.cursor()

    query = """INSERT INTO Alumnos(id, nombre, apellido) VALUES(?, ?, ?)"""
    cursor.execute(query, (id, nombre, apellido))

    cursor.close()
    conn.commit()
    conn.close()

def find_alumnos(nombre):
    """Funcion encargada de buscar los datos del alumno en la BD por su Nombre

    Args:
        nombre (str)
    """    
    conn = sqlite3.connect('escuela.db')
    cursor = conn.cursor()

    query = f'SELECT * FROM Alumnos WHERE nombre="{nombre}"'
    rows = cursor.execute(query)
    for row in rows:
        print(row)

    

    cursor.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
"""
Script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista.
No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y 
separados por comas.
"""
paises = []

lista_paises = input('Escriba una lista de paises separadas por ,\n')
lista_paises = lista_paises.split(',')
# Eliminar posbiles caso que el usuario introduzca " ," o "," en la separacion de los paises
for pais in lista_paises:
    paises.append(pais.strip())

lista_paises = set(paises)
lista_paises = sorted(lista_paises)
print(lista_paises)




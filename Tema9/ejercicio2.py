"""
Crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos 
elementos obtenidos mediante reduce.
"""
from functools import reduce


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

resultado = filter(lambda x : x % 2 != 0, numeros)
resultado = list(resultado)

resultado = reduce(lambda x, y : x + y, resultado)
print(resultado)
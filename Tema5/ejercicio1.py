import math

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi * radio**2

print("Para calcular el Area del Triangulo:")
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

print(f"El Area del triangulo es {area_triangulo(base, altura)}\n")

print("Para calcular el Area del Circulo:")
radio = int(input("Ingrese el radio: "))
print(f"El Area del Circulo es {area_circulo(radio)}")

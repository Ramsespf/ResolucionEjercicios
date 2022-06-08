"""
Implementar la Vinculacion has-a
"""
class Vehiculo:
    color = 'Azul'
    ruedas = 4
    puertas = 4

class Coche:
    vehiculo =Vehiculo()
    velocidad = '100 Km'
    cilindrada = '1600 cc'

c = Coche()

print('Cilindrada: ', c.cilindrada)
print('Velocidad: ', c.velocidad)
print('Puertas: ', c.vehiculo.puertas)
print('Ruedas: ', c.vehiculo.ruedas)
print('Color: ', c.vehiculo.color)
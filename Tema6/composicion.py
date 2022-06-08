class Motor:
    tipo = "Diesel"

class Ventana:
    cantidad = 5

    def cambiar_cantidad(self, cantidad):
        self.cantidad = cantidad

class Rueda:
    ruedas = 4

class Carroceria:
    rueda = Rueda() # De esta forma se crea una composicion se crea una variable con el nombre de la clase
    ventana = Ventana()

class Coche:
    motor = Motor()
    carroceria = Carroceria()

c = Coche()
print('Motor es tipo: ', c.motor.tipo)
print('Ventanas: ', c.carroceria.ventana.cantidad)  # De esta forma se llama a un metodo de una clase mediante la composicion

c.carroceria.ventana.cambiar_cantidad(2)
print('Ventanas: ', c.carroceria.ventana.cantidad)
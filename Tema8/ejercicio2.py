import pickle

class Vehiculo:

    def __init__(self, color, modelo, year):
        self.color = color
        self.modelo = modelo
        self.year = year
    
    def getColor(self):
        return self.color
    
    def getModelo(self):
        return self.modelo

    def getYear(self):
        return self.year

carro = Vehiculo('rojo', 'toyota', 1990)

f = open('archivo.txt', 'wb')
pickle.dump(carro, f)
f.close()

f = open('archivo.txt', 'rb')
carro_load = pickle.load(f)
f.close()

print(carro_load.getColor())


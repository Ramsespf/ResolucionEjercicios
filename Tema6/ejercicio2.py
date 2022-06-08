
class Alumno:

    nombre = ''
    nota = None

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        if self.nota >= 7:
            print(f'{self.nombre} usted a aprobado la materia con {self.nota} ptos')
        else:
            print(f'{self.nombre} usted a suspendido la materia con {self.nota} ptos')

alumno1 = Alumno('Ramon', 8)
alumno2 = Alumno('Fernando', 5)

print(alumno1.nombre)
print(alumno1.nota)

alumno1.aprobado()
alumno2.aprobado()

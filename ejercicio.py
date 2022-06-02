peso = input("Ingrese su peso en Kg: ")
estatura = input ("Ingrese su estatura en metros: ")
imc = float(peso) / (float(estatura) ** 2)
print(f"Tu índice de masa corporal es {round(imc,2)} ")
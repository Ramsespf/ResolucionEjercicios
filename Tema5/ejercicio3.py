def bisiesto(year):
    """
    Para determinar si un año es bisiesto, siga estos pasos:

    1.- Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
    2.- Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
    3.- Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
    4.- El año es un año bisiesto (tiene 366 días).
    5.- El año no es un año bisiesto (tiene 365 días).
    """
    #Determino que sea divisible por 100 y 400
    if year % 100 == 0 and year % 400 == 0:
        print(f'El año {year} es bisiesto')
    else:
        # Determino si el año es divisible por 4 pero que no sea deivisible por 100
        if year % 4 == 0 and year % 100 != 0:
            print(f'El año {year} es bisiesto')
        else:
            print(f'El año {year} no es bisiesto')
        

bisiesto(1988)
import math

def primo(numero):
    multiplo = math.factorial(numero - 1) + 1
    if multiplo % numero == 0:
        print(f'{numero} es un numero primo')
    else:
        print(f'{numero} no es un numero primo')

primo(114)
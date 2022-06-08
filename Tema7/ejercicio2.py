from time import localtime
"""
Indice      Atributo        Valores
0           tm_year         (por ejemplo, 1993)
1           tm_mon          rango [1, 12]
2           tm_mday         rango [1, 31]
3           tm_hour         rango [0, 23]
4           tm_min          rango [0, 59]
5           tm_sec          rango [0, 59]
.....
"""

hora = localtime()

hora_restante = 19 - hora[3]
min_restante = 60 - hora[4]
    

if hora[3] > 17:
    print('Es hora de ir a la casa')
else:
    print(f'Te faltan {hora_restante}hrs y {min_restante}min para salir del Trabajo')



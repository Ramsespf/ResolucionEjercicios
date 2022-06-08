def escribir(texto):
    f = open('archivo.txt', 'a')
    f.write(texto)
    f.close

escribir('1ra linea\n')
escribir('2da linea\n')
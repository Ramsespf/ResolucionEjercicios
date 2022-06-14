import tkinter

from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccion = tkinter.StringVar()

# Funcion que imprime el valor del RadioButton
def imprimir():
    print(seleccion.get())     

# Funcion que se encarga de deseleccionar todos los RadioButton
def reiniciar(event):
    seleccion.set(None)

r1 = ttk.Radiobutton(window, text='Radio 1',value='Usted a seleccinado la opcion 1', variable=seleccion, command=imprimir)
r1.grid(column=0, row=0)

r2 = ttk.Radiobutton(window, text='Radio 2',value='Usted a seleccinado la opcion 2', variable=seleccion, command=imprimir)
r2.grid(column=0, row=1)

r3 = ttk.Radiobutton(window, text='Radio 3',value='Usted a seleccinado la opcion 3', variable=seleccion, command=imprimir)
r3.grid(column=0, row=2)

r4 = ttk.Radiobutton(window, text='Radio 4',value='Usted a seleccinado la opcion 4', variable=seleccion, command=imprimir)
r4.grid(column=0, row=3)




boton_salir = tkinter.Button(window, text='Reiniciar')
#boton_salir.pack()
boton_salir.bind('<Button-1>', reiniciar)
boton_salir.grid(column=0, row=4)


window.mainloop()

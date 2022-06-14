import tkinter

from tkinter import ttk
from tkinter import filedialog

window = tkinter.Tk()

def salir(event):
    print('Salir')
    window.quit()

def saludar(event):
    print('Haz dado Click')

def doble_click(event):
    print('Haz dado Doble Click')

boton = tkinter.Button(window, text='Haz Click')
boton.pack()
boton.bind('<Button-1>', saludar)
boton.bind('<Double-1>', doble_click)

boton_salir = tkinter.Button(window, text='Salir')
boton_salir.pack()
boton_salir.bind('<Button-1>', salir)

filename = filedialog.askopenfilename()     # Te abre el buscador de archovos de window

window.mainloop()


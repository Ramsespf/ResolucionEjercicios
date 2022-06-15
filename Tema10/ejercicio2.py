import tkinter

from tkinter import E, ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

frame = ttk.Frame(window)



lista = ['Naranja', 'Banana', 'Guayaba', 'Limon', 'Toronja', 'Piña', 'Melon']
lista_items = tkinter.StringVar(value=lista)
listbox = tkinter.Listbox(window, height=20, listvariable=lista_items)
listbox.grid(column=0, row=0, sticky=tkinter.W)

mercado_label = ttk.Label(window, text='Super Mercado')
mercado_label.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

window.mainloop()
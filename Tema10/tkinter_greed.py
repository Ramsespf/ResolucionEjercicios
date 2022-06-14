import tkinter

from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

frame = ttk.Frame(window)


#listas
#lista = ['Windows', 'macOS', 'Linux', 'MS DOS', 'AmigaOS', 'BeOS', 'OS/2']
#lista_items = tkinter.StringVar(value=lista)
#listbox = tkinter.Listbox(window, height=100, listvariable=lista_items)
#listbox.grid(column=0, row=0, sticky=tkinter.W)

# Radio Buttom
seleccionado = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text='Si', value='1', variable=seleccionado)
r1.grid(column=0, row=1, padx=5, pady=5)


# Checkbox
seleccionado_checkbox = tkinter.StringVar()
checkbox = ttk.Checkbutton(window, text='acepto las condiciones', variable=seleccionado_checkbox)
checkbox.grid(row=2, column=0)

## Username
username_label = ttk.Label(window, text='Username:')
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

username_entry = ttk.Entry(window)
username_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

## Password
password_label = ttk.Label(window, text='Password:')
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

password_entry = ttk.Entry(window, show='*')
password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

## Boton
login_button = ttk.Button(window, text='Login')
login_button.grid(column=1, row=2, sticky=tkinter.E, padx=5, pady=5)



window.mainloop()
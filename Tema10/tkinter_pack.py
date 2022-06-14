import tkinter

window = tkinter.Tk()


label1 = tkinter.Label(window, text='Label1', bg='yellow', fg='blue')
label1.pack(ipadx=45, ipady=15, fill='x')

label2 = tkinter.Label(window, text='Label2', bg='red', fg='white')
label2.pack(ipadx=45, ipady=15, fill='x')

label3 = tkinter.Label(window, text='Label3', bg='green', fg='blue')
label3.pack(ipadx=45, ipady=15, fill='x')

label4 = tkinter.Label(window, text='Label4', bg='blue', fg='white')
label4.pack(ipadx=15, ipady=15, side='left')

label5 = tkinter.Label(window, text='Label5', bg='black', fg='blue')
label5.pack(ipadx=15, ipady=15, side='left')

label6 = tkinter.Label(window, text='Label6', bg='pink', fg='white')
label6.pack(ipadx=15, ipady=15, side='right')


window.mainloop()
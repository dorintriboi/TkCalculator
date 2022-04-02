from tkinter import *
import tkinter

pagina_calculator = Tk()
panza = Canvas(pagina_calculator,bg = "black")
panza.pack()
scris = Entry(panza, width = 45 , borderwidth = 5, bg = "black", fg = "red")
scris.grid(row = 0, column = 0, columnspan = 3,padx = 10, pady = 10)

def apasat(x):
    curent = scris.get()
    scris.delete(0,END)
    scris.insert(0,str(curent) + str(x))

def clear():
    scris.delete(0,END)

def adaugare():
    global nr_1
    nr_1 = int (scris.get())
    scris.delete(0,END)

def egalul():
    nr_2 = int (scris.get())
    scris.delete(0,END)
    scris.insert(0,nr_1 + nr_2)


buton_1 = Button(panza, text = "1", bg = 'black', fg = 'green', padx = 45,pady = 20, activebackground="black", activeforeground="red", command = lambda : apasat("1"))
buton_2 = Button(panza, text = "2", bg = 'black', fg = 'green', command = lambda : apasat("2"), padx = 45,pady = 20, activebackground="black", activeforeground="red")
buton_3 = Button(panza, text = "3", bg = 'black', fg = 'green', command = lambda : apasat("3"), padx = 45,pady = 20, activebackground="black", activeforeground="red")
buton_4 = Button(panza, text = "4", bg = 'black', fg = 'green', command = lambda : apasat("4"), padx = 45,pady = 20, activebackground="black", activeforeground="red")
buton_5 = Button(panza, text = "5", bg = 'black', fg = 'green', command = lambda : apasat("5"), padx = 45,pady = 20, activebackground="black", activeforeground="red")
buton_6 = Button(panza, text = "6", bg = 'black', fg = 'green', command = lambda : apasat("6"), padx = 45,pady = 20, activebackground="black", activeforeground="red")
buton_7 = Button(panza, text = "7", bg = 'black', fg = 'green', command = lambda : apasat("7"), padx = 45,pady = 20, activebackground="black", activeforeground="red")
buton_8 = Button(panza, text = "8", bg = 'black', fg = 'green', command = lambda : apasat("8"), padx = 45,pady = 20, activebackground="black", activeforeground="red")
buton_9 = Button(panza, text = "9", bg = 'black', fg = 'green', command = lambda : apasat("9"), padx = 45,pady = 20, activebackground="black", activeforeground="red")
buton_0 = Button(panza, text = "0", bg = 'black', fg = 'green', command = lambda : apasat("0"), padx = 45,pady = 20, activebackground="black", activeforeground="red")

buton_1.grid(row = 1, column = 0)
buton_2.grid(row = 1, column = 1)
buton_3.grid(row = 1, column = 2)

buton_4.grid(row = 2, column = 0)
buton_5.grid(row = 2, column = 1)
buton_6.grid(row = 2, column = 2)

buton_7.grid(row = 3, column = 0)
buton_8.grid(row = 3, column = 1)
buton_9.grid(row = 3, column = 2)

buton_0.grid(row = 4, column = 0)

buton_plus = Button(panza, text = "+", bg = 'black', fg = 'green', command = adaugare, padx = 45,pady = 20, activebackground="black", activeforeground="red")
buton_plus.grid(row = 4, column = 1)
buton_clear = Button(panza, text = "Clear", bg = 'black', fg = 'green', command = clear, padx =34,pady = 20, activebackground="black", activeforeground="red")
buton_clear.grid(row= 4, column = 2)

buton_egal = Button(panza, text = "=", bg = "black",fg = "green", command = egalul, padx = 150, pady = 20, activeforeground= "red", activebackground="black")
buton_egal.grid(row = 5,column = 0, columnspan = 3)

pagina_calculator.mainloop()
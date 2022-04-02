from tkinter import *
from tkinter import ttk
pagina = Tk()
panza = Canvas(pagina, width = "400", height = "300")
panza.pack()
butoane = [
    '(',')','n!','<-',
    '7','8','9','*',
    '4','5','6','/',
    '1','2','3','+',
    ',','0','-','='
]
def adauga(x):
    semne = ['1','2','3','4','5','6','7','8','9','0','+','-','*','/',')','(',',']
    for i in semne:
        if (i == x):
            print("da")

ttk.Style().configure("TButton", padding = 10, relief = "flat", background = "black" )
c = 1
cc = 0
for i in butoane:
    cc += 1
    ttk.Button(panza, text = i , command = lambda:adauga(i)).grid(row = c, column = cc)
    if (cc == 4):
        cc = 0
        c += 1
scris = Entry(panza,selectbackground="black",selectforeground="red", selectborderwidth=5,   width = 62 )
scris.grid(row = 0,column = 1, columnspan = 4)


pagina.mainloop()
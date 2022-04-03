from tkinter import *
from tkinter import ttk
from tkinter import messagebox
pagina = Tk()
pagina.resizable(width = False, height = False)
panza = Canvas(pagina, width = "400", height = "300")
panza.pack()
butoane = [
    '(',')','n!','<-',
    '7','8','9','*',
    '4','5','6','/',
    '1','2','3','+',
    '.','0','-','Clear'
]
scris = Entry(panza,selectbackground="black",selectforeground="red", selectborderwidth=5,   width = 62 )
scris.grid(row = 0,column = 1, columnspan = 4)
ttk.Style().configure("TButton", padding = 10, relief = "flat", background = "black" )
c = 3
cc = 0
deschis = 0
semne2 = 0
for i in butoane:
    cc += 1
    ttk.Button(panza, text = i , command = lambda x = i :adauga(x)).grid(row = c, column = cc)
    if (cc == 4):
        cc = 0
        c += 1
ttk.Button(panza, text = "=", width = 58, command = lambda x = '=':adauga(x)).grid(row = 8,column = 0, columnspan = 5)

def adauga(x):
    ok = False
    if (x == '('):
        global deschis
        deschis += 1
    semne1 = ['+','-','*','/']
    if (x in semne1):
        global semne2
        semne2 += 1
    semne = ['1','2','3','4','5','6','7','8','9','0','+','-','*','/','.','(']
    for i in semne:
        if (i == x):
            ok = True
    if (ok == True):
        y = scris.get()
        scris.insert(len(y),x)
    elif (x == "Clear"):
        semne2 = 0
        scris.delete(0,END)
    elif (x == ")" and deschis != 0):
        y = scris.get()
        scris.insert(len(y),x)
        deschis -= 1
    elif ( x == ")" and deschis == 0):
        messagebox.showerror('Eroare','Paranteza nu are pereche')
    elif (x == "<-"):

        y = scris.get()
        if (len(y) > 0):
            if (y[len(y)-1] in semne1 ):
                semne2 -= 1
        scris.delete(len(y)-1,len(y))
    elif (x == "n!" and semne2 != 0):
        messagebox.showerror("Eroare!","Trebuie sa ai doar un numar pentru a efectua factorialul")
    elif ((x == "n!") and semne2 == 0):
        y = int (scris.get())
        if (y > 100):
            messagebox.showwarning("Warning!","Numarul este prea mare,va supraincarca sistemyl!!")
        else:
            yy = 1
            for i in range(1,y+1):
                yy *= i
            scris.delete(0,END)
            scris.insert(0,yy)
    elif (x == '='):
        semne3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '+', '-', '*', '/', '.', '(',')']
        y = scris.get()
        okk = False
        oj = True
        for i  in y:
            for j in semne3:
                if (i == j): okk = True
            if (okk == False) : oj = False
        if (oj == True):
            try :
                yy = int (eval(scris.get()))
                scris.delete(0,END)
                scris.insert(0,yy)
                semne2 = 0
            except:
                messagebox.showerror("Eroare!","Matinca undeva imparte la zero sau ai pus egal aiurea sau ceva la paranteze")
        else:
            messagebox.showerror("Eroare!","Ceva nu ai facut bine!")

pagina.mainloop()




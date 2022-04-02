from tkinter import *
import math as m
x = pow(2,3)
print(x)
pagina = Tk()
pagina.title('Munca')
panza = Canvas(pagina,width = 800, height = 600, bg = "black")
panza.pack()
x = 400
y = 300
R = 120
r1 = int (R * m.sin(2 * m.pi / 5))
r2 = int (R * m.cos(2 * m.pi / 5))
r11 =int ( R * m.sin(2 * m.pi / 10))
r22 = int (R * m.cos(2 * m.pi / 10))
lista = [
    #punctul A
    x - r1 ,
    y - r2,
    #punctul C
    x + r1 ,
    y - r2 ,
    #punctul E
    x - r11 ,
    y + r22 ,
    #punctul B
    x,
    y - R ,
    #include D
    x + r11 ,
    y + r22
]
stea = panza.create_polygon(lista,fill = 'green', width = 3, outline = 'black')

def up(event):
    x = 0
    y = -5

    panza.move(stea,x,y)
def down(event):
    x = 0
    y = +5
    panza.move(stea, x, y)
def left(event):
    x = -5
    y = 0
    panza.move(stea,x,y)
def right(event):
    x = +5
    y = 0
    panza.move(stea,x,y)

pagina.bind("<Left>",left)
pagina.bind("<Right>",right)
pagina.bind("<Up>",up)
pagina.bind("<Down>",down)
panza.winfo_rootx()



pagina.mainloop()
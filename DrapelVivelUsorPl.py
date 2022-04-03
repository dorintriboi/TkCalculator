from tkinter import *
pagina = Tk()
panza = Canvas(pagina,width = 800, height = 500)
panza.pack()
panza.create_rectangle(75,50, 375,250, fill = "dodgerblue", outline = "white")
panza.create_oval(135,90,255,210,fill = "yellow",outline = "yellow")
panza.create_rectangle(50,50,75,450,fill = "saddle brown", outline = "saddle brown")
pagina.mainloop()
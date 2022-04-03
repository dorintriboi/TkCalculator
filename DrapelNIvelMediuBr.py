from tkinter import *
pagina = Tk()
panza = Canvas(pagina,width = "800", height = "500")
panza.pack()
panza.create_rectangle(75,50, 380,250, fill = "SkyBlue3", outline = "Skyblue3")
panza.create_rectangle(75,50+70,380, 75+110,fill = "white", outline = "White")
panza.create_rectangle(75,50+80,380,75+100,fill = "black", outline = "SkyBlue3")

panza.create_rectangle(50,50,75,450,fill = "saddle brown", outline = "saddle brown")
pagina.mainloop()
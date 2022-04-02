from tkinter import *
pagina = Tk()
panza = Canvas(pagina, width = 800, height = 600)
panza.pack()

panza.create_rectangle(75,50,375,250, fill = "white", outline = "white")

rosu = panza.create_rectangle(75,130,375,170, fill = "brown3", outline = "brown3")
rosu1 =panza.create_rectangle(210,50,240,250, fill = "brown3", outline = "brown3")

triunghi1 = panza.create_polygon(75,110,142.5,110,75,65,fill = "dodgerblue4", outline = "white")
triunghi2 = panza.create_polygon(375,110,375,65,307.5,110, fill = "dodgerblue4", outline = "white")

triunghi1_copie = panza.create_polygon(75,190,142.5,190,75,190+35+10,fill = "dodgerblue4", outline = "white")
triunghi2_copie = panza.create_polygon(307.5,190,375,190,375,190+35+10,fill = "dodgerblue4", outline = "white")



polygon1 =panza.create_polygon(75,50,75,62,142.5+10-2,110,142.5+5+20-2,110,fill = "brown3", outline = "white")
polygon2 =panza.create_polygon(375,50,360,50,260+5,110,260+5+15,110,fill = "brown3", outline = "white")
polygon3 = panza.create_polygon(75,250,92,250,182,190,167,190, fill = "brown3", outline = 'white')
polygon3 = panza.create_polygon(375,250,375,240,307.5-5,190,307.5-5-15,190, fill = "brown3", outline = 'white')




triunghi3 = panza.create_polygon(190,50,100,50,190,110,fill = "dodgerblue4", outline = "white")
triunghi4= panza.create_polygon(260,50,260+95,50,260,110, fill = "dodgerblue4", outline = "white")

triunghi3_copie = panza.create_polygon(190,250,100,250,190,190,fill = "dodgerblue4", outline = "white")
triunghi4_copie = panza.create_polygon(260,190,260+90,250,260,250,fill = "dodgerblue4", outline = "white")














panza.create_rectangle(50,50,75,450,fill = "brown")

pagina.mainloop()

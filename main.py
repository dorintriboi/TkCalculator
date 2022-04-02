from tkinter import *
pagina = Tk()
panza = Canvas(pagina, width = 650, height = 450, bg = "black")
panza.pack()
#Cartea fata
cartea_fata = panza.create_rectangle(50,50,300,400, fill = "white")
cartea_spate = panza.create_rectangle(350,50,600,400, fill = "white")
linia1 = panza.create_line(60,60,60,100,fill = "black", width = 5)
linia2 = panza.create_line(290,350,290,390, width = 5)
cerc_10_unu = panza.create_oval(70,60,80,100,fill = "white",width = 5)
cerc_10_doi = panza.create_oval(270,350,280,390, fill = "white", width = 5)

forma1 = panza.create_oval(63,105,73,115, fill = "black")
forma1_2 = panza.create_oval(55,113,65,123, fill = "black")
forma1_3 = panza.create_oval(71,113,81,123, fill = "black")

lini1_1 = panza.create_line(68,113,68,130,fill = "black",width = 5)

linia_dr_sus = panza.create_line(270,60,270,100,fill = "black", width = 5)

cerc_10_dr_sus = panza.create_oval(280,60,290,100, width = 5)
cerc_10_st_jos = panza.create_oval(60,350,70,390,width = 5)
lini_st_jos = panza.create_line(80,350,80,390,width = 5)

forma2 = panza.create_oval(273,105,279,111,fill = "black", width = 5)
forma2_2 = panza.create_oval(265,113,271,119,fill = "black",width = 5)
forma2_3 = panza.create_oval(281,113,287,119, fill = "black", width = 5)
linia2_2 = panza.create_line(276,105,276,130,fill = "black", width = 5 )

pagina.mainloop()
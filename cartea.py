from tkinter import *
pagina = Tk()
panza = Canvas(pagina, width = 650, height = 450, bg = "black")
panza.pack()
#Cartea fat
cartea_fata = panza.create_rectangle(50,50,300,400, fill = "goldenrod", outline = "goldenrod", width = 4)
cartea_spate = panza.create_rectangle(350,50,600,400, outline = "navy", width = 4)
linia1 = panza.create_line(60,60,60,100,fill = "black", width = 5)
linia2 = panza.create_line(290,350,290,390, width = 5)
cerc_10_unu = panza.create_oval(70,60,80,100,fill = "goldenrod",width = 5)
cerc_10_doi = panza.create_oval(270,350,280,390, fill = "goldenrod", width = 5)

x = 350
while (x < 600):
    x += 1
    panza.create_line(x,50,600,400, fill = "gold",width = 2)
x = 350
while (x < 600):
    x += 1
    panza.create_line(350,50,x,400, fill = "navy", width = 2)


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
linia2_2 = panza.create_line(276,105,276,128,fill = "black", width = 5 )

forma3 = panza.create_oval(70,340,76,346, fill = "black",width = 5)
forma3_2 = panza.create_oval(62,332,68,338,fill = "black", width = 5)
forma3_3 = panza.create_oval(78,332,84,338, fill = "black", width = 5)
linia3_3 = panza.create_line(73,340,73,323, fill = "black",width = 5)

forma4 = panza.create_oval(280,340,286,346, fill = "black", width = 5)
forma4_2 = panza.create_oval(272,332,278,338, fill = "black", width = 5)
forma4_3 = panza.create_oval(288,332,294,338, fill = "black", width = 5)
linia4_4 = panza.create_line(283,340,283,322, fill = "black", width = 5)

cerc_forma1 = panza.create_oval(115,75,135,95, fill = "black", width = 5)
cerc_forma2 = panza.create_oval(95,95,115,115, fill = "black", width = 5)
cerc_forma3 = panza.create_oval(135,95,155,115, fill = "black", width = 5)
linia_forma1 = panza.create_line(125,75,125,130, fill = "black" , width = 15)

cerc_forma1 = panza.create_oval(215,75,235,95, fill = "black", width = 5)
cerc_forma2 = panza.create_oval(195,95,215,115, fill = "black", width = 5)
cerc_forma3 = panza.create_oval(235,95,255,115, fill = "black", width = 5)
linia_forma1 = panza.create_line(225,75,225,130, fill = "black" , width = 15)

cerc_forma1 = panza.create_oval(115,165,135,185, fill = "black", width = 5)
cerc_forma2 = panza.create_oval(95,185,115,205, fill = "black", width = 5)
cerc_forma3 = panza.create_oval(135,185,155,205, fill = "black", width = 5)
linia_forma1 = panza.create_line(125,165,125,220, fill = "black" , width = 15)

cerc_forma1 = panza.create_oval(215,165,235,185, fill = "black", width = 5)
cerc_forma2 = panza.create_oval(195,185,215,205, fill = "black", width = 5)
cerc_forma3 = panza.create_oval(235,185,255,205, fill = "black", width = 5)
linia_forma1 = panza.create_line(225,165,225,220, fill = "black" , width = 15)

cerc_forma1 = panza.create_oval(115,275,135,295, fill = "black", width = 5)
cerc_forma2 = panza.create_oval(95,255,115,275, fill = "black", width = 5)
cerc_forma3 = panza.create_oval(135,255,155,275, fill = "black", width = 5)
linia_forma1 = panza.create_line(125,295,125,245, fill = "black" , width = 15)

cerc_forma1 = panza.create_oval(215,275,235,295, fill = "black", width = 5)
cerc_forma2 = panza.create_oval(195,255,215,275, fill = "black", width = 5)
cerc_forma3 = panza.create_oval(235,255,255,275, fill = "black", width = 5)
linia_forma1 = panza.create_line(225,295,225,245, fill = "black" , width = 15)

cerc_forma1 = panza.create_oval(115,365,135,385, fill = "black", width = 5)
cerc_forma2 = panza.create_oval(95,345,115,365, fill = "black", width = 5)
cerc_forma3 = panza.create_oval(135,345,155,365, fill = "black", width = 5)
linia_forma1 = panza.create_line(125,385,125,335, fill = "black" , width = 15)

cerc_forma1 = panza.create_oval(215,365,235,385, fill = "black", width = 5)
cerc_forma2 = panza.create_oval(195,345,215,365, fill = "black", width = 5)
cerc_forma3 = panza.create_oval(235,345,255,365, fill = "black", width = 5)
linia_forma1 = panza.create_line(225,385,225,335, fill = "black" , width = 15)



pagina.mainloop()
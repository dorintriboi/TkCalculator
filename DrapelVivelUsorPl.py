from tkinter import *
pagina = Tk()
panza = Canvas(pagina,width = 600, height = 500)
panza.pack()
panza.create_rectangle(75,50, 375,250, fill = "dodgerblue", outline = "white")
panza.create_oval(135,90,255,210,fill = "yellow",outline = "yellow")
panza.create_rectangle(50,50,75,450,fill = "saddle brown", outline = "saddle brown")
panza.create_text(171,300,text="Drapel: Palau", fill = "dodgerblue", font = "Helvetica 15 bold")
panza.create_text(206,325,text="Student: Triboi Dorin", fill = "black", font = "Helvetica 15 bold")
panza.create_text(210,350,text="UTM, FCIM, Gr. FI-211", fill = "gold", font = "Helvetica 15 bold")
pagina.mainloop()
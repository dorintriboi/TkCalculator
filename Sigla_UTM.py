from tkinter import *
pagina = Tk()
panza = Canvas(pagina,width = 600, height = 500)
panza.pack()
cerc1 = panza.create_oval(50,50,350,400, fill = "blue", activeoutline="green",width = 1)
cerc2 = panza.create_oval(15,50,400,375, fill = "white", activeoutline="red", width = 1)
pagina.mainloop()
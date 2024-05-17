from tkinter import *

from src.Interfaces.AppInterface import Aplicacion


#Create interface aplication

screenMain = Tk()
app = Aplicacion(screenMain) 
screenMain.mainloop()


import datetime
import sys

from tkinter import *
from src.Interfaces.AppInterface import Aplicacion
from src.Interfaces.mainInterface import MainApplication


# Definir la fecha límite
fecha_limite = datetime.date(2024, 7, 25)  # Año, mes, día


# Obtener la fecha actual
fecha_actual = datetime.date.today()

# Verificar si la fecha actual es posterior a la fecha límite
if fecha_actual > fecha_limite:
    print("Este programa ya no está disponible. Por favor, contacta al soporte.")
    sys.exit()

#Create interface aplication
app = MainApplication()
app.mainloop()

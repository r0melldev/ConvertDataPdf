from tkinter import *
from src.TablePDF.__main__ import createDocuments
from src.HandleData.importExelData import getDataClasificated
from src.Interfaces.AppInterface import Aplicacion



# proyect = input("Ingresa proyecto: ")
# client = input("Ingresa cliente: ")
# dep = input("Ingresa departamento: ")
# orderProduction = input("Ingresa Orden de Produccion: ")
# dateSave = input("Ingresa fecha entrega: ")

# print('Proyecto' + proyect )
# print('Cliente' + client )
# print('Departamento' + dep )
# print('Orden de production' + orderProduction )
# tuplaInformationHead = [proyect, client , dep , orderProduction, dateSave]

#print(tuplaInformationHead)

routeFileExcel = "OrdenesTest.xlsx" 

screenMain = Tk()
app = Aplicacion(screenMain) 


testVariable =  app.getDataResponse
print('-------------')
print(testVariable)

screenMain.mainloop()




# tuplaInformationHead = getDataForm()


# print("--------------------")
# print(tuplaInformationHead)

# tuplaArrayCases = getDataClasificated(routeFileExcel)

# for segmentEnd in tuplaArrayCases:
#     createDocuments(segmentEnd, tuplaInformationHead )

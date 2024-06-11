import json
import os

def repotDataVerefication(tuplaInformation):
    
    reportData = {}    
    reportData['TotalPdf'] = len(tuplaInformation) 

    listElements  = []

    for  indice, sizeTablePdf in enumerate(tuplaInformation):
        claveName = 'Npdf' + str(indice + 1)  
        reportData[claveName] = len(sizeTablePdf) 
        listElements.append(len(sizeTablePdf))

    totalElements = sum(listElements)         
    reportData['ElementosProcesados'] = totalElements

    return reportData


def createReportFile(information):
   
    nombre_archivo = 'NOrden121.txt'

    currentRoute = os.getcwd()
    routeFather = os.path.dirname(currentRoute)

    routeFileDocuments = os.path.join(routeFather, 'Documents')
    routeFilereports = os.path.join(routeFather, 'Reports') 
    
    if not os.path.exists(routeFileDocuments):
        os.mkdir(routeFileDocuments)

    if not os.path.exists(routeFilereports):
        os.mkdir(routeFilereports)

    print(routeFather)

    ruta_completa = os.path.join(routeFilereports, nombre_archivo)

    # Guardar el diccionario en el archivo JSON en la ruta especificada
    with open(ruta_completa, 'w') as archivo:
            json.dump(information, archivo) 

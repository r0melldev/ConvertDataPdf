import json
import os
import re

def repotDataVerefication(tuplaInformation):
    
    reportData = {}    
    reportData['TotalPdf'] = len(tuplaInformation) 

    listElements  = []

    for  indice, sizeTablePdf in enumerate(tuplaInformation):

        codDoc = re.sub(r'\s+', '', sizeTablePdf[0][1])

        # codDoc = sizeTablePdf[0][1].replace(" ", "")
        nameFile = sizeTablePdf[0][11] + '-' + codDoc + '-' + str(indice + 1)
        # claveName = nameFile + str(indice + 1)  
        reportData[nameFile] = len(sizeTablePdf) 
        listElements.append(len(sizeTablePdf))

    totalElements = sum(listElements)         
    reportData['ElementosProcesados'] = totalElements

    return reportData


def createReportFile(information, option, nOrden):

    documentName = 'NOrden' + nOrden + '.txt'

    if option == 1:
        fileReportOrder = 'MUEBLES_' + nOrden
    else:
        fileReportOrder = 'COMPLEMENTOS_' + nOrden


    currentRoute = os.getcwd()
    routeFather = os.path.dirname(currentRoute)

    routeFileDocuments = os.path.join(routeFather, 'Documents')
    
    routeFilereports = os.path.join(routeFather, 'Reports')  
    routeFileReportsByOrder = os.path.join(routeFilereports, fileReportOrder) 
    
    if not os.path.exists(routeFileDocuments):
        os.mkdir(routeFileDocuments)

    if not os.path.exists(routeFilereports):
        os.mkdir(routeFilereports)

    if not os.path.exists(routeFileReportsByOrder):
        os.mkdir(routeFileReportsByOrder)

    ruta_completa = os.path.join(routeFileReportsByOrder, documentName)

    # Guardar el diccionario en el archivo JSON en la ruta especificada
    with open(ruta_completa, 'w') as archivo:
            json.dump(information, archivo) 

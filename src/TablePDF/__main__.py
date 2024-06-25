import os
import re

from .structurePdf import structurePdf
from .detailsOrder import *
from .styles import *

def createDocuments(tuplaArrayCases, tuplaInformationHead, optionType):

    #Order List by description 
    listOrderByDescription = sorted(tuplaArrayCases, key=lambda x: x[2])

    #Create a structure Pdf 
    pdf = structurePdf(orientation = 'L', unit = 'mm', format='A4') 
    pdf.alias_nb_pages()
    pdf.add_page()

    # Information Order
    bcol_set(pdf, 'white')
    tfont_size(pdf,9)
    tfont(pdf,'B')
    detailOrder(pdf, tuplaArrayCases[0], tuplaInformationHead, optionType)

    # Table Products  
    tfont_size(pdf,6.5)
    bcol_set(pdf, 'blue')

    pdf.cell(w = 80, h = 10, txt = 'DESCRIPCIÓN', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 7, h = 10, txt = 'CANT', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 13.5, h = 10, txt = 'ANCHO M1', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 13.5, h = 10, txt = 'ALTO M2', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 15.5, h = 10, txt = 'ESPESOR', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 50, h = 10, txt = 'CÓDIGO FILO', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 22.5, h = 10, txt = 'FILO SUP MEDIDA 1', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 22.5, h = 10, txt = 'FILO INF MEDIDA 1', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 22.5, h = 10, txt = 'FILO DER MEDIDA 2', border = 1, align = 'C', fill = 1)
    pdf.multi_cell(w = 0, h = 10, txt = 'FILO IZQ MEDIDA 2', border = 1, align = 'C',  fill = 1)




    #estilos del color de borde y de letra 
    tfont_size(pdf,7.5)
    dcol_set(pdf, 'blue')
    tcol_set(pdf, 'black')

    c = 0
    for datos in listOrderByDescription:
        c+=1
        if(c%2==0):bcol_set(pdf, 'gray2')
        else:bcol_set(pdf, 'white')

        pdf.cell(w = 80, h = 7, txt = str(datos[2]), border = 'TBL', align = 'L', fill = 1)
        pdf.cell(w = 7, h = 7, txt =  str(datos[12]), border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 13.5, h = 7, txt =  str(datos[3]), border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 13.5, h = 7, txt =  str(datos[4]), border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 15.5, h = 7, txt =  str(datos[5]), border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 50, h = 7, txt = str(datos[6]), border = 'TB', align = 'L', fill = 1)
        pdf.cell(w = 22.5, h = 7, txt = str(datos[7]), border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 22.5, h = 7, txt = str(datos[8]), border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 22.5, h = 7, txt = str(datos[9]), border = 'TB', align = 'C', fill = 1)
        pdf.multi_cell(w = 0, h = 7, txt = str(datos[10]), border = 'TBR', align = 'C', fill = 1)



    #Export Document PDF
    currentRoute = os.getcwd()
    routeFather = os.path.dirname(currentRoute)
    routeFileDocuments = os.path.join(routeFather, 'Documents')
    
    nameSubfileOrder = '' 
  
    if optionType == 1:
          nameSubfileOrder = 'MUEBLES_' + str(tuplaInformationHead[3])
    else: 
          nameSubfileOrder = 'COMPLEMENTOS_' + str(tuplaInformationHead[3])

    dinamicRoute = os.path.join(routeFileDocuments, nameSubfileOrder) 

    if not os.path.exists(dinamicRoute):
        os.mkdir(dinamicRoute)
    
    
    nameDocument = structureNamePDF(tuplaArrayCases[0], optionType )

    pdf.output(dinamicRoute + '/' + nameDocument + '.pdf')


def structureNamePDF(informationFirstTupla, optionType):

    codigoName = re.sub(r'/', '', informationFirstTupla[1])
       
    if optionType == 1: 
        return informationFirstTupla[11] + '-' + codigoName 
    else:    
        return informationFirstTupla[11] + '-' + informationFirstTupla[13] + '-' + codigoName 

def createFilesFistOption(tuplaInformationHead, numberOrder):
   nameDocument =  'documents/'+ 'NORDEN_' +     numberOrder + '/' + nameDocument + '.pdf'
   return nameDocument

    
def createFilesSecondOption():
    ...
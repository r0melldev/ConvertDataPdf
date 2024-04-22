from src.TablePDF.structurePdf import structurePdf
from src.TablePDF.__main__ import createDocuments
from src.HandleData.importExelData import getDataClasificated

ruta_archivo_excel = "OrdenesTest.xlsx" 

tuplaArrayCases = getDataClasificated(ruta_archivo_excel)
print(tuplaArrayCases)
print(len(tuplaArrayCases))
print('-----------------')

# TODO -- create a document py Cases 


for segmentEnd in tuplaArrayCases:
    createDocuments(segmentEnd)
    




 
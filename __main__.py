from src.TablePDF.__main__ import createDocuments
from src.HandleData.importExelData import getDataClasificated

routeFileExcel = "OrdenesTest.xlsx" 

tuplaArrayCases = getDataClasificated(routeFileExcel)

for segmentEnd in tuplaArrayCases:
    createDocuments(segmentEnd)
  
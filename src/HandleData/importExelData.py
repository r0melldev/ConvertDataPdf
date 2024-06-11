import pandas as pd

from .clasificationData import * 

def getDataClasificated(ruta_archivo, typeClasificated):

    print(typeClasificated)
    try:
        # Leer el archivo Excel
        datos_excel = pd.read_excel(ruta_archivo,
                                    sheet_name="Hoja1",
                                    header=0)
        
        #validate depend of menu options 
        if typeClasificated == 1 : 
            tuplaCasesBySegments = groupByData(datos_excel, 'AMBIENTE')
        else:
            tuplaCasesBySegments = groupByData2(datos_excel, 'AMBIENTE')


        return tuplaCasesBySegments
    except Exception as e:
        print("Error al leer el archivo Excel:", e)
        return None



 
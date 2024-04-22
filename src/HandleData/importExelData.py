import pandas as pd

from .clasificationData import * 

def getDataClasificated(ruta_archivo):
    # Leer el archivo Excel
    try:
        datos_excel = pd.read_excel(ruta_archivo,
                                    sheet_name="Hoja1",
                                    header=0)

        tuplaCasesBySegments = groupByData(datos_excel, 'AMBIENTE')
        # for segmeCasesBySegments:
        #     print(segmentEnd) 

        return tuplaCasesBySegments
    except Exception as e:
        print("Error al leer el archivo Excel:", e)
        return None



 
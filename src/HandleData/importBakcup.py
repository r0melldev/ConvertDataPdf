import pandas as pd

def leer_excel(ruta_archivo):
    # Leer el archivo Excel
    try:
        datos_excel = pd.read_excel(ruta_archivo,
                                    sheet_name="Hoja1",
                                    header=0)
        return datos_excel
    except Exception as e:
        print("Error al leer el archivo Excel:", e)
        return None

if __name__ == "__main__":
    # Ruta del archivo Excel
    ruta_archivo_excel = "OrdenesTest.xlsx"  
 
    # Llamar a la función para leer el archivo Excel
    datos = leer_excel(ruta_archivo_excel)
    
    # Verificar si se pudo leer el archivo
    if datos is not None:
        ...
        #print("Contenido del archivo Excel:")
        #print(datos)
        #print(type(datos) )
    
    #print(datos.columns)
    # print(datos.head(4))
    # print(datos.describe())

    #print(datos['CODIGO'].head(2))
    
    #visualiza los 5 primeros registro por cada columna 
    # cols = datos.columns
    
    # for col in cols:
    #     print(datos[col].head(50))

#print(datos.columns)
datos_agrupados = datos.groupby('AMBIENTE')

#Primera forma //{'BAÑO': [5, 8, 10, 22, 24, 26, 36, 38, 50,
#listaXAmbiente = list(datos_agrupados) 
# listaXAmbiente = datos_agrupados .groups
# print(listaXAmbiente)

#print(list(listaXAmbiente))
#print(datos_agrupados[0].head(5))
#print(listaXAmbiente[0])

#Segunda forma // 

# Iterar sobre el objeto DataFrameGroupBy para obtener los grupos
for nombre_grupo, grupo_df in datos_agrupados:
    #print("Grupo:", nombre_grupo)
    #print(grupo_df)
    #print(grupo_df.head(3))
    #print(type(grupo_df))

    grupo_codigo = grupo_df.groupby('CODIGO')

    #print(list(grupo_codigo))

    for nombre_grupo, grupo_df in grupo_codigo:
        #print(grupo_df.describe())
        tuplas_document = grupo_df.to_records(index=False)
        print(tuplas_document)
        #print(grupo_df.describe())

    print('--------')




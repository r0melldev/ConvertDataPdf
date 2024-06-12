import pandas as pd

def groupByData(dataGroup, category):
    # firstGroupBy = dataGroup.groupby(category)
    tuplasSegmentsResponse = []
    firstGroupBy = dataGroup.groupby('AMBIENTE')


    for categoryGroup, groupSegment in firstGroupBy:
        #print("Grupo:", nombre_grupo)
        #print(grupo_df)
        #print(grupo_df.head(3))
        #print(type(grupo_df))

        secondGroupBy = groupSegment.groupby('CODIGO')

        #print(list(grupo_codigo))

        for categoryGroup2, groupSegment2 in secondGroupBy:
            #print(grupo_df.describe())
            tuplasBySegments = groupSegment2.to_records(index=False)
            #print(tuplasBySegments)
            lista_de_tuplas = [tuple(row) for row in tuplasBySegments]
            tuplasSegmentsResponse.append(lista_de_tuplas)
            #print(grupo_df.describe())

    print('--------')
    #print(tuplasBySegments)
    return tuplasSegmentsResponse


def groupByData2(dataGroup, category):
    # firstGroupBy = dataGroup.groupby(category)
    tuplasSegmentsResponse = []
    firstGroupBy = dataGroup.groupby('AMBIENTE')


    for categoryGroup, groupSegment in firstGroupBy:
        #print("Grupo:", nombre_grupo)
        #print(grupo_df)
        #print(grupo_df.head(3))
        #print(type(grupo_df))

        secondGroupBy = groupSegment.groupby('CODIGO')

        #print(list(grupo_codigo))

        for categoryGroup2, groupSegment2 in secondGroupBy:
            #print(grupo_df.describe())
            
            threeGroupBy = groupSegment2.groupby('RESPONSABLE')

            for categoryGroup3, groupSegment3 in threeGroupBy:

                tuplasBySegments = groupSegment3.to_records(index=False)
                #print(tuplasBySegments)
                lista_de_tuplas = [tuple(row) for row in tuplasBySegments]
                tuplasSegmentsResponse.append(lista_de_tuplas)
                #print(grupo_df.describe())

    print('--------')   
    #print(tuplasBySegments)
    return tuplasSegmentsResponse







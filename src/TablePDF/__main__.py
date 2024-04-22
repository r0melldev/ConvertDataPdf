import random
from .structurePdf import structurePdf
from .detailsOrder import *
from .styles import *

def createDocuments(tuplaArrayCases):

    lista_datos = (
        ('BASES'                    ,1,	620,	500,   	15,	'BB 22X1	             '      , 'CD BB',  'XX',       '-',	    '-'),
        ('BASES'                    ,1,	720,	550,   	15,	'BB 22X1	             '      , 'CD BB',  'XX',       '-',	    '-'),
        ('BASES'                    ,1,	870,	550,   	15,	'BB 22X1	             '      , 'CD BB',  'XX',       '-',	    '-'),
        ('LATERALES'                ,2,	500,	710,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'PVC BB', 'PVC BB',	'CD BB',	'XX'),
        ('LATERALES'                ,4,	550,	710,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'PVC BB',	'PVC BB',	'CD BB',	'XX'),
        ('REFUERZO POSTERIOR'	    ,1,	620,	90,   	15,	'-	                 '          , 'XX',     ' XX',      '-',	    '-'),
        ('REFUERZO POSTERIOR'	    ,1,	720,	90,   	15,	'-	                 '          , 'XX',     ' XX',      '-',	    '-'),
        ('REFUERZO POSTERIOR'	    ,1,	870,	90,   	15,	'-	                 '          , 'XX',     ' XX',      '-',	    '-'),
        ('REPISAS'                  ,1,	619,	340,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'PVC BB',	'PVC BB'),
        ('REPISAS'                  ,1,	719,	340,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'PVC BB',	'PVC BB'),
        ('REPISAS'                  ,1,	869,	340,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'PVC BB',	'PVC BB'),
        ('TIRAS DE UNIÓN'           ,2,	620,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	720,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
        ('TIRAS DE UNIÓN'           ,2,	870,	90,   	15,	'BB 22X1 /  BB 22X0.45'       	, 'CD BB',  'PVC BB',	'-',	    '-'),
    )

    print(tuplaArrayCases)
    
    pdf = structurePdf(orientation = 'P', unit = 'mm', format='A4') 
    pdf.alias_nb_pages()

    pdf.add_page()

    # Information Order
    bcol_set(pdf, 'green')
    tfont_size(pdf,10)
    tfont(pdf,'B')
    detailOrder(pdf)

    # tabla ----

    # encabezado tabla
    bcol_set(pdf, 'green')
    tfont_size(pdf,15)
    tfont(pdf,'B')
    pdf.cell(w = 0, h = 15, txt = 'Orden de Producción', border = 0,ln = 2, align = 'C', fill = 1)
    tfont(pdf,'')

    # columna de infomacion 
    tfont_size(pdf,6)
    bcol_set(pdf, 'blue')


    pdf.cell(w = 27, h = 10, txt = 'DESCRIPCION', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 7, h = 10, txt = 'CANT', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 13, h = 10, txt = 'ANCHO M1', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 13, h = 10, txt = 'ALTO M2', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 15, h = 10, txt = 'ESPESOR', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 25, h = 10, txt = 'CÓDIGO FILO', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 22, h = 10, txt = 'FILO SUP MEDIDA 1', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 22, h = 10, txt = 'FILO INF MEDIDA 1', border = 1, align = 'C', fill = 1)
    pdf.cell(w = 22, h = 10, txt = 'FILO DER MEDIDA 2', border = 1, align = 'C', fill = 1)
    pdf.multi_cell(w = 0, h = 10, txt = 'FILO IZQ MEDIDA 2', border = 1, align = 'C',  fill = 1)

    #estilos del color de borde y de letra 

    tfont_size(pdf,6)
    dcol_set(pdf, 'blue')
    tcol_set(pdf, 'gray')
    pdf.rect(x= 10, y= 60, w= 190, h= 53)
    c = 0

    for datos in tuplaArrayCases:
        c+=1
        if(c%2==0):bcol_set(pdf, 'gray2')
        else:bcol_set(pdf, 'white')
        pdf.cell(w = 27, h = 7, txt = str(datos[1]), border = 'TBL', align = 'L', fill = 1)
        pdf.cell(w = 7, h = 7, txt =  str(datos[11]), border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 13, h = 7, txt =  str(datos[2]), border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 13, h = 7, txt =  str(datos[3]), border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 15, h = 7, txt =  str(datos[4]), border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 25, h = 7, txt = datos[5], border = 'TB', align = 'L', fill = 1)
        pdf.cell(w = 22, h = 7, txt = datos[6], border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 22, h = 7, txt = datos[7], border = 'TB', align = 'C', fill = 1)
        pdf.cell(w = 22, h = 7, txt = datos[8], border = 'TB', align = 'C', fill = 1)
        pdf.multi_cell(w = 0, h = 7, txt = datos[9], border = 'TBR', align = 'C', fill = 1)


    numero_aleatorio = random.randint(0, 100)
    nameDocument = tuplaArrayCases[0][0] + str(numero_aleatorio) 
    print(tuplaArrayCases[0][0])

    pdf.output('documents/' + nameDocument + '.pdf')

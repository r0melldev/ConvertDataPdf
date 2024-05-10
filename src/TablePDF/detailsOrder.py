def detailOrder(document, information, tuplaInformationHead):
 
     nameVestidor = information[11] + ' - ' + information[0] 

     proyectName = 'PROYECTO: ' + str(tuplaInformationHead[0]).upper()  
     clientName = 'CLIENTE: ' + str(tuplaInformationHead[1]).upper() 
     depName = 'DEPARTAMENTO: ' + str(tuplaInformationHead[2]).upper() 
     oPName = 'ORDEN DE PRODUCCIÓN: ' + str(tuplaInformationHead[3]).upper() 
     dateSaveName = 'FECHA DE ENTREGA: ' + str(tuplaInformationHead[4]).upper() 
  
     document.multi_cell(w = 0, h = 6, txt = 'CORTE DE TABLEROS', border = 0,
          align = 'L', fill = 6)

     document.cell(w = 100, h = 6, txt = clientName , border = 0,
          align = 'L', fill = 6)

     document.cell(w = 100, h = 6, txt = proyectName, border = 0,
          align = 'L', fill = 6)
     
     document.multi_cell(w = 0, h = 6, txt = depName, border = 0,
          align = 'L', fill = 6)  
     
     
     document.cell(w = 100, h = 6, txt = oPName, border = 0,
          align = 'L', fill = 6)

     document.multi_cell(w = 0, h = 6, txt = dateSaveName, border = 0,
          align = 'L', fill = 6)


     document.multi_cell(w = 0, h = 6, txt = nameVestidor, border = 0,
          align = 'L', fill = 6)
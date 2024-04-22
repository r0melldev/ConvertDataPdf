def detailOrder(document, information):
    nameVestidor = information[11] + ' - ' + information[0] 
  
    document.multi_cell(w = 0, h = 7, txt = 'CORTE DE TABLEROS', border = 0,
         align = 'L', fill = 7)
   
    document.cell(w = 80, h = 7, txt = 'CLIENTE: GRAND BAY MANTA', border = 0,
         align = 'L', fill = 7)
    document.multi_cell(w = 0, h = 7, txt = 'FECHA DE ENTREGA: 19 MAYO 2024', border = 0,
         align = 'L', fill = 7)
    
    document.cell(w = 80, h = 7, txt = 'DEPARTAMENTOS: DPTO MODELO 307', border = 0,
         align = 'L', fill = 7)  
    document.multi_cell(w = 0, h = 7, txt = 'PROYECTO: DPTO MODELO 307', border = 0,
         align = 'L', fill = 7)
      
    document.multi_cell(w = 0, h = 7, txt = 'ORDEN DE PRODUCCIÓN: 199', border = 0,
         align = 'L', fill = 7)
    
    document.multi_cell(w = 0, h = 7, txt = nameVestidor, border = 0,
         align = 'L', fill = 7)

from tkinter import *

class Aplicacion:

    responseService = ''

   


    def __init__(self, screenMain):
        # self.ventana = ventana
        # self.contador = IntVar()
        # self.contador.set(0)

        # self.boton = Button(ventana, text="Incrementar", command=self.incrementar_contador)
        # self.boton.pack()

        # self.etiqueta = Label(ventana, textvariable=self.contador)
        # self.etiqueta.pack()


    
        screenMain.title('Principal interface')
        screenMain.minsize(width=500, height=500)
        screenMain.config(padx=35, pady=35)




          #Proyect
        self.proyectLabelName = Label(text="Ingrese el proyecto:", font=("Arial", 10)) 
        self.proyectLabelName.grid(column=0, row=1)

        self.proyectInput = Entry(width=20, font=("Arial", 10))
        self.proyectInput.grid(column=1, row=1) 

        self.spaceLabelName = Label( text="", font=("Arial", 10)) 
        self.spaceLabelName.grid(column=0)

        # #Cliente
        # clientLabelName = Label(text="Ingrese el cliente:", font=("Arial", 10) ) 
        # clientLabelName.grid(column=0, row=3)

        # clientInput = Entry(width=20, font=("Arial", 10))
        # clientInput.grid(column=1, row=3) 

        # spaceLabelName = Label( text="", font=("Arial", 10)) 
        # spaceLabelName.grid(column=0)

        # #Dep
        # depLabelName = Label(text="Ingrese el departamento:", font=("Arial", 10) ) 
        # depLabelName.grid(column=0, row=5)

        # depInput = Entry(width=20, font=("Arial", 10))
        # depInput.grid(column=1, row=5)

        # spaceLabelName = Label( text="", font=("Arial", 10)) 
        # spaceLabelName.grid(column=0)
    
        # #orderProduction
        # orderProductionLabelName = Label(text="Ingrese N° Order:", font=("Arial", 10) ) 
        # orderProductionLabelName.grid(column=0, row=7)

        # orderProductionInput = Entry(width=20, font=("Arial", 10))
        # orderProductionInput.grid(column=1, row=7)

        # spaceLabelName = Label( text="", font=("Arial", 10)) 
        # spaceLabelName.grid(column=0)
    
        # #dateSave
        # dateSaveLabelName = Label(text="Ingrese el departamento:", font=("Arial", 10) ) 
        # dateSaveLabelName.grid(column=0, row=9)

        # dateSaveInput = Entry(width=20, font=("Arial", 10))
        # dateSaveInput.grid(column=1, row=9)

        # spaceLabelName = Label( text="", font=("Arial", 10)) 
        # spaceLabelName.grid(column=0)

        self.getDataButton = Button(text="Enviar", font=("Arial", 10), command=self.incrementar_contador)
        self.getDataButton.grid(column=0, row=11)


    def incrementar_contador(self):
            #self.proyectInput.set(self.proyectInput.get() + 1)
        
        testEntre = self.proyectInput.get() 
        # print(testEntre)

        self.responseService = testEntre
    
    def getDataResponse(self):
        return self.responseService


  
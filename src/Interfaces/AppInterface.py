
from tkinter import *
from tkinter import filedialog

from src.TablePDF.__main__ import createDocuments
from src.HandleData.importExelData import getDataClasificated

class Aplicacion:

    nameRouteFile = ''
    statusApp = NO


    def __init__(self, screenMain):
        # self.ventana = ventana
        # self.contador = IntVar()
        # self.contador.set(0)

        # self.boton = Button(ventana, text="Incrementar", command=self.incrementar_contador)
        # self.boton.pack()

        # self.etiqueta = Label(ventana, textvariable=self.contador)
        # self.etiqueta.pack()

        screenMain.title('Generate Files')
        screenMain.minsize(width=600 , height=200)
        screenMain.config(padx=35, pady=35)


        #Proyect
        self.proyectLabelName = Label(screenMain, text="Ingrese el proyecto:", font=("Arial", 12))       
        self.proyectLabelName.grid(column=0, row=1, padx=6, pady=6, sticky='w')

        self.proyectInput = Entry(screenMain, width=40, font=("Arial", 12))
        self.proyectInput.grid(column=1, row=1, padx=6, pady=6, sticky='w')

        # #Cliente
        self.clientLabelName = Label(text="Ingrese el cliente:", font=("Arial", 12) ) 
        self.clientLabelName.grid(column=0, row=3, padx=6, pady=6, sticky='w')

        self.clientInput = Entry(width=40, font=("Arial", 12))
        self.clientInput.grid(column=1, row=3, padx=6, pady=6, sticky='w') 

        # #Dep
        self.depLabelName = Label(text="Ingrese el departamento:", font=("Arial", 12) ) 
        self.depLabelName.grid(column=0, row=5, padx=6, pady=6, sticky='w')

        self.depInput = Entry(width=40, font=("Arial", 12))
        self.depInput.grid(column=1, row=5, padx=6, pady=6, sticky='w')

        # #orderProduction
        self.orderProductionLabelName = Label(text="Ingrese N° Order:", font=("Arial", 12) ) 
        self.orderProductionLabelName.grid(column=0, row=7, padx=6, pady=6, sticky='w')

        self.orderProductionInput = Entry(width=40, font=("Arial", 12))
        self.orderProductionInput.grid(column=1, row=7, padx=6, pady=6, sticky='w')

        # #dateSave
        self.dateSaveLabelName = Label(text="Ingrese fecha de ingreso:", font=("Arial", 12) ) 
        self.dateSaveLabelName.grid(column=0, row=9, padx=6, pady=6, sticky='w')

        self.dateSaveInput = Entry(width=40, font=("Arial", 12))
        self.dateSaveInput.grid(column=1, row=9, padx=6, pady=6, sticky='w')

        # #Select File
        self.selectFileButton = Button(text="Select", font=("Arial", 12), command=self.chooseFile)
        self.selectFileButton.grid(column=0, row=10, padx=6, pady=6, sticky='w')

        self.routeFile=Entry(width=60, font=("Arial", 8)) 
        self.routeFile.grid(column=1, row=10, padx=6, pady=6, sticky='w')

        # #Generate Data
        self.getDataButton = Button( state="normal",text="Enviar", font=("Arial", 12), command=self.generateFilesData)
        self.getDataButton.grid(column=0, row=11, padx=6, pady=6, sticky='w')


    def chooseFile(self):

        # Abrir el explorador de archivos en la ruta especificada
        self.statusApp = YES

        ruta_archivo = filedialog.askopenfilename()
        self.nameRouteFile = ruta_archivo

        self.routeFile.insert(0, ruta_archivo) 


    def generateFilesData(self):
           
        #self.proyectInput.set(self.proyectInput.get() + 1)
        
        proyectValue = self.proyectInput.get().upper()
        clientValue = self.clientInput.get().upper()
        depValue = self.depInput.get().upper()
        orderProductionValue = self.orderProductionInput.get().upper()
        dateSaveValue = self.dateSaveInput.get().upper()
        
        tuplaInformationHead = [proyectValue, clientValue, depValue, orderProductionValue, dateSaveValue]
        tuplaArrayCases = getDataClasificated(self.nameRouteFile)

        for segmentEnd in tuplaArrayCases:
            createDocuments(segmentEnd, tuplaInformationHead )




    

  
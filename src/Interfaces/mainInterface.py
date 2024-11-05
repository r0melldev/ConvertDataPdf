import tkinter as tk
import os
from tkinter import filedialog

from src.TablePDF.__main__ import createDocuments
from src.HandleData.importExelData import getDataClasificated
from src.HandleData.generateReportData import repotDataVerefication
from src.HandleData.generateReportData import createReportFile

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        
        self.title("Klass App")
        self.geometry("600x400")
        icon_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'favicon.ico')
        self.iconbitmap(icon_path)
        
        # Container to hold all the frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        
        # Make the container expand with window resize
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("StartPage")
    
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        label = tk.Label(self, text="Opciones de Clasificación")
        label.pack(pady=10, padx=10)
        
        button1 = tk.Button(self, text="MUEBLES",
                            command=lambda: controller.show_frame("PageOne"))
        button1.pack()
        
        button2 = tk.Button(self, text="COMPLEMENTOS",
                            command=lambda: controller.show_frame("PageTwo"))
        button2.pack()

        
class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__(parent)
        self.controller = controller

        self.nameRouteFile = ''
        
        titleLabel = tk.Label(self, text="Clasificacion Muebles", font=("Arial", 12))
        
        titleLabel.grid(column=0, row=0, padx=6, pady=6, sticky='w')

        homeButton = tk.Button(self, text="Volver a la página de inicio",
                           command=lambda: controller.show_frame("StartPage"))
        
        homeButton.grid(column=0, row=1, padx=6, pady=6, sticky='w')
   
        # #Proyect
        self.proyectLabelName = tk.Label(self, text="Ingrese el proyecto:", font=("Arial", 12))       
        self.proyectLabelName.grid(column=0, row=2, padx=6, pady=6, sticky='w')
     
        self.proyectInput = tk.Entry(self, width=40, font=("Arial", 12))
        self.proyectInput.grid(column=1, row=2, padx=6, pady=6, sticky='w')

        # #Cliente
        self.clientLabelName = tk.Label(self, text="Ingrese el cliente:", font=("Arial", 12) ) 
        self.clientLabelName.grid(column=0, row=3, padx=6, pady=6, sticky='w')

        self.clientInput = tk.Entry(self, width=40, font=("Arial", 12))
        self.clientInput.grid(column=1, row=3, padx=6, pady=6, sticky='w') 

        # #Dep
        self.depLabelName = tk.Label(self, text="Ingrese el departamento:", font=("Arial", 12) ) 
        self.depLabelName.grid(column=0, row=5, padx=6, pady=6, sticky='w')

        self.depInput = tk.Entry(self, width=40, font=("Arial", 12))
        self.depInput.grid(column=1, row=5, padx=6, pady=6, sticky='w')

        # #orderProduction
        self.orderProductionLabelName = tk.Label(self, text="Ingrese N° Order:", font=("Arial", 12) ) 
        self.orderProductionLabelName.grid(column=0, row=7, padx=6, pady=6, sticky='w')

        self.orderProductionInput = tk.Entry(self, width=40, font=("Arial", 12))
        self.orderProductionInput.grid(column=1, row=7, padx=6, pady=6, sticky='w')

        # #dateSave
        self.dateSaveLabelName = tk.Label(self, text="Ingrese fecha de ingreso:", font=("Arial", 12) ) 
        self.dateSaveLabelName.grid(column=0, row=9, padx=6, pady=6, sticky='w')

        self.dateSaveInput = tk.Entry(self, width=40, font=("Arial", 12))
        self.dateSaveInput.grid(column=1, row=9, padx=6, pady=6, sticky='w')

        # #Select File
        self.selectFileButton = tk.Button(self, text="Select", font=("Arial", 12), command = self.chooseFile)       
        self.selectFileButton.grid(column=0, row=10, padx=6, pady=6, sticky='w')

        self.routeFile = tk.Entry(self, width=60, font=("Arial", 8)) 
        self.routeFile.grid(column=1, row=10, padx=6, pady=6, sticky='w')

        # #Generate Data
        self.getDataButton = tk.Button(self, state="normal",text="Enviar", font=("Arial", 12), command=self.generateFilesData)      
        self.getDataButton.grid(column=0, row=11, padx=6, pady=6, sticky='w')


    def chooseFile(self):

        # Open exploreFile
        ruta_archivo = filedialog.askopenfilename()
        
        self.nameRouteFile = ruta_archivo
        
        self.routeFile.insert(0, ruta_archivo) 

    def generateFilesData(self):

        proyectValue = self.proyectInput.get().upper()
        clientValue = self.clientInput.get().upper()
        depValue = self.depInput.get().upper()
        orderProductionValue = self.orderProductionInput.get().upper()
        dateSaveValue = self.dateSaveInput.get().upper()
        
        # Get header for Pdf to interface
        tuplaInformationHead = [proyectValue, clientValue, depValue, orderProductionValue, dateSaveValue]
        
        # Get data of exel route
        tuplaArrayCases = getDataClasificated(self.nameRouteFile, 1)
        
        # Get report of process cells 
        dataInformationReport = repotDataVerefication(tuplaArrayCases)

        # Create a report document 
        createReportFile(dataInformationReport, 1, orderProductionValue )

        
        for segmentEnd in tuplaArrayCases:
            createDocuments(segmentEnd, tuplaInformationHead, 1)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.nameRouteFile = ''
        self.optionClas = 2

        # Construct form
        titleLabel = tk.Label(self, text="Clasificacion Complementos")
        titleLabel.grid(column=0, row=0, padx=6, pady=6, sticky='w')
        
        homeButton = tk.Button(self, text="Volver a la página de inicio",
                           command=lambda: controller.show_frame("StartPage"))
        
        homeButton.grid(column=0, row=1, padx=6, pady=6, sticky='w')
        

        self.proyectLabelName = tk.Label(self, text="Ingrese el proyecto:", font=("Arial", 12))       
        self.proyectLabelName.grid(column=0, row=2, padx=6, pady=6, sticky='w')
     
        self.proyectInput = tk.Entry(self, width=40, font=("Arial", 12))
        self.proyectInput.grid(column=1, row=2, padx=6, pady=6, sticky='w')

        # #Cliente
        self.clientLabelName = tk.Label(self, text="Ingrese el cliente:", font=("Arial", 12) ) 
        self.clientLabelName.grid(column=0, row=3, padx=6, pady=6, sticky='w')

        self.clientInput = tk.Entry(self, width=40, font=("Arial", 12))
        self.clientInput.grid(column=1, row=3, padx=6, pady=6, sticky='w') 

        # #Dep
        self.depLabelName = tk.Label(self, text="Ingrese el departamento:", font=("Arial", 12) ) 
        self.depLabelName.grid(column=0, row=5, padx=6, pady=6, sticky='w')

        self.depInput = tk.Entry(self, width=40, font=("Arial", 12))
        self.depInput.grid(column=1, row=5, padx=6, pady=6, sticky='w')

        # #orderProduction
        self.orderProductionLabelName = tk.Label(self, text="Ingrese N° Order:", font=("Arial", 12) ) 
        self.orderProductionLabelName.grid(column=0, row=7, padx=6, pady=6, sticky='w')

        self.orderProductionInput = tk.Entry(self, width=40, font=("Arial", 12))
        self.orderProductionInput.grid(column=1, row=7, padx=6, pady=6, sticky='w')

        # #dateSave
        self.dateSaveLabelName = tk.Label(self, text="Ingrese fecha de ingreso:", font=("Arial", 12) ) 
        self.dateSaveLabelName.grid(column=0, row=9, padx=6, pady=6, sticky='w')

        self.dateSaveInput = tk.Entry(self, width=40, font=("Arial", 12))
        self.dateSaveInput.grid(column=1, row=9, padx=6, pady=6, sticky='w')

        # #Select File
        self.selectFileButton = tk.Button(self, text="Select", font=("Arial", 12), command = self.chooseFile2)       
        self.selectFileButton.grid(column=0, row=10, padx=6, pady=6, sticky='w')

        self.routeFile = tk.Entry(self, width=60, font=("Arial", 8)) 
        self.routeFile.grid(column=1, row=10, padx=6, pady=6, sticky='w')

        # #Generate Data
        self.getDataButton = tk.Button(self, state="normal",text="Enviar", font=("Arial", 12), command=self.generateFilesData2)      
        self.getDataButton.grid(column=0, row=11, padx=6, pady=6, sticky='w')


    def chooseFile2(self):

        # Open exploreFile
        ruta_archivo = filedialog.askopenfilename()
        
        self.nameRouteFile = ruta_archivo
        
        self.routeFile.insert(0, ruta_archivo) 


    def generateFilesData2(self):
           
        proyectValue = self.proyectInput.get().upper()
        clientValue = self.clientInput.get().upper()
        depValue = self.depInput.get().upper()
        orderProductionValue = self.orderProductionInput.get().upper()
        dateSaveValue = self.dateSaveInput.get().upper()
        
        # Get header for Pdf to interface
        tuplaInformationHead = [proyectValue, clientValue, depValue, orderProductionValue, dateSaveValue]
        
        # Get data of exel route
        tuplaArrayCases = getDataClasificated(self.nameRouteFile, 2)
        
        # Get report of process cells 
        dataInformationReport = repotDataVerefication(tuplaArrayCases)

        # Create a report document 
        createReportFile(dataInformationReport, 2, orderProductionValue )
        

        for segmentEnd in tuplaArrayCases:
            createDocuments(segmentEnd, tuplaInformationHead, 2)







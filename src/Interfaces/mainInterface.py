from tkinter import *

testlista= []

def testInterface():
    print("hola mundo")

 

    
    def getDataForm():
        proyectValue = proyectInput.get()
        clientValue = clientInput.get()
        depValue = depInput.get()
        orderProductionValue = orderProductionInput.get()
        dateSaveValue = dateSaveInput.get()

        tuplaInformationHead = [proyectValue, clientValue, depValue, orderProductionValue, dateSaveValue]

        testlista = tuplaInformationHead

        print(tuplaInformationHead)
        
        return tuplaInformationHead


    screenMain = Tk()
    screenMain.title('Principal interface')
    screenMain.minsize(width=500, height=500)
    screenMain.config(padx=35, pady=35)

    
    #Header 
    #titleName = Label(screenMain, text="Muebleria") 
    #titleName.pack()
    #titleName.grid(column=0, row=0)
    
    # spaceLabelName = Label( text="", font=("Arial", 10)) 
    # spaceLabelName.grid(column=0)

    #Proyect
    proyectLabelName = Label(text="Ingrese el proyecto:", font=("Arial", 10)) 
    proyectLabelName.grid(column=0, row=1)

    proyectInput = Entry(width=20, font=("Arial", 10))
    proyectInput.grid(column=1, row=1) 

    spaceLabelName = Label( text="", font=("Arial", 10)) 
    spaceLabelName.grid(column=0)

    #Cliente
    clientLabelName = Label(text="Ingrese el cliente:", font=("Arial", 10) ) 
    clientLabelName.grid(column=0, row=3)

    clientInput = Entry(width=20, font=("Arial", 10))
    clientInput.grid(column=1, row=3) 

    spaceLabelName = Label( text="", font=("Arial", 10)) 
    spaceLabelName.grid(column=0)

    #Dep
    depLabelName = Label(text="Ingrese el departamento:", font=("Arial", 10) ) 
    depLabelName.grid(column=0, row=5)

    depInput = Entry(width=20, font=("Arial", 10))
    depInput.grid(column=1, row=5)

    spaceLabelName = Label( text="", font=("Arial", 10)) 
    spaceLabelName.grid(column=0)
  
    #orderProduction
    orderProductionLabelName = Label(text="Ingrese N° Order:", font=("Arial", 10) ) 
    orderProductionLabelName.grid(column=0, row=7)

    orderProductionInput = Entry(width=20, font=("Arial", 10))
    orderProductionInput.grid(column=1, row=7)

    spaceLabelName = Label( text="", font=("Arial", 10)) 
    spaceLabelName.grid(column=0)
  
    #dateSave
    dateSaveLabelName = Label(text="Ingrese el departamento:", font=("Arial", 10) ) 
    dateSaveLabelName.grid(column=0, row=9)

    dateSaveInput = Entry(width=20, font=("Arial", 10))
    dateSaveInput.grid(column=1, row=9)

    spaceLabelName = Label( text="", font=("Arial", 10)) 
    spaceLabelName.grid(column=0)

    getDataButton = Button(text="Enviar", font=("Arial", 10), command=getDataForm)
    getDataButton.grid(column=0, row=11)

    screenMain.mainloop()






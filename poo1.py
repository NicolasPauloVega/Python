#Creamos una clase para definir cada metodo del programa.
class Computadores():

    #Creamos atributos para identificar el diccionario
    id = 0
    dispositivo = ""
    ambiente = 0
    addPc = {}

    #Creamos un metodo cuya funcion sea agregar la informacion a una computadora.
    def agregarComputador(self):

        #Creamos una variable que identifiquecuantos computadores se registran
        agr = int(input("¿Cuantos computadores desea ingresar?: "))

        #Se crea un bucle que se encarga de realizar el registro las veces que digito el usuario.
        for i in range(agr):

            #Se agregan los datos correspondientes al diccionaro id, dispositivos, ambiente y propietario.
            self.id = int(input("Ingresa el id del dispositivo: "))
            self.dispositivo = input("El dispositivo trae cargador y/o mouse: ")
            self.ambiente = int(input("Ingresa el numero de ambiente al que pertence el computador: "))
            self.propietario = input("Ingresa el nombre del aprendis encargado del computador: ")
            print("\nSe añadio el computador al ambiente: " + str(self.ambiente) + " con la id: " + str(self.id) + " con sus respectivos dispositivos: " + self.dispositivo.title() + ".")
        
        self.addPc.update({str(self.id): {"dispositivos": self.dispositivo.title()}, "Ambiente": {self.ambiente}, "Propietario": {self.propietario.title()}})
        print(self.addPc)

    #Se crea un metodo que permita editar la informacion de un computador.
    def editarPc(self):
        
        #Le preguntamos al usuario si va a editar la informacion de un computador.
        editar = input("¿Deseas editar un computador? (Ingresa si o no): ")

        #Se crea una condicion la cual si el usuario digita si se ejecute el codigo
        if editar == "si":

            #Se pregunta al usuario si va aeditar el dispositivo
            disp = input("\n¿Deseas editar el dispositivo? (Ingresa si o no): ")

            #Se inicia una condicion la cual si digita "si" empieza la edicion del dispositivo por la id.
            if disp.lower() == "si":

                num = input("\nIngresa el id del computador: ") #Se pregunta por la id
                ing = input("Ingresa el nuevo dispositivo: ")
                self.addPc[num]["dispositivos"] = ing
                print(f"\nSe edito el dispositivo del computador con la id ({num}): {self.addPc}")
            else:
                print("No se edito el dispositivo.")
            
            #Se pregunta si se edita el ambiente
            ambiente = input("\n¿Deseas editar el ambiente? (Ingresa si o no): ")

            #Se inicia una condicion la cual si digita "si" empieza la edicion del ambiente por la id.
            if ambiente.lower() == "si":
                
                num1 = input("\nIngresa el id del computador: ")
                ing1 = input("Ingresa el nuevo ambiente: ")

                self.addPc[num1]["Ambiente"] = ing1
                print(f"\nSe edito el ambiente del computador con la id ({num1}: {self.addPc})")
            else:
                print("No se cambio el ambiente.")

            #Se pregunta si se edita al propietario.
            propietario = input("¿Deseas ingresar un nuevo propietario al computador? (Ingresa si o no): ")

            #Se inicia una condicion la cual se digita "si" empieza la edicion del propietario por la id.
            if propietario.lower() == "si":

                num2 = input("\nIngresa el id del computador: ")
                ing2 = input("Ingresa el nuevo propietario: ")

                self.addPc[num2]["Propietario"] = ing2
                print(f"\nSe edito el ambiente del computador con la id ({num2}: {self.addPc})")
            else:
                print("No se cambio al propietario")
        #Finaliza la condicion si se digita "no".
        else:
            print("No se realizo ninguna edicion en los computadores.")
    
    #Se crea un metodo el cual nos permita eliminar la informacion de un computador.
    def eliminarInfoPc(self):
        
        #Se pregunta al usuario si desea eliminar la informacion de un computador
        eliminar = input("¿Deseas eliminar la informacion de la pc? (Ingresa si o no): ")
        
        #Se inicia una condicion la cual si se digita "si" ejecute el codigo.
        if eliminar.lower() == "si":

            #Se pregunta al usuario si desea eliminar el dispositivo.
            disp = input("\n¿Deseas eliminar el dispositivo de los computadores? (Ingresa si o no): ")

            #Se inicia una condicion que digita "si" pida la id del computador y elimine el dispositivo.
            if disp == "si":

                num = input("\nIngresa la id del computador: ")
                del self.addPc[num]["dispositivos"]
                print(f"\nSe eliminaron los dispositivos de los computadores.\nEl registro del computador quedo asi: {self.addPc}")
            else:
                print("No se eliminaron los dispositivos.")
            
            #Se pregunta al usuario si desea eliminar el ambiente del computador.
            ambiente = input("\n¿Deseas eliminar el ambiente del computador? (Ingresa si o no):")

            #Se inicia una condicion que digita "si" pida la id del computador y elimine el ambiente.
            if ambiente.lower() == "si":

                num1 = input("\nIngresa la id del computador: ")
                del self.addPc[num1]["Ambiente"]
                print(f"Se elimino el ambiente del computador {num1}.\nEl registro del computador quedo asi: {self.addPc}.")
            else:
                print("No se elimino el ambiente del computador.")

            #Se pregunta si se desea eliminar al propietario del computador.
            propietario = input("\n¿Deseas eliminar al propietario del computador? (Ingresa si o no): ")

            #Se inicia una condicion que digita "si" pida la id del computador y elimine al propietario.
            if propietario.lower() == "si":

                num2 = input("\nIngresa el numero de id del computador : ")
                del self.addPc[num2]["Propietario"]
                print(f"\nSe elimino al propietario del computador: {num2}.\nEl registro del computador quedo asi: {self.addPc}.")
            else:
                print("No se elimino al propietario de este computador.")
        #Finaliza la codicion si el usuario digita "no"
        else:
            print("No se elimino nada en este dispositivo.")
    
    #Se crea un metodo que permita ingresar una novedad del dispositivo.
    def agregarNovedad(self):

        #Se pregunta al usuario si desea ingresar alguna novedad.
        novedad = input("¿Deseas agregar alguna novedad al dispositivo? (Ingresa si o no): ")

        #Si inicia una condicion la cual si el usuario digita "si" se ejecute el codigo.
        if novedad.lower() == "si": 
            
            #Se ingresa la id del computador
            num = input("\nIngresa la id del dispositivo con la novedad: ")

            #Se pregunta ¿cual es la novedad? que ingresa del computador.
            novedad1 = input("¿Cual es la novedad del dispositivo?: ")

            #Se añade la novedad a la id del dispositivo y se imprime los registros completos.
            self.addPc[num]["Novedad"] = novedad1
            print(f"\nSe agrego la novedad al computador ({num}).\nEl registro de la novedad: {self.addPc}.")
        #Si el usuario ingresa "no" la condicion no se cumple.
        else:
            print("No se agregaron novedades a los dispositivos.")

    #Creamos un metodo que permite buscar la novedad de un quipo.
    def MostrarNovedad(self):
        
        #Se pregunta si se desea ver el ultimo registro de novedad que se realizo
        mostrarNovedad = input("¿Deseas ver la ultima novedad agregado? (Ingresa si o no): ")

        #Se inicia una condicion que si digita "si" se ejecuta el codigo.
        if mostrarNovedad.lower() == "si":
            
            #Se ingresa la id de la novedad a la cual se desea ver
            num = input("\nIngresa la id del computador que deseas ver la novedad: ")
            
            #Se imprime el registro de la novedad que se desea ver.
            print(f"\nEl registro de la novedad del computador ({num}) es: {self.addPc[num]["Novedad"]}")
        #Se finaliza la condicion si el usuario digita "no"
        else:
            print("No se mostro la novedad del computador.")

    #Se crea un metodo el cual busque un computador.
    def buscarEquipo(self):

        #Se le pregunta al usuario si desea buscar un computador.
        buscarEquipo = input("¿Desea buscar un computador (Ingresa si o no): ")

        #Se inicia una condicion la cual si el usuario digita "si" ejecute el codigo
        if buscarEquipo.lower() == "si":

            #Se pide la id del computador que se desea buscar.
            num = input("\nIngresa la id del dispositivo que deseas buscar: ")

            #Se imprime el regitro del computador buscado.
            self.addPc[num]
        #Se finaliza la condicion si el usuario digita "no"
        else:
            print("No se busco ningun equipo.")
            
computadores = Computadores()

#Creamos un menu que identifique que se desea hacer.
while True:

    print("Ingresa los siguientes numeros para el trabajo que deseas hacer:\n1)Agregar computadores.\n2)Editar computador.\n3)Eliminar computador.\n4)Agregar novedad.\n5)Mostrar novedad.\n6)Buscar equipo\n7)Para salir")

    menu = int(input(""))

    if menu == 1:
        computadores.agregarComputador()
        print()
    elif menu == 2:
        computadores.editarPc()
        print()
    elif menu == 3:
        computadores.eliminarInfoPc()
        print()
    elif menu == 4:
        computadores.agregarNovedad()
        print()
    elif menu == 5:
        computadores.MostrarNovedad()
        print()
    elif menu == 6:
        computadores.buscarEquipo()
        print()
    else:
        print("Gracias por usar nuestro programa :)")
    break

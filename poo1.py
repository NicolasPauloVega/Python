class Computadores():

    id = 0
    dispositivo = ""
    ambiente = 0
    addPc = {}

    def agregarComputador(self):

        agr = int(input("¿Cuantos computadores desea ingresar?\n"))

        for i in range(agr):

            self.id = int(input("Ingresa el id del dispositivo: "))
            self.dispositivo = input("El dispositivo trae cargador y/o mouse: ")
            self.ambiente = int(input("Ingresa el numero de ambiente al que pertence el computador: "))
            print("Se añadio el computador al ambiente: " + str(self.ambiente) + " con la id: " + str(self.id) + " con sus respectivos dispositivos: " + self.dispositivo.title() + ".\n")
        
        self.addPc.update({str(self.id): {"dispositivos": self.dispositivo.title(), "Ambiente": self.ambiente}})
        print(self.addPc)

    def editarComputador(self):

        com = input("¿Deseas cambiar alguna informacion de los equipos?  (si o no)")

        if com.lower() == "si":

            num = int(input("Ingresa el numero de id del computador: "))

            sn = input("Deseas cambiar el dispositivos. (si o no) ")

            if sn.lower() == "si":
                disp = input("Ingresa los nuevos dispositivos. \n")
                self.addPc[num]["Dispositivos"] = disp
            else:
                print("No se cambio los dispositivos. \n")

            sn1 = input("¿Deseas cambiar el ambiente? (si o no)")

            if sn1.lower() == "si":
                amb = int(input("Ingresa el nuevo numero del ambiente: "))
                self.addPc[num]["Ambiente"] = amb
            else:
                print("No se agrego el ambiente. \n")
            print(self.addPc)
        else:
            print("No se cambia nada en los computadores.\n")

computadores = Computadores()

computadores.agregarComputador()
print()
computadores.editarComputador()
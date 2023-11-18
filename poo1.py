class Computadores():

    id = 0
    dispositivo = ""
    ambiente = 0
    addPc = {}

    def agregarComputador(self):

        agr = int(input("¿Cuantos computadores desea ingresar? "))

        for i in range(agr):

            self.id = int(input("Ingresa el id del dispositivo: "))
            self.dispositivo = input("El dispositivo trae cargador y/o mouse: ")
            self.ambiente = int(input("Ingresa el numero de ambiente al que pertence el computador: "))
            self.propietario = input("Ingresa el nombre del aprendis encargado del computador: ")
            print("Se añadio el computador al ambiente: " + str(self.ambiente) + " con la id: " + str(self.id) + " con sus respectivos dispositivos: " + self.dispositivo.title() + ".\n")
        
        self.addPc.update({str(self.id): {"dispositivos": self.dispositivo.title(), "Ambiente": self.ambiente}, "Propietario": {self.propietario}})
        print(self.addPc)

    def editarPc(self):

        inf = ("¿Deseas cambiar la informacion del computador? (si o no): ")

        if inf.lower() == "si":

            num = int(input("Ingresa el numero que corresponde al cambio que quieres hacer:\n1)Cambiar dispositivo.\n2)cambiar ambiente.\n3)cambiar propietario.\notro para salir del menú.\n"))

            while num != 0:

                if num == 1:

                    com = int(input("Ingresa el numero de id que deseas cambiar: "))

                    if com in self.addPc:
                        disp = input("Ingresa los nuevos dispositivos del computador: ")
                        self.addPc[disp]["dispositivos"] = disp
                    else:
                        print("No se cambio nada en el computador. ")
                        continue

                elif num == 2:

                    comp = int(input("Ingresa el numero de id que deseas cambiar: "))

                    if comp in self.addPc:
                        amb = int(input("Ingresa el nuevo ambiente del computador: "))
                        self.addPc[amb]["Ambiente"] = amb
                    else:
                        print("No se cambio nada en el computador. ")
                        continue
                
                elif num == 3:

                    comu = int(input("Ingresa el numero de id que deseas cambiar: "))

                    if comu in self.addPc:
                        pro = input("Ingresa el nombre del aprendis encargado del computador: ")
                        self.addPc[pro]["Propietario"] = pro
                    else:
                        print("No se cambio al propietario. ")
                        continue
                else:
                    print("No se realizo ningun cambio.")
                    break
        else:
            print("No se realizo ningun cambio. ")


computadores = Computadores()

computadores.agregarComputador()
print()
computadores.editarPc()
print()

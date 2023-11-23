idV = 0
nombre = ""
num = 0
votante = {}
candidato = {
        1: {
            "Identificacion": 1104938806,
            "Nombre": "Gustavo Puerta"
        },
        2: {
            "Identificacion": 1127586877,
            "Nombre": "Carlos Luiz"
        },
        3: {
            "Identificacion": 65765786,
            "Nombre": "Daniela Vargas"
        },
        4: {
            "Identificacion": 71456896,
            "Nombre": "Luisa Gimenez"
        },
        5: {
            "Identificacion": 0,
            "Nombre": "Blanco"
        }
    }



class postulado():

    def registro():

        vot = int(input("Ingresa el numero de personas que van a entrar a votar: "))
        
        for i in range(vot):

            idV = int(input("¿Cual es tu numero de identificacion: "))
            nombre = input("¿Cual es tu nombre? ")

            votante.update({idV: {"Nombre": nombre}})

        print(votante)

    def ingreso():

        id = int(input("Ingresa el numero de id del votante: "))

        print(votante[id])

    def votCand():
        
        cont = 0
        cont1 = 0
        cont2 = 0
        cont3 = 0
        cont4 = 0

        while True:

            print("Escoge un de los candidatos siguiendo las siguientes reglas:\n-Debes escribir solo numeros si dijitas alguna letra saldra un error.\n-Debes escoger a consiencia\n1)Gustavo Puerta.\n2)Carlos Luis.\n3)Luisa Gimenez.\n4)Daniela Vargas.\n5)Voto en blanco.\n")

            num = int(input("\n"))

            if num == 1:
                id = 1
                print(candidato[id])
                cont += 1
            elif num == 2:
                id = 2
                print(candidato[id])
                cont1 += 1
            elif num == 3:
                id = 3
                print(candidato[id])
                cont2 += 1
            elif num == 4:
                id = 4
                print(candidato[id])
                cont3 += 1
            elif num == 5:
                id == 5
                print(candidato[id])
                cont4 += 1
            else:
                print("El votante no se encuentra en el regitro intentalo de nuevoo.")
                continue

            break

        print("Este es el conteo de los candidatos: ")

        print(f"Gustavo tuvo un total de: {cont} votos.")
        
postulado.votCand()
postulado.registro()
postulado.ingreso()



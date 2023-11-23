#creamos variables que nos permita el ingreso de datos a un diccionario
idV = 0
nombre = ""
num = 0
#Creamos un diccionario que almacene las variables anteriores
votante = {}
#Creamos un diccionario que almacene la informacion acerca de los candidatos a la voceria.
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
            "Nombre": "Voto en blanco"
        }
    }

#Creamos una clase que realiza el proceso de votacion.
class postulado():

    #Creamos un metodo que permita agregar votantes al diccionario votantes.
    def registro():

        #Creamos una variable que almacene la cantidad de votantes que se necesite.
        vot = int(input("Ingresa el numero de personas que van a entrar a votar: "))
        
        #Creamos un bucle el cual nos permita agregar la cantidad propuesta de los votantes.
        for i in range(vot):

            #Creamos unas variables que nos permitan agregar la id y el nombre en el diccionario.
            idV = int(input("¿Cual es tu numero de identificacion: "))
            nombre = input("¿Cual es tu nombre? ")

            #Agregamos los datos al diccionario.
            votante.update({idV: {"Nombre": nombre}})

        #Imprimimos el diccionario.
        print(votante)

    #Creamos un metodo que permita el ingreso de un usuario para poder votar.
    def ingreso():

        id = int(input("Ingresa el numero de id del votante: "))

        print(votante[id])

    #Creamos un metodo que permita votar por un candidato y los cuente mostrando el que mas votos tuvo y el que menos votos tuvo.
    def votCand():
        
        #Se crean variables para poder contar la cantidad de votos.
        cont = 0
        cont1 = 0
        cont2 = 0
        cont3 = 0
        cont4 = 0

        #Creamos un bucle que pregunte cuantos votantes hay para que se pueda calcular por la misma cantidad que se desea votar.
        while True:

            print("Escoge un de los candidatos siguiendo las siguientes reglas:\n-Debes escribir solo numeros si dijitas alguna letra saldra un error.\n-Debes escoger a consiencia\n1)Gustavo Puerta.\n2)Carlos Luis.\n3)Luisa Gimenez.\n4)Daniela Vargas.\n5)Voto en blanco.\n")

            num = int(input("\n"))

            #Se crean condiciones en las cuales mostrara al candidato que se desea votar y contara la cantidad de votos.
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
        
        #Se mostrar el conteo de cada voto por cantidato y cuantos votos totales hay.
        print("\nEste es el conteo de votos de los candidatos: ")

        print(f"Gustavo Puerta tuvo un total de: {cont} votos.")
        print(f"Carlos Luis tuvo un total de: {cont1} votos.")
        print(f"Daniela Vargas tuvo un total de: {cont2} votos.")
        print(f"Luisa Gimenez tuvo un total de: {cont3} votos.")
        print(f"Voto en blanco tuvo un total de: {cont4} votos.")

        suma = cont+cont1+cont2+cont3+cont4

        print(f"Este es el total de votos. {suma}")

        
#Se imprime cada uno de los metodos de la clase.
postulado.registro()
postulado.ingreso()
postulado.votCand()


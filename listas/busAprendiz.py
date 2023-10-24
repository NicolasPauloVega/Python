#Creamos una lista llamada aprendices con unos valores predeterminados y otra vacia llamada edades
aprendices = ["Juan Diego","Mathew Guarnizo","Maria Fernanda","Melissa","Nicolas Paulo","Miguel Angel","Stiven","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly","Camila","Stiwar","Lina Vanesa","Paula Garcia","Maria Paula","Vanesa","Kevin Hernandez","Yency","Matias","Sebastian Tovar","Cristian Peña","Dahiana","Kevin Eduardo","Santiago Tomas","Nicolas Fierro","Laura Benavidez","Willfran"]
edades = []

#Importamos el modulo ramdom el cual genera numeros aleatorios
import random

#Creamos un bucle el cual genera un total de 30 iteraciones.
for i in range(30):
    #creamos una variable la cual dara numeros randoms con la funcion "radint" que empiezan del 16 y terminan en el 20
    edad = random.randint(16,20)
    #Agregamos los datos de la variable edad a la lista edades
    edades.append(edad)

print(aprendices) #Imprimimos los resultados de las listas
print(edades)     #y edades

#Creamos una variable la cual pregunte si desea buscar un aprendiz o por el nombre o por la edad
entrar = input("Deseas buscar por nombre [n] o por edades[e]")

#creamos unas condiciones las cuales busque al aprendiz ya sea por el nombre [n] o por la edad [e]
if entrar.lower() == "n":

    buscar = input("Digita el nombre del aprendiz que desea buscar: ")

    if buscar in aprendices:
        encN = aprendices.index(buscar)
        edad = edades[encN]

        print(f"La persona que buscas se llama {buscar} y tiene {edad} años de edad")
    else:
        print("La persona a la que buscas no esta en las lista que posee el programa.")
elif entrar.lower() == "e":

    buscar = int(input("Digita la edad del aprendiz que desea buscar: "))

    if buscar in edades:
        encE = edades.index(buscar)
        name = aprendices[encE]

        print(f"El aprendiz que buscas tiene {buscar} años de edad y se llama {name}")
    else:
        print("La persona a la que buscas no esta en las lista que posee el programa.")
else:
    print("Error... La persona que buscas no esta en mis registros")

# aprendices1 = ["Juan Diego","Mathew Guarnizo","Maria Fernanda","Melissa","Nicolas Paulo","Miguel Angel","Stiven","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly","Camila","Stiwar","Lina Vanesa","Paula Garcia","Maria Paula","Vanesa","Kevin Hernandez","Yency","Matias","Sebastian Tovar","Cristian Peña","Dahiana","Kevin Eduardo","Santiago Tomas","Nicolas Fierro","Laura Benavidez","Willfran"]
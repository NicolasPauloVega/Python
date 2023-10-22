#Creamos 2 listas vacias
aprendices = []
edades = []

#Creamos un bucle el cual almacene los nombres y las edades de los aprendices y los agrege a la lista
for i in range(30):
    registro = input("Ingresa el nombre del aprendiz: ")
    registro1 = int(input("Ingresa la edad del aprendiz: "))

    aprendices.append(registro)
    edades.append(registro1)

#Imprimimos las listas con los nuevos valores
print(aprendices)
print(edades)

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
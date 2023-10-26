#Indique un dato a buscar en la lista de aprendices

aprendices = ["Juan Diego","Mathew Guarnizo","Maria Fernanda","Melissa","Nicolas Paulo","Miguel Angel","Stiven","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly","Camila","Stiwar","Lina Vanesa","Paula Garcia","Maria Paula","Vanesa","Kevin Hernandez","Yency","Matias","Sebastian Tovar","Cristian Peña","Dahiana","Kevin Eduardo","Santiago Tomas","Nicolas Fierro","Laura Benavidez","Willfran"]
edades = []

import random

for i in range(30):
    edad = random.ramdint(16,20)
    edades.append(edad)

print(aprendices)
print(edades)

entrar = input("Deseas buscar por nombre [N o n] o por edades[E o e]")

if entrar == "E":
    buscar = input("Digita el nombre del aprendiz que desea buscar: ")
    
    if buscar in aprendices:
        encN = aprendices.indes(buscar)
        edad = edades[enc]
        print(f"La persona que buscas se llama {buscar} y tiene {edad} años de edad")
    else:
        print("La persona a la que buscas no esta en las lista que posee el programa.")
elif entrar == "N":
    buscar = int(input("Digita la edad del aprendiz que desea buscar: "))
    if buscar in edades:
        encE = edades.index(buscar)
        name = aprendices[enc]
        print(f"El aprendiz que buscas tiene {buscar} años de edad y se llama {name}")
    else:
        print("La persona a la que buscas no esta en las lista que posee el programa.")
else:
    print("Error... La persona que buscas no esta en mis registros")
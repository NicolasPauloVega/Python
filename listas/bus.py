aprendices = []
edades = []

for i in range(2):
    registro = input("Ingresa el nombre del aprendiz: ")
    registro1 = int(input("Ingresa la edad del aprendiz: "))

    aprendices.append(registro)
    edades.append(registro1)

print(aprendices)
print(edades)

entrar = input("Deseas buscar por nombre [n] o por edades[e]")

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
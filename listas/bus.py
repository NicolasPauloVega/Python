aprendices = ["Adriana Lucia"]
edades = [0]

for i in range(2):
    registro = input("Ingresa el nombre del aprendiz: ")
    registro1 = int(input("Ingresa la edad del aprendiz: "))

    aprendices.append(registro)
    edades.append(registro1)

    print(aprendices)
    print(edades)
    continue

buscar = input("Digita la edad o el nombre de la persona a la que quieres buscar: ")

if buscar in aprendices:
    encN = aprendices.index(buscar)
    edad = edades[encN]

    print(f"La persona que buscas se llama {buscar} y tiene {edad} años de edad")
else:
    print("La persona a la que buscas no esta en las lista que posee el programa.")


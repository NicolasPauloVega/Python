aprendices = ["Adriana Lucia"]
edades = [0]

for i in range(30):
    registro = input("Ingresa el nombre del aprendiz: ")
    registro1 = int(input("Ingresa la edad del aprendiz: "))

    aprendices.append(registro)
    edades.append(registro1)

    print(aprendices)
    print(edades)
    continue

eliminar = input('deseas eliminar a la instructora "Adriana Lucia" de la lista [Dijitar si o no]')

if eliminar == "si":
    aprendices.remove("Adriana Lucia")
    edades.remove(0)
print(f"Se elimino a la instructora adriana de la lista aprendices. \n{aprendices}")
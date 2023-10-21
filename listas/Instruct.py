aprendices = []
edades = []

for i in range(30):
    registro = input("Ingresa el nombre del aprendiz: ")
    registro1 = int(input("Ingresa la edad del aprendiz: "))

    aprendices.append(registro)
    edades.append(registro1)

    print(aprendices)
    print(edades)

    aprendices.insert(0, "Adriana Lucia")
    edades.insert(0, "")
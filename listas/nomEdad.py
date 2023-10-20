aprendices = []
edades = []

for i in range(30):
    registro = input("Ingresa el nombre del aprendiz: ")
    registro1 = int(input("Ingresa la edad del aprendiz: "))

    aprendices.append(registro)
    edades.append(registro1)

    for registro, registro1 in zip(aprendices,edades):
        print(registro,registro1)
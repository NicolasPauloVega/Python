aprendices = []
edades = []

for i in range(30):
    registro = input("Ingresa el nombre del aprendiz: ")
    registro1 = int(input("Ingresa la edad del aprendiz: "))

    aprendices.append(registro)
    edades.append(registro1)

    print(aprendices)
    print(edades)

conteo = 0

for registro1 in edades:
    if registro1 == 18:
        conteo+=1

print(conteo)
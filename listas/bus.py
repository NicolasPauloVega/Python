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

buscar = input("Deseas buscar algun nombre (n) o alduna edad (e): ")

if buscar.lower() == "n":
    encNombre = input("Aquien deseas encontrar: ")
    print(aprendices.index(encNombre))
aprendices = []
edades = []

instructor = "Estos son los aprendices de la Instructora Adriana Lucia Rincon Forero"

for i in range(30):
    aprendiz = input("Digita el nombre del aprendiz: ")
    edad = int(input("Digita la edad del aprendiz: "))

    aprendices.append(aprendiz)
    edades.append(edad)

    print(instructor)
    print(aprendices)
    print(edades)
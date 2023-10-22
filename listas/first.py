#Creamos dos listas vacias llamadas aprendices y edades
aprendices = []
edades = []

#Creamos un bucle el cual registrara todos los valores ingresados tanto para la lista aprendices y edades
for i in range(30):
    registro = input("Digite el nombre del aprendiz: ")
    registro1 = int(input("Registre la edad del aprendiz: "))

    aprendices.append(registro)
    edades.append(registro1)

#Imprimimos las listas con sus respectivos valores
print(aprendices)
print(edades)

#Creamos una variable la cual preguntara si el usuario desea ver los 10 primero aprendices
mostrar = input("Deseas ver los 10 primeros de la lista? [si o no] ")

#Creamos unas condiciones las cuales si el usuario desea ver los 10 primero se los mostrar y si no lo desea se los mostrara completa
if mostrar.lower() == "si":
    print(aprendices[0:11])
    print(edades[0:11])
else:
    print(aprendices)
    print(edades)
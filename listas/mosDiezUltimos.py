#Muestre los 10 últimos aprendices de la lista

#Creamos una lista llamada aprendices con unos valores predeterminados y otra vacia llamada edades
aprendices = ["Juan Diego","Mathew Guarnizo","Maria Fernanda","Melissa","Nicolas Paulo","Miguel Angel","Stiven","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly","Camila","Stiwar","Lina Vanesa","Paula Garcia","Maria Paula","Vanesa","Kevin Hernandez","Yency","Matias","Sebastian Tovar","Cristian Peña","Dahiana","Kevin Eduardo","Santiago Tomas","Nicolas Fierro","Laura Benavidez","Willfran"]
edades = []

#Importamos el modulo ramdom el cual genera numeros aleatorios
import random

#Creamos un bucle el cual genera un total de 30 iteraciones.
for i in range(31):
    #creamos una variable la cual dara numeros randoms con la funcion "radint" que empiezan del 16 y terminan en el 20
    edad = random.randint(16,20)
    #Agregamos los datos de la variable edad a la lista edades
    edades.append(edad)

print(aprendices) #Imprimimos los resultados de las listas
print(edades)     #y edades

#Creamos una variable la cual preguntara si el usuario desea ver los 10 ultimos aprendices
mostrar = input("Deseas ver los 10 ultimos de la lista? [si o no] ")

#Creamos unas condiciones las cuales si el usuario desea ver los 10 ultimos aprendices se los mostrar y si no lo desea se los mostrara completa
if mostrar.lower() == "si":
    print(aprendices[20:30])
    print(edades[20:30])
else:
    print(aprendices)
    print(edades)
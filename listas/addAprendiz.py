#Agregue un aprendiz x al final de la lista

#Creamos una lista llamada aprendices con unos valores predeterminados y otra vacia llamada edades
aprendices = ["Juan Diego","Mathew Guarnizo","Maria Fernanda","Melissa","Nicolas Paulo","Miguel Angel","Stiven","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly","Camila","Stiwar","Lina Vanesa","Paula Garcia","Maria Paula","Vanesa","Kevin Hernandez","Yency","Matias","Sebastian Tovar","Cristian Peña","Dahiana","Kevin Eduardo","Santiago Tomas","Nicolas Fierro","Laura Benavidez","Willfran"]
edades = []

#Importamos el modulo ramdom el cual genera numeros aleatorios
import random

#Creamos un bucle el cual genera un total de 30 iteraciones.
for i in range(30):
    #creamos una variable la cual dara numeros randoms con la funcion "radint" que empiezan del 16 y terminan en el 20
    edad = random.randint(16,20)
    #Agregamos los datos de la variable edad a la lista edades
    edades.append(edad)

print(aprendices) #Imprimimos los resultados de las listas
print(edades)     #y edades

x = input("Ingresa el nombre del nuevo aprendiz: ") #Creamos una variable la cual almacene el valor que queremos agregar [nombre]
xE = int(input("Ingresa la edad del nuevo aprendiz: ")) #Creamos una variable la cual almacene el valor que queremos agregar [edad]

aprendices.append(x) #Agregamos el valor de la variable [x(nombre)] a la lista {aprendices}
edades.append(xE) #Agregamos el valor de la variable [xE(edad)] a la lista {edades}

#Finalmente imprimimos todas las listas
print(aprendices)
print(edades)